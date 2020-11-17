# import the opencv library 
import cv2 as cv
import numpy as np

# define a video capture object 
# vid = cv.VideoCapture(1) for the EasyCap usb
# vid = cv.VideoCapture(-1) for the Webcam
vid = cv.VideoCapture(-1) 


while(True): 
      
    # CAPTURE THE VIDEO FRAME 
    # by frame 
    ret, frame = vid.read() 
    mask = np.zeros((frame.shape[0],frame.shape[1]), dtype='uint8')
    cv.circle(mask,(350,200),100,255,-1)
    masked = cv.bitwise_and(frame, frame, mask=mask)

    # DISPLAY THE OUTPUT IMAGE
    cv.imshow('masked',masked)


    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv.destroyAllWindows() 

