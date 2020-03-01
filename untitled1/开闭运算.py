#开操作 = 膨胀+腐蚀
#闭操作 = 腐蚀+膨胀
import  cv2
import numpy as np
from matplotlib import  pyplot as plt

def open_demo(image):
    print(image.shape)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray,235,255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (31, 3))#模块的修改可以提取不同的东西
    result = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    cv2.imshow("open_result", result)

def close_demo(image):
    print(image.shape)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray,235,255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (38, 1))
    result = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("close_result", result)

def b():

    for i in range(1, 5):
        image = cv2.imread("C:/Users/yangchao/Desktop/OpenCV/picture/%d.jpg"%(i))
        cv2.imshow("image", image)
        close_demo(image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    b()
