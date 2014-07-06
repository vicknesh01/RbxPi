import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
cap.set(3,300)
cap.set(4,300)
while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    #draw grid for basic rubix layout
    #the output image has a size of w=176 and h=144
    
    cv2.line(frame,(58,0),(58,144),(0,255,255),4,8,0)
    cv2.line(frame,(117,0),(117,144),(0,255,255),4,8,0)
    cv2.line(frame,(0,48),(176,48),(0,255,255),4,8,0)
    cv2.line(frame,(0,96),(176,96),(0,255,255),4,8,0)
  


    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    time.sleep(1)
    if k == 27:
        break

cv2.destroyAllWindows()
