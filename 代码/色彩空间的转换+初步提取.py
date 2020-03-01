import cv2
import numpy as np


image = cv2.imread("C:/Users/yangchao/Desktop/OpenCV/picture/2.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv",hsv)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)
YUV = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
cv2.imshow("YUV",YUV)

#通道的分离和修改
lower_hsv = np.array([0, 43, 46])
upper_hsv = np.array([10, 255, 255])
mast1 = cv2.inRange(hsv,lowerb=lower_hsv,upperb=upper_hsv)
cv2.imshow("mast1",mast1)

lower_hsv = np.array([156, 43, 45])
upper_hsv = np.array([180, 255, 255])
mast2 = cv2.inRange(hsv,lowerb=lower_hsv,upperb=upper_hsv)
cv2.imshow("mast2",mast2)

mast = cv2.add(mast1, mast2)
cv2.imshow("mast", mast)
c = cv2.waitKey(0)
if c==(27):
    cv2.destroyAllWindows()


