import cv2
import numpy as np


capture = cv2.VideoCapture(1)
while(True):
    ret, frame = capture.read()
    frame = cv2.flip(frame, 1, 0)
    cv2.imshow("frame", frame)
    if cv2.waitKey(10)==27:
        break

capture.release()
cv2.destroyAllWindows()
