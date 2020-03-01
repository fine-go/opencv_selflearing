import  cv2
import numpy as np
from matplotlib import  pyplot as plt


def water_demo(image):
    dst = cv2.GaussianBlur(image, (3, 3), 0)
    gary = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gary, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cv2.imshow("binary", binary)

    #形态学操作
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    mb = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=2)
    sure_bg = cv2.dilate(mb, kernel, iterations=3)
    cv2.imshow("sure_bg", sure_bg)

    #距离变换
    dist = cv2.distanceTransform(sure_bg, cv2.DIST_L2,3)
    dist_output = cv2.normalize(dist, 0, 1.0, cv2.NORM_MINMAX)
    cv2.imshow("dist_output", dist_output)

    ret, surface =cv2.threshold(dist_output, dist.max()*0.6, 255, cv2.THRESH_BINARY)
    cv2.imshow("surface", surface)

    surface_fg = np.uint8(surface)
    unknown = cv2.subtract(sure_bg, surface_fg)
    ret, markers = cv2.connectedComponents(surface_fg)
    print(ret)

    #分水岭变换
    markers = markers+1
    markers[unknown==255] = 0
    markers = cv2.watershed(image, markers=markers)
    image[markers == -1] = [0, 0, 255]
    cv2.imshow("result", image)


image = cv2.imread("0.png")
cv2.imshow("image", image)
water_demo(image)
c = cv2.waitKey(0)
if c == 27:
    cv2.destroyAllWindows()
