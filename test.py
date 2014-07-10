#RbxPI Alpha 0.1
#Color Detection Module
#Created By g15 (Vickneshwaran Elangkeeran)
# Licensed Under GPL


import cv2
import time
import numpy



raw_image = cv2.imread("test.jpg")
output = raw_image
raw_image = cv2.resize(raw_image,(raw_image.shape[1]/3,raw_image.shape[0]/3))
cv2.rectangle(output,(387,289),(468,369),(100,100,100),3,0,0)

ROI = raw_image[289:369,387:468]

mean = cv2.mean(ROI)
print "BLUE: ",int(mean[0]), "GREEN: ",int(mean[1]), "RED: ",int(mean[2])
cv2.imshow("output", raw_image)
cv2.imshow("ROI", ROI)

cv2.waitKey(0)
cv2.destroyAllWindows()