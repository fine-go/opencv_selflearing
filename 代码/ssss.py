import cv2
import numpy as np

capture = cv2.VideoCapture(0)
while(True):
    ret, frame= capture.read()
    gary = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gary = cv2.flip(gary, 1)
    cv2.imshow("gray",gary)
    if cv2.waitKey(20)==27:
        break


c = cv2.waitKey()
if c == 27:
    cv2.destoryALLWindows()
    
