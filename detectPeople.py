import cv2
import imutils
import numpy as np
import os
import sys
import imagezmq
import time

from ReceiveStream import ReceiveStream

def detect(img):

    # Getting Labels
    labelsPath = 'coco.names'
    LABELS = open(labelsPath).read().strip().split('\n')

    # Setting path to weights and  config file
    weightsPath = 'yolov3.weights'
    configPath = 'yolov3.cfg'

    # Loading YOLO trained on COCO Dataset
    net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)

    # Getting Image Shape
    (H, W) = img.shape[:2]

    # Getting Output layer names
    ln = net.getLayerNames()
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    # Creating blob from image to perform feature normalization
    blob = cv2.dnn.blobFromImage(img, 1 / 255.0, (416, 416), swapRB=True, crop=False)

    # Setting Input and performing forward pass through YOLO Network
    net.setInput(blob)
    layerOutputs = net.forward(ln)

    # Initialing required lists
    boxes = []
    confidences = []

    t1 = time.time()
    for output in layerOutputs:
        for detection in output:

            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]

            # If a person is detected with high confidence
            if (confidence > 0.5) and (classID == 0):
                # scaling bounding box coordinates according to size of original image
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY, width, height) = box.astype('int')

                # Converting into top-left coordinates
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))

                # Appending to lists
                boxes.append((x, y, int(width), int(height)))
                confidences.append(float(confidence))

    # Applying Non-Maximum Suppression to remove duplicate boxes
    idxs = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.3)
    j = 0
    if len(idxs) > 0:

        for i in idxs.flatten():

            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])

            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

            j += 1

    t2 = time.time()
    num = j

    timeText = "Detection Time: " + str(round((t2-t1),3)) + 'sec'
    detectionText = "No. of people detected: " + str(num)

    cv2.putText(img,detectionText,(W-330,20),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,0),1)
    cv2.putText(img, timeText, (W-330,40), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 1)


    return (img,num)
