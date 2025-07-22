# Waste-classification-using-object-detection
Programming lang:Python  
Front-end:Html,css,javascript
Back-end:Flask,Yolov8,Opencv
Data preparation:Roboflow for labelling
This repository contains the files and instructions used for the project "Waste classification using object detection"
STEP1(DATA COLLECTION):Nine datasets are stored in "cdataset" folder to label them.
STEP2(DATA LABELLING):Datasets are labelled using roboflow and stored as train,valid,test in "CDATA" folder.
STEP3(MODEL SELECTION AND TRAINING):YOLOv8 is used as object detection model and is trained using labelled datasets in command prompt.
STEP4(LIVE DETECTION):Live detection code is created using YOLOv8 and Opencv.It contains the path of trained datasets.(live detction code in "myproject" folder).
STEP5(FRONT END DEV):User friendly interface is created to capture waste in real time and this front end is connected with flask backened for communication between server(batch file) and webpage(batch file is needed to run live detection on clicking "open camera" in webpage.
