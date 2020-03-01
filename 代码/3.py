# coding: utf-8
import cv2
import numpy 

# 创建黑色正方形图像
img = numpy.zeros((3,3), dtype = numpy.uint8)
print(img)

#每个像素都是由8位整数表示，范围是0—255
#先将其变为BGR格式

img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
print(img)

img1 = cv2.imread(r'C:\Users\yangchao\Desktop\OpenCV\picture\1.jpg',0)
cv2.imshow("imgae", img1)


