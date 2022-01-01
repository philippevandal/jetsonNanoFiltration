import numpy as np
import cv2
import RPi.GPIO as GPIO

button = 18  # BOARD pin 12, BCM pin 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN)

Cap = cv2.VideoCapture(0)
filename = input("Enter name of input file: ")
writerC = cv2.VideoWriter('/videos/{filename}.mp4', cv2.VideoWriter_fourcc(*'XVID'),8, (1280, 960))

while True:
    ret, frameC = Cap.read()     
    frameC = cv2.resize(frameC,(1280, 960))
    writerC.write(frameC)
    # cv2.imshow('frameC', frameC)
    frame = None
    #if GPIO.input(button):
    key = cv2.waitKey(30) & 0xff
    if key == 27:
        #GPIO.cleanup()
        break