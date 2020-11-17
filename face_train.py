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
    haar_cascade = cv.CascadeClassifier('haar_face.xml')
    #haar_cascade = cv.CascadeClassifier('haarcascade_fullbody.xml')
    

    faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)


    # DISPLAY THE OUTPUT IMAGE
    cv.imshow('gray',gray)  
    print(len(faces_rect))
    for(x,y,w,h) in faces_rect:
    	cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)
    cv.imshow('Detected faces', frame)

    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv.destroyAllWindows() 

