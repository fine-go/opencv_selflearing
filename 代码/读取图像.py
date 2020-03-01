import numpy as np
import cv2

#读取图像
img1 = cv2.imread("C:/Users/yangchao/Desktop/OpenCV/picture/1.jpg", -1)
    #img = cv2.imread("C:\Users\yangchao\Desktop\OpenCV\picture\1.jpg", -1)
    #img = cv2.imread("C:\Users\yangchao\Desktop\OpenCV\picture\1.jpg", 0)
cv2.imshow("image1", img1)

cv2.waitKey(0)
img2 = cv2.imread("C:/Users/yangchao/Desktop/OpenCV/picture/2.jpg", 1)
cv2.imshow("image2", img2)
#删除特定窗口
cv2.waitKey(0)
cv2.destroyWindow("image2")
cv2.waitKey(0)

