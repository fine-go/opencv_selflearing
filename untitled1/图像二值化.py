import  cv2
import numpy as np
from matplotlib import  pyplot as plt

def threshold_demo(image):
    gary = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gary,  130,255, cv2.THRESH_TOZERO)# | cv2.THRESH_TRIANGLE)
    print("%s"%ret)
    cv2.imshow("binary", binary)


def local_threshold_demo(image):
    gary = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gary,  130,255, cv2.THRESH_TOZERO)# | cv2.THRESH_TRIANGLE)
    print("%s"%ret)
    cv2.imshow("binary", binary)

def custom_threshold(image):
    gary = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    h, w = gary.shape[:2]
    m = np.reshape(gary, [1, w*h])
    mean = m.sum()/ (w *h)
    print("mean ; ", mean)
    ret, binary = cv2.threshold(gary, mean, 255, cv2.THRESH_BINARY)
    cv2.imshow("binary", binary)



image = cv2.imread("C:/Users/yangchao/Desktop/OpenCV/picture/666.jpg")
cv2.imshow("image", image)
h, w = image.shape[:2]
print(image.shape[:2])

custom_threshold(image)

c = cv2.waitKey(0)
if c == 27:
    cv2.destroyAllWindows()