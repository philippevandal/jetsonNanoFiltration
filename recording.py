import numpy as np
import cv2
import RPi.GPIO as GPIO

button = 18  # BOARD pin 12, BCM pin 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN)

Cap = cv2.VideoCapture(0)
writerC = cv2.VideoWriter('/home/filtration/Videos/Color_Video.mp4', cv2.VideoWriter_fourcc(*'XVID'),8, (2048, 1024))

while True:
    ret, frameC = Cap.read()     
    frameC = cv2.resize(frameC,(2048, 1024))
    writerC.write(frameC)
    # cv2.imshow('frameC', frameC)
    frame = None
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    if GPIO.input(button): 
        GPIO.cleanup()
        break