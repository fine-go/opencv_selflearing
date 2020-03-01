import  cv2
import numpy as np
from matplotlib import  pyplot as plt


def edga_demo(image):
    blurred = cv2.GaussianBlur(image, (3, 3), 0)
    gary = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    xgrad = cv2.Sobel(gary, cv2.CV_16SC1, 1, 0)
    ygrad = cv2.Sobel(gary, cv2.CV_16SC1, 0, 1)
    edge_output = cv2.Canny(gary, 10, 120)
    cv2.imshow("edge_output", edge_output)

    return edge_output


def contours_demo(image):
    '''dst = cv2.GaussianBlur(image, (9,7), 0)
    gary = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gary", gary)
    ret, demo = cv2.threshold(gary, 160, 255, cv2.THRESH_BINARY)
    cv2.imshow("threshold", demo)'''
    demo = edga_demo(image)
    cloneimage, contours, heriachy = cv2.findContours(demo, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cloneimage, contours, heriachy = cv2.findContours(demo, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)#仅仅返回最外围
    for i, contour in enumerate(contours):
        cv2.drawContours(image, contours, i, (255, 0, 0), 2)#-1表示填充
        print(i)
        print(cloneimage)
        print(heriachy)
    cv2.imshow("contours_image", image)

image = cv2.imread("C:/Users/yangchao/Desktop/OpenCV/picture/01.jpg")
cv2.imshow("image", image)
contours_demo(image)
c = cv2.waitKey(0)
if c == 27:
    cv2.destroyAllWindows()
