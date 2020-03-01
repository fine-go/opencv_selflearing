import cv2
import numpy as np
from scipy import ndimage

kernel_3x3 = np.array([[-1, -1, -1],
                      [-1, 2 , -1],
                      [-1, -1, -1]])

kernel_5x5 = np.array([[-1, -1, -1, -1, -1],
                       [-1,  1,  2,  1, -1],
                       [-1,  2,  4,  2, -1],
                       [-1,  1,  2,  1, -1],
                       [-1, -1, -1, -1, -1]])
                      


image = cv2.imread("C:/Users/yangchao/Desktop/OpenCV/picture/1.jpg", 0)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv",hsv)
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
k3 = ndimage.convolve(mast, kernel_3x3)
k5 = ndimage.convolve(mast, kernel_5x5)


blurred = cv2.GaussianBlur(mast, (11,11), 0)
g_hpf = img - blurred
cv2.imshow("3x3", k3)
cv2.imshow("5x5", k5)


c = waitKey(20)
if c== 27:
    cv2.destoryALLWindows()
