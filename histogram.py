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

    # CALCULATE HISTOGRAM
    gray_hist = cv.calcHist([gray],[0],None,[256],[0,256])


    # DISPLAY THE OUTPUT IMAGE
    cv.imshow('gray',gray)  
    plt.figure()
    plt.title('Grayscale Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of pixels')
    plt.plot(gray_hist)
    plt.xlim([0,256])
    plt.show()

    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv.destroyAllWindows() 

