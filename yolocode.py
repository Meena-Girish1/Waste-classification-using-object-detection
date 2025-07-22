from ultralytics import YOLO  # Ensure YOLO is correctly imported

if __name__ == "__main__":
    model = YOLO("yolov8n.pt")  # Load the YOLO model
    model.train(data=r"C:\Users\Meena Girish\Desktop\CDATA\data.yaml", epochs=50, imgsz=640) #To train yolo model with labelled datasets