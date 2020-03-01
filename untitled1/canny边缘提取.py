import  cv2
import numpy as np
from matplotlib import  pyplot as plt
#降噪
#求梯度
#非最大信号的抑制
#输出二值图像


def edge_demo(image):
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    xgrad = cv2.Sobel(gray, cv2.CV_16SC1, 1, 0)
    ygrad = cv2.Sobel(gray, cv2.CV_16SC1, 0, 1)
    print(xgrad)
    print(type(xgrad))
    edge_output = cv2.Canny(xgrad, ygrad,50, 150)
    cv2.imshow("edge_output", edge_output)

    dst = cv2.bitwise_and(image, image, mask=edge_output)
    cv2.imshow("edge_output_color", dst)



image = cv2.imread("C:/Users/yangchao/Desktop/OpenCV/picture/1.jpg")
cv2.imshow("image", image)
edge_demo(image)
c = cv2.waitKey(0)
if c == 27:
    cv2.destroyAllWindows()

