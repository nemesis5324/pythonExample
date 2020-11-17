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
    blank = np.zeros(frame.shape[:2], dtype='uint8')

    # COLOR SPACE EDITING
    b,g,r = cv.split(frame)
    merged = cv.merge([b,g,r])
    blue = cv.merge([b,blank,blank])
    red  = cv.merge([blank,blank,r])
    green  = cv.merge([blank,g,blank])
    # DISPLAY THE OUTPUT IMAGE
    cv.imshow('frame',frame)  
    cv.imshow('blue',blue) 
    cv.imshow('red',red)  
    cv.imshow('green',green) 



    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv.destroyAllWindows() 

