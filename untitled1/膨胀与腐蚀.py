import  cv2
import numpy as np
from matplotlib import  pyplot as plt

def erode_deom(image):
    print(image.shape)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray,235,255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    dst = cv2.erode(binary, kernel=kernel)
    cv2.imshow("dst", dst)

def dilate_deom(image):
    print(image.shape)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray,220,255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    dst = cv2.dilate(binary, kernel=kernel)
    cv2.imshow("dst1", dst)


image = cv2.imread("C:/Users/yangchao/Desktop/OpenCV/picture/01.jpg")
cv2.imshow("image", image)
erode_deom(image)
dilate_deom(image)
c = cv2.waitKey(0)
if c == 27:
    cv2.destroyAllWindows()
