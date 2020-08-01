import cv2
import imagezmq
import sys

def ReceiveStream():
    image_hub = imagezmq.ImageHub()
    rpi_name, image = image_hub.recv_image()
    #cv2.imshow(rpi_name, image)  # 1 window for each RPi
    #cv2.waitKey(1)
    print('mil gyi photo')
    image_hub.send_reply(b'OK')
    return (rpi_name,image)
