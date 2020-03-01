import numpy as np
import cv2

img = cv2.imread(r'C:\Users\yangchao\Desktop\OpenCV\picture\1.jpg', 1)
cv2.imshow("image",img)
cv2.waitKey(0)

px = img[100, 100]
print(px)

blue = img[100,100,0]
print(blue)

green = img[100, 100, 1]
print(green)

red = img[100, 100, 2]
print(red)
