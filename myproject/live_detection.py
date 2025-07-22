import cv2
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO(r"C:\Users\Meena Girish\Desktop\runs\detect\train2\weights\best.pt")

# Define class colors
class_colors = {
    0: (0, 0, 255),  # Blue for Blister packs
    1: (0, 255, 255),  # cyan for charger
    2: (255, 255, 255), # white for earbud
    3: (0, 255, 127), #yellow for ID card
    4: (51, 0, 153), #purple for mobile
    5: (255, 51, 255), #pink for paper
    6: (255, 51, 51), #salmon for paperbag
    7: (102, 255, 51), #lightgreen for pen
    8: (0, 153, 0), #green for plastic
    9: (204, 0, 204), #violet for toothbrush
}

# Open camera
cap = cv2.VideoCapture("http://192.168.190.188:8080/video")
cap.set(cv2.CAP_PROP_BUFFERSIZE,1)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO detection
    results = model(frame, conf=0.9, iou=0.5)

    # Ensure YOLO is detecting multiple objects
    for result in results:
        boxes = result.boxes  # Get all detected boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Get box coordinates
            class_id = int(box.cls[0])  # Get class ID
            conf = float(box.conf[0])  # Confidence score

            # Get class name & color
            label = f"{model.names[class_id]}: {conf:.2f}"
            color = class_colors.get(class_id, (153, 153, 153))  # Default to grey if class not found

            # Draw bounding box & label
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Show the frame
    cv2.imshow("YOLO Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()