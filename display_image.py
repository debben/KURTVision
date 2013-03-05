''' filename : display_image.py

Description : This sample demonstrates how to read an image, display it on the window and print image size.

This script also tries to find lines in the image and highlights them red.'''

import cv2
import sys
import math
import numpy as np

if len(sys.argv)!=2:                  ## Check for error in usage syntax
    print "Usage : python display_image.py <image_file>"

else:
    img = cv2.imread(sys.argv[1],cv2.CV_LOAD_IMAGE_COLOR)  ## Read image file

    if (img == None):                      ## Check for invalid input
        print "Could not open or find the image"
    else:
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)        
        edges = cv2.Canny(gray, 80, 120)
        lines = cv2.HoughLinesP(edges,1, math.pi/4,2,None,30,1)
        for line in lines[0]:
            pt1 = (line[0],line[1])
            pt2 = (line[2],line[3])
            cv2.line(img,pt1, pt2, (0,0,255),3)
        cv2.namedWindow('Display Window')        ## create window for display
        cv2.imshow('Display Window',img)         ## Show image in the window
        print "size of image: ",img.shape        ## print size of image
        cv2.waitKey(0)                           ## Wait for keystroke
        cv2.destroyAllWindows()                  ## Destroy all windows