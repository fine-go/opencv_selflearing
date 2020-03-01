import cv2
import time
import numpy as np
import threading

index = 0
cap = cv2.VideoCapture("rtsp://192.168.10.103:8554/stream0")

while cap.isOpened():
    ret, frame = cap.read()
    print(index)
    index = index + 1

    cv2.imshow("frame", frame)
    a = time.time()

    if np.mod(index, 10) == 0:

        cv2.imwrite("picture/1.bmp",frame)
        b = time.time()
        print("cost = %f"% (b-a))
    else:
        pass
    cv2.waitKey(20)

