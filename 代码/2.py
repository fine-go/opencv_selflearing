import cv2
img = cv2.imread('C:/Users/yangchao/Desktop/OpenCV/picture/1.jpg',0)
cv2.namedWindow('1')
cv2.imshow('1',img)
#灰度化处理

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.namedWindow('2')
cv2.imshow('2',img)

#二值化处理

ret,im_fixed=cv2.threshold(gray,0,20,cv2.THRESH_BINARY)
cv2.namedWindow('3')
cv2.imshow('3',img)
