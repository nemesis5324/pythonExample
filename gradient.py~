# import the opencv library 
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# define a video capture object 
# vid = cv.VideoCapture(1) for the EasyCap usb
# vid = cv.VideoCapture(-1) for the Webcam
vid = cv.VideoCapture(-1) 


while(True): 
      
    # CAPTURE THE VIDEO FRAME 
    # by frame 
    ret, frame = vid.read() 
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)


    # THRESHOLDING
    laplace = cv.Laplacian(gray, cv.CV_16S)
    laplace = np.uint8(np.absolute(laplace))

    canny = cv.Canny(gray, 150, 175)
    # DISPLAY THE OUTPUT IMAGE
    cv.imshow('gray',gray)  
    cv.imshow('Laplacian',laplace) 
    cv.imshow('canny', canny)

    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv.destroyAllWindows() 

