# import the opencv library 
import cv2 as cv
import numpy as np

# define a video capture object 
# vid = cv.VideoCapture(1) for the EasyCap usb
# vid = cv.VideoCapture(-1) for the Webcam
vid = cv.VideoCapture(0) 


while(True): 
      
    # CAPTURE THE VIDEO FRAME 
    # by frame 
    ret, frame = vid.read() 
    rectangle = np.zeros((400,400), dtype='uint8')
    circle = np.zeros((400,400), dtype='uint8')
    result = np.zeros((400,400), dtype='uint8')

    cv.rectangle(rectangle,(30,30),(370,370),255,-1)
    cv.circle(circle,(200,200),200,255,-1)
    image_and= cv.bitwise_and(rectangle,circle)
    image_or= cv.bitwise_or(rectangle,circle)
    image_xor= cv.bitwise_xor(rectangle,circle)
    # BITWISE


    # DISPLAY THE OUTPUT IMAGE
    #cv.imshow('frame',frame)
    #print(frame.shape)
    cv.imshow('rectangle',rectangle) 
    cv.imshow('circle',circle)
    cv.imshow('image_and',image_and)
    cv.imshow('image_or',image_or)
    cv.imshow('image_xor',image_xor)
 
    




    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv.destroyAllWindows() 

