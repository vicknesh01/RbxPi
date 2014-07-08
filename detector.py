import cv2
import cv2.cv
import numpy as np
import time

cap = cv2.VideoCapture(0)
#override input resolution here
cap.set(3,240) #width
cap.set(4,160) #height

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



def detectCube():
	
	global result,low,high,lx0,ly0,lx1,ly1,lx2,ly2,o1,o2,o3
	

	#set the edge detection low treshhold
	low = 10
	#set the edge detection high treshhold
	high = 150

	#get raw camera feed for manipulation
	_, raw = cap.read()
	#apply Gaussian Blur to the feed to reduce noise
	result = cv2.GaussianBlur(raw,(3,3),0)
	#change the feed to grayscale for better object detection
	result = cv2.cvtColor(result,cv2.COLOR_BGR2GRAY)
	#apply Laplacian Operator to define corners and lines more
	result= cv2.Laplacian(result,0)
	#Output Laplician Output for debugging purpose. Comment to Disable
	o1 = result
	#Do Canny Detection on the image to detect edges
	result = cv2.Canny(result,low,high,apertureSize = 3)
	#output Canny Detection for debugging purpose. Comment to disable
	o2 = result
	#generate straight lines using HoughLines Algorythm
	lines = cv2.HoughLines(result,1,np.pi/180,50)
	#if no line then stay silent, if got lines then run the for loop
	if lines != None:
		#calculates the starting coordinates and the ending coordinates of the lines	
		for rho,theta in lines[0]:
			a = np.cos(theta)
			b = np.sin(theta)
			lx0 = a*rho
			ly0 = b*rho
			lx1 = int(lx0 + 1000*(-b))
			ly1 = int(ly0 + 1000*(a))
			lx2 = int(lx0 - 1000*(-b))
			ly2 = int(ly0 - 1000*(a))
			#debugging purposes (DELETE if not needed)
			print "Cube Detected!"
			#draws the line on the preview for debugging purposes
			cv2.line(frame,(int(lx1),int(ly1)),(int(lx2),int(ly2)),(0,0,255),2)


#execute while each frame is recieved from the source
while(1):



	# Take each frame and load it into the FRAME variable
	global frame
	_, frame = cap.read()
	



	
    	
	calculateGuidelineGrid() 	#calculate the grid to align the rubix [disable if not needed]
	drawGuidelineGrid() 		#draw the grid that has been calculated [disable if not needed]
	
     
	
	detectCube()			#run the function to detect the cube


	cv2.imshow('frame',frame)	#this will output video stream to window [disable if not needed]
    	cv2.imshow('processed',result)	#this will output video stream to window [disable if not needed]
	cv2.imshow('laucian',o1)	#this will output video stream to window [disable if not needed]
	cv2.imshow('canny',o2)		#this will output video stream to window [disable if not needed]
	
    
	

	#end the program if ESC is pressed
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
