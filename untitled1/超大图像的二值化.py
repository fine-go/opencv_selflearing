'''

2019年2月13日20:53:24
对于大图像的二值化因为噪点的原因可以进行分区操作
之后用在写出来
或者resize进行全图分割
注意自适应阈值的使用

'''


import  cv2
import numpy as np
from matplotlib import  pyplot as plt

def big_image_demo(image):
    print(image.shape)
    cw = 256
    ch = 256
    h, w = image.shape[:2]
    gary = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    for row in range(0, h, ch):
        for col in range(0, w, cw):
            roi = gary[row:row+ch,col:col+cw ]
           # ret, dst = cv2.threshold(roi, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TOZERO)
            dst = cv2.adaptiveThreshold(roi, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 127, 25)
            gary[row:row+ch,col:col+cw ] = dst
    cv2.imwrite("C:/Users/yangchao/Desktop/OpenCV/picture/hhh6.jpg", gary)



image = cv2.imread("C:/Users/yangchao/Desktop/OpenCV/picture/hhh.jpg")
#cv2.imshow("image", image)

big_image_demo(image)

c = cv2.waitKey(0)
if c == 27:
    cv2.destroyAllWindows()
