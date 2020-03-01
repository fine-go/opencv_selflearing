'''

原理：reduce = 高斯模糊 + 降采样

expand = 扩大 + 卷积

拉普拉斯金字塔 l1= g1 —expand（g2）
反应的轮廓

'''

import  cv2
import numpy as np
from matplotlib import  pyplot as plt

def pyramid_demo(image):
    level = 3
    temp = image.copy()
    pyramid_images = []
    for i in range(level):
        dst = cv2.pyrDown(temp)
        pyramid_images.append(dst)
        cv2.imshow("pyramid_demo"+str(i), dst)
        temp = dst.copy()
    return pyramid_images


'''def lapalian_demo(image):
    pyramid_images = pyramid_demo(image)
    level = len(pyramid_images)
    print(level)
    for i in range(level-1, -1, -1):
        if (i - 1)<0:
            expend = cv2.pyrUp(pyramid_images[i], dstsize=image.shape[:2])
            lpls = cv2.subtract(pyramid_images, expend)
            cv2.imshow("lapalian_demo"+str(i), lpls)
        else:
            expend = cv2.pyrUp(pyramid_images[i], dstsize=pyramid_images[i - 1].shape[:2])
            lpls = cv2.subtract(pyramid_images, expend)
            cv2.imshow("lapalian_demo"+str(i), lpls)
'''
#缕清i


image = cv2.imread("C:/Users/yangchao/Desktop/OpenCV/picture/1.jpg")
cv2.imshow("image", image)
pyramid_demo(image)
#lapalian_demo(image)

c = cv2.waitKey(0)
if c == 27:
    cv2.destroyAllWindows()
