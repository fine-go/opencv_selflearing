import  cv2
import numpy as np
from matplotlib import  pyplot as plt

def measure_object(image):
    dst = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(dst, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    print(ret)
    cv2.imshow("binary", binary)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        print(area)
        x, y, w, h = cv2.boundingRect(contour)
        mm = cv2.moments(contour)
        print(type(mm))

        cx = mm['m10']/(mm['m00']+1)
        cy = mm['m01']/(mm['m00']+1)
        cv2.circle(image,( np.int(cx), np.int(cy)), 3, (0, 255, 255), -1)
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
        # print(contour)

    cv2.imshow("measured_object", image)


image = cv2.imread("D:/tello_video/test.png")
cv2.imshow("image", image)
measure_object(image)
c = cv2.waitKey(0)
if c == 27:
    cv2.destroyAllWindows()
