# import the opencv library 
import cv2 as cv
import numpy as np

# define a video capture object 
# vid = cv.VideoCapture(1) for the EasyCap usb
# vid = cv.VideoCapture(-1) for the Webcam
vid = cv.VideoCapture(1) 


while(True): 
      
    # CAPTURE THE VIDEO FRAME 
    # by frame 
    ret, frame = vid.read() 

    # BLURRING
    average = cv.blur(frame,(7,7))
    gaussian = cv.GaussianBlur(frame,(7,7),cv.BORDER_DEFAULT)
    median = cv.medianBlur(frame,3)

    # DISPLAY THE OUTPUT IMAGE
    cv.imshow('frame',frame) 
    cv.imshow('avarage',average)  
    cv.imshow('gaussian',gaussian)
    cv.imshow('median',median) 
 




    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv.destroyAllWindows() 

