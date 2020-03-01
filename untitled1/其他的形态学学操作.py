#tophat顶帽： 原图像与开操作的差值
#blackhat黑帽：原图像与闭操作的差值
import  cv2
import numpy as np
from matplotlib import  pyplot as plt

def top_Hat_demo(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    dst = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)
    cimage = np.array([gray.shape], np.uint8)
    cimage = 100
    dst = cv2.add(dst ,cimage)
    cv2.imshow("top_gat_demo", dst)


def black_hat_demo(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))
    dst = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)
    cimage = np.array([gray.shape], np.uint8)
    cimage = 100
    dst = cv2.add(dst ,cimage)
    cv2.imshow(" black_hat_demo", dst)

def gary_black_hat_demo(image):#相当于方向提取
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, binary =cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))
    dst = cv2.morphologyEx(binary, cv2.MORPH_BLACKHAT, kernel)
    cimage = np.array([gray.shape], np.uint8)
    cimage = 100
    dst = cv2.add(dst ,cimage)
    cv2.imshow(" gary_black_hat_demo", dst)

def t_gary_black_hat_demo(image):#相当于方向提取
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, binary =cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))
    dst = cv2.morphologyEx(binary, cv2.MORPH_RECT, kernel)
    cimage = np.array([gray.shape], np.uint8)
    cimage = 100
    dst = cv2.add(dst ,cimage)
    cv2.imshow(" t_gary_black_hat_demo", dst)

image = cv2.imread("1.jpg")
cv2.imshow("image", image)

t_gary_black_hat_demo(image)
c = cv2.waitKey(0)
if c == 27:
    cv2.destroyAllWindows()
