import  cv2
import numpy as np
from matplotlib import  pyplot as plt

#可以跟踪目标hsv色彩空间

def create_mask(image):
    mask = image[175:190, 175:195]
    cv2.imshow("mask", mask)
    cv2.imwrite("C:/Users/yangchao/Desktop/OpenCV/picture/mask.jpg", mask)


def hist2d_demo(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist(image, [0, 1], None, [180, 256], [0, 180, 0, 256])
    # cv2.imshow("hist2d", hist)
    plt.imshow(hist, interpolation="nearest")
    plt.title("hist2d")
    plt.show()

def roi_hist():
    sample = cv2.imread("C:/Users/yangchao/Desktop/OpenCV/picture/mask.jpg")
    target = cv2.imread("C:/Users/yangchao/Desktop/OpenCV/picture/1.jpg")

    cv2.imshow("sample", sample)
    cv2.imshow("target", target)

    roi_hsv = cv2.cvtColor(sample, cv2.COLOR_BGR2HSV)
    target_hsv = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)

    roiHist = cv2.calcHist([roi_hsv], [0, 1], None, [180, 256], [0,180, 0, 256])
    cv2.normalize(roiHist, roiHist, 0, 256, cv2.NORM_MINMAX)
    dst = cv2.calcBackProject([target_hsv], [0, 1], roiHist, [0, 180,0, 256], 1)
    cv2.imshow("roi_hist", dst)





#image = cv2.imread("C:/Users/yangchao/Desktop/OpenCV/picture/1.jpg")
#src = cv2.imread("C:/Users/yangchao/Desktop/OpenCV/picture/mask.jpg")
#cv2.imshow("image", image)
#cv2.imshow("mask", src)
roi_hist()
c = cv2.waitKey(0)
if c == 27:
    cv2.destroyAllWindows()
