
# import the opencv library 
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# define a video capture object 
# vid = cv.VideoCapture(1) for the EasyCap usb
# vid = cv.VideoCapture(-1) for the Webcam
vid = cv.VideoCapture(1) 
blank = np.zeros((300,300,3),dtype='uint8')
green = np.zeros((300,300,3),dtype='uint8')
green[:] = 0,255,0

#plt.subplot(121),plt.imshow(blank)
#plt.title('Blank Image'), plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(green)
#plt.title('Green Image'), plt.xticks([]), plt.yticks([])
#plt.show()

# Change resolution function
#def changRes(width, height):
#	capture.set(3,width)
#	capture.set(4,height)	

# Rescale the frame
def rescaleFrame(frame, scale=0.75):
	width  = int(frame.shape[1] * scale)
	height = int(frame.shape[0] * scale)
	dimensions = (width, height)
	return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

  
while(True): 
      
    # Capture the video frame 
    # by frame 
    ret, frame = vid.read() 
    
    #dilated = cv.dilate(edges,(7,7),iterations=3)
    #eroded = cv.erode(dilated,(7,7),iterations=3)
    #resized = cv.resize(frame,(1280,960),interpolation=cv.INTER_CUBIC)
    #blur = cv.GaussianBlur(frame,(7,7),cv.BORDER_DEFAULT)
    # Display the resulting frame 
    # cv.imshow('frame', frame) 
    #cv.rectangle(frame,(264,160),(376,320),(0,255,0), thickness=2)
    cv.line(frame,(160,240),(480,240),(0,255,0),thickness=2)
    cv.line(frame,(320,120),(320,360),(0,255,0),thickness=2)
    cv.circle(frame,(320,240),60,(0,255,0),thickness=2)

    # Image transformation
    
    # Contour detection
    # STEP 1: CREATE BINARY IMAGE
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #blur = cv.GaussianBlur(gray,(7,7),cv.BORDER_DEFAULT)
    #edges = cv.Canny(blur,100,200)

    # STEP 2: APPLY THRESHOLD TO MAKE OBJECT DIFFERENT
    ret, thresh = cv.threshold(gray, 110,255,cv.THRESH_BINARY) 
    dilated = cv.dilate(thresh,(7,7),iterations=3)
    blank = np.zeros((thresh.shape[0],thresh.shape[1],3), dtype='uint8')
 
    # STEP 3: COUNT HOW MANY CONTOURS IN THE IMAGE
    contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    print(len(contours))
    cv.drawContours(blank, contours,-1,(0,0,255),2)
    
	


    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(frame,'Camera test',(50,50), font, 1,(0,0,255),2)
    
    
    # STEP 4: DISPLAY THE OUTPUT IMAGE
    cv.imshow('frame',frame)  
    cv.imshow('thresh',thresh)  
    cv.imshow('Contours', blank)  


    #Drawing 
    

    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv.destroyAllWindows() 

