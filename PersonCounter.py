import cv2
import imutils
import numpy as np
import os
import sys
import imagezmq
import time

from ReceiveStream import ReceiveStream
from detectPeople import detect
from Database import InsertIntoTable

while True:
    num = -1
    rpi_image, img= ReceiveStream()
    img, num = detect(img)
    print("No. of people: ",num)
    cv2.imwrite("Detections/detection.jpg",img)
    if num > -1:
        InsertIntoTable(num,'People')
    #cv2.imshow(rpi_image,img)
    #cv2.waitKey(0)
