import cv2
import numpy as np

capture=cv2.VideoCapture(0)
while(True):
    ret,flame=capture.read()
    flame=cv2.flip(flame,1)
    cv2.imshow("flame",flame)
    if cv2.waitKey(10)==27:
        break

capture.release()
cv2.destroyAllWindows()

