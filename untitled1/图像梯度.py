import  cv2
import numpy as np
from matplotlib import  pyplot as plt

#找边缘

def laplian_demo(image):
    #dst = cv2.Laplacian(image, cv2.CV_32F)
    #lpls = cv2.convertScaleAbs(dst)用拉普拉斯算子搞的
    #自定义算子搞的
    kernel = np.array([[0, 1, 0],
                       [1, -8, 1],
                       [0, 1, 0]])
    dst = cv2.filter2D(image, cv2.CV_32F, kernel=kernel)
    grad =  cv2.convertScaleAbs(dst)
    cv2.imshow("laplian_demo", grad)

def sobel_demo(image):
    grad_x = cv2.Scharr(image, cv2.CV_32F, 1, 0)#增强的边缘很弱的边缘也可以
    grad_y = cv2.Scharr(image, cv2.CV_32F, 0, 1)

    #grad_x = cv2.Sobel(image, cv2.CV_32F, 1, 0)
    #grad_y = cv2.Sobel(image, cv2.CV_32F, 0, 1)
    gradx =  cv2.convertScaleAbs(grad_x)
    grady = cv2.convertScaleAbs(grad_y)
    cv2.imshow("gradient_x", gradx)
    cv2.imshow("gradient_y", grady)

    gradxy = cv2.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv2.imshow("gradientxy", gradxy)

image = cv2.imread("C:/Users/yangchao/Desktop/OpenCV/picture/666.jpg")
cv2.imshow("image", image)

#sobel_demo(image)
laplian_demo(image)
c = cv2.waitKey(0)
if c == 27:
    cv2.destroyAllWindows()
