import  cv2
import numpy as np
from matplotlib import  pyplot as plt

#参数方程所对应的两点确定的直线
#基于边缘检测
#霍夫直线空间

def lina_dectection(image):
    gary = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gary, 50, 150,apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
    print(lines)
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0+1000*(-b))
        y1 = int(y0+1000*(a))
        x2 = int(x0-1000*(-b))
        y2 = int(y0-1000*(a))
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv2.imshow("image1", image)

def line_detect_possible_demo(image):
    gary = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gary, 50, 150,apertureSize=3)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=50, maxLineGap=10)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        print(line[0])
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv2.imshow("image_line", image)

image = cv2.imread("C:/Users/yangchao/Desktop/OpenCV/picture/line.jpg")
cv2.imshow("image", image)

lina_dectection(image)
line_detect_possible_demo(image)
c = cv2.waitKey(0)
if c == 27:
    cv2.destroyAllWindows()
