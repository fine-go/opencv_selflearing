import  cv2
import numpy as np
from matplotlib import  pyplot as plt


def create_mask(image):
    mask = image[100:300, 100: 300]
    cv2.imshow("mask", mask)
    cv2.imwrite("C:/Users/yangchao/Desktop/OpenCV/picture/template.png", mask)

def template_demo():
    target = cv2.imread("C:/Users/yangchao/Desktop/OpenCV/picture/1.jpg")
    tql = cv2.imread("C:/Users/yangchao/Desktop/OpenCV/picture/template.png")
    cv2.imshow("tql", tql)
    cv2.imshow("target", target)
    methods = [cv2.TM_SQDIFF_NORMED, cv2.TM_CCORR_NORMED, cv2.TM_CCOEFF_NORMED]
    th, tw = tql.shape[:2]
    for md in methods:
        print(md)
        result = cv2.matchTemplate(target, tql, md)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if md == cv2.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        br = (tl[0]+tw, tl[1]+th)
        cv2.rectangle(target, tl, br, (0, 0, 255), 2)
        cv2.imshow("match"+np.str(md), target)
        cv2.imshow("resure"+np.str(md), result)

image = cv2.imread("C:/Users/yangchao/Desktop/OpenCV/picture/1.jpg")
#cv2.imshow("image", image)

template_demo()

c = cv2.waitKey(0)
if c == 27:
    cv2.destroyAllWindows()
