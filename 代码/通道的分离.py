#通道的分离splitapi的使用
import cv2
import numpy as np

image = cv2.imread("C:/Users/yangchao/Desktop/OpenCV/picture/2.jpg")
#RGB通道的分离
b, g, r = cv2.split(image)
cv2.imshow("blue", b)
cv2.imshow("green", g)
cv2.imshow("rad", r)

#hsv通道的分离
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
cv2.imshow("h", h)
cv2.imshow("s", s)
cv2.imshow("v", v)


c = cv2.waitKey(0)
if c==(27):
    cv2.destroyAllWindows()
