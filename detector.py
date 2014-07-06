import cv2
import cv2.cv
import numpy as np
import time

cap = cv2.VideoCapture(0)
#override input resolution here
cap.set(3,240) #height?
cap.set(4,160) #width?

#get stream size and other info
print "INPUT VIDEO WIDTH:",cap.get(3)
print "INPUT VIDEO HEIGHT:",cap.get(4)

input_width = cap.get(3)
input_height = cap.get(4)






# a function to draw the grids on the video capture

def calculateGuidelineGrid():
	#this will calculate the coordinates for the gridlines
	global x1,x2,x3,x4,x5,x6,x7,x8,y1,y2,y3,y4,y5,y6,y7,y8,widthInc,heightInc
	widthInc= input_width/3
	heightInc= input_height/3
	x1=widthInc
	y1=0
	x2=widthInc*2
	y2=0
	x3=input_width
	y3=heightInc
	x4=input_width
	y4=heightInc*2
	x5=x2
	y5=input_height
	x6=x1
	y6=input_height
	x7=0
	y7=y4
	x8=0
	y8=y3	
	


def drawGuidelineGrid():
#draws the actual grid on the capture WARNING!!: MUST RUN calculateGuidelineGrid First
	
	cv2.line(frame,(int(x1),int(y1)),(int(x6),int(y6)),(0,255,255),2,8,0)
	cv2.line(frame,(int(x2),int(y2)),(int(x5),int(y5)),(0,255,255),2,8,0)
	cv2.line(frame,(int(x8),int(y8)),(int(x3),int(y3)),(0,255,255),2,8,0)
	cv2.line(frame,(int(x7),int(y7)),(int(x4),int(y4)),(0,255,255),2,8,0)




while(1):



# Take each frame
	_, frame = cap.read()
	
#draw grid for basic rubix layout



    
    
	calculateGuidelineGrid()
	drawGuidelineGrid()

    

    
	

	cv2.imshow('frame',frame)
    
    
    
	


	k = cv2.waitKey(5) & 0xFF
	#time.sleep(1)
	if k == 27:
		break

cv2.destroyAllWindows()
