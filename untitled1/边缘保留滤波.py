import  cv2
import numpy as np

def di_demo(image):#高斯双边模糊
    #d:一般默认为0 通过后面算前面，后面表示色彩方向的范围尽可能大，和空间方向上的范围尽可能小
    dst = cv2.bilateralFilter(image, 0, 45, 2)
    cv2.imshow("di_demo", dst)

#均值偏移滤波
def mean_shift_demo(img):
    dst = cv2.pyrMeanShiftFiltering(src=img,sp=15,sr=20)
    '''
    均值偏移滤波处理，想当与把图片转油画的操作
    src: 原图像
    sp：空间窗的半径（The spatial window radius）
    sr: 色彩窗的半径（The color window radius）
    通过均值迁移来进行边缘保留滤波有时会导致图像过度模糊
    '''
    cv2.imshow('mean_shift_demo',dst)


image = cv2.imread("C:/Users/yangchao/Desktop/OpenCV/picture/666.jpg")
cv2.imshow("image", image)

di_demo(image)
#mean_shift_demo(image)
c = cv2.waitKey(0)
if c == 27:
    cv2.destroyAllWindows()

