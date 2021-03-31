from yolov4.tf import YOLOv4
import cv2
import math
import matplotlib.pyplot as plt
import time

# YOLO SYSTEM
width = 224
height = 224
yolo = YOLOv4()
yolo.classes = "coco.names"
yolo.input_size = (width, height)
yolo.make_model()
yolo.load_weights("yolov4.weights", weights_type="yolo")
bboxList = []


# VIDEO CAPTURE
cap = cv2.VideoCapture('VID_20210308_130629.mp4')

if not cap.isOpened():
    ValueError("No video feed")

frameNo = 0
start = time.time()
while True:
    ret, frame = cap.read()
    frameNo = frameNo + 1
    height, width, channels = frame.shape
    img = cv2.resize(frame, (244, 224))
    bbox = yolo.predict(img)
    annotatedImg = yolo.draw_bboxes(img, bbox)
    resizedAnnImg = cv2.resize(annotatedImg, (int(width/2), int(height/2)))
    if len(bbox) < 5:
        bboxList.append(bbox)
    else:
        bboxList = []
    cv2.imshow('YOLOv4', resizedAnnImg)
    c = cv2.waitKey(1)
    if c == 27:
        end = time.time()
        break

# Create confusion Matrix
# Read in Image as above and read in label (dependant on how it is presented)
# Compare the generted label with the label provided to asses
# True positive, True negative, False positive, False negatives

cap.release()
cv2.destroyAllWindows()

for i in bboxList:
    print(i)

print("fps is roughly: {:3f}".format(frameNo/((end - start)/1000)))







