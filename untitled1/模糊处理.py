import  cv2
import numpy as np


def blur_demo(image):#均值模糊去随机噪声
    #ksize :表示卷积核的大小
    dst = cv2.blur(image,(5, 5))
    cv2.imshow("blur_demo",dst)

def median_demo(image):#中值模糊,去椒盐噪声
    #ksize :表示卷积核的大小
    dst = cv2.medianBlur(image, 5)
    cv2.imshow("median_demo",dst)

def custom_demo(image):#自定义模糊
    #kernel = np.ones([5, 5], np.float32)/25
    #自定义算子，加起来为奇数，中和为0梯度， 1锐化
    #ddepth:-1,det输出anchor中心
    kernel = np.array([[0, -1, 0],[-1, 5, -1],[0, -1, 0]], np.float32)
    dst = cv2.filter2D(image,-1, kernel=kernel)
    cv2.imshow("custom_demo",dst)


image = cv2.imread("C:/Users/yangchao/Desktop/OpenCV/picture/666.jpg")
cv2.imshow("image", image)

blur_demo(image)
median_demo(image)
custom_demo(image)
c = cv2.waitKey(0)

if c == 27:
    cv2.destroyAllWindows()
















