import  cv2
import numpy as np
from matplotlib import pyplot as plt

def plot_demo(image):
    #第一个统计图像中像素的频次的, 256表示bins的个数，【0， 256】表示范围
    plt.hist(image.ravel(), 256, [0, 256])
    plt.show()

def image_hist(image):#画三通道图像的直方图
    color = ('b', 'g', 'r')#这里画笔颜色的值可以为大写或小写或只写首字母或大小写混合
    for i, color in enumerate(color):
        hist  = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color)
        plt.xlim([0, 256])
    plt.show()


#画部分图像的直方图

def bufen_deom(image):#创建掩码
    mask = np.zeros(image.shape[:2], np.uint8)
    mask[100:300, 100:300] = 255
    masked_image = cv2.bitwise_and(image, image, mask =  mask)
    cv2.imshow("masked_image", masked_image)

    hist_full = cv2.calcHist([image], [0], None, [256], [0, 256])
    hist_mask = cv2.calcHist([image], [0], mask, [256], [0, 256])
    plt.plot(hist_full)
    plt.plot(hist_mask)
    plt.show()




image = cv2.imread("C:/Users/yangchao/Desktop/OpenCV/picture/1.jpg", 0)
cv2.imshow("image", image)
#plot_demo(image)
bufen_deom(image)
#image_hist(image)
c = cv2.waitKey(0)
if c == 27:
    cv2.destroyAllWindows()
