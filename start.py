# these imports let you use opencv
import cv2 #opencv itself
import numpy as np # matrix manipulations

cap = cv2.VideoCapture(1)
n=0; #let us have a counter
flag, img = cap.read() # get an initial frame
cv2.namedWindow('outputwindow') # open a window for output
cv2.imshow('outputwindow',img) # put the image in the output window

while True:

#read a frame from the video capture obj
    flag, img = cap.read()

    # the line below just copies the input image to the output image.
    # try replacing it with some code from the tutorial
    output_image=img.copy()

    cv2.imshow('outputwindow',output_image) # put the image in the output window

    # wait for someone to press escape then destroy the output window 
    if cv2.waitKey(2) & 0xff == 27:
        cv2.destroyAllWindows()
        break
    print("Finished frame {}".format(n))
    n=n+1

