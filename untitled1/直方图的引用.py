import  cv2
import numpy as np
from matplotlib import  pyplot as plt

#直方图均衡化基于灰度图对比度增强
def equalHist(image):
    gary = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    dst = cv2.equalizeHist(gary)
    cv2.imshow("equel_demo", dst)
    print(dst)

    #cv.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
''' images：它是uint8类型或float32的源图像。它应该用方括号括起来，也就是”[img]”。
    channels：它也用方括号括起来。它是我们计算直方图的信道的索引。例如，如果输入是灰度图像，它的值是0。对于颜色图像，您可以通过0、1或2来分别计算蓝色、绿色或红色通道的直方图。
    mask：遮罩图。为了找到完整图像的直方图，它被指定为“None”。但如果你想找到图像的特定区域的直方图，你必须为它创建一个遮罩图，并将其作为遮罩。
    histSize：这代表了我们的BINS数。需要用方括号来表示。在整个范围内，我们通过了256。
    ranges：强度值范围，通常是 [ 0，256 ]'''


def mask_demo(image):#带遮罩的直方图均化
    gary = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    mask = np.zeros(image.shape[:2], np.uint8)
    mask[100:300, 100:300] = 255
    masked_image = cv2.bitwise_and(gary, gary, mask = mask)
    cv2.imshow("masked_gary", masked_image)

    hist_mask = cv2.calcHist([gary], [0], mask, [256], [0, 256])
    #均值化处理
    cdf = hist_mask.cumsum()
    cdf = (cdf-cdf[0])*255/(cdf[-1]-1)
    cdf = cdf.astype(np.uint8)

    #均值化之后生成img
    image_2 = np.zeros((500, 500, 1), np.uint8)
    image_2 = cdf[image]

    print(image2)
    cv2.imshow("after", image2)
    plt.show()
    cv2.waitKey(0)

def clare(gary):#自适应直方图均衡
#    gary = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    clare = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    cl1 = clare.apply(gary)
    cv2.imshow("clare", cl1)


def create_rgb_hist(image):
    h, w, s = image.shape
    rgbHist = np.zeros([16*16*16, 1],np.float32)
    bsize = 256/16
    for row in range(h):
        for col in range(w):
            b = image[row, col, 0]
            g = image[row, col ,1]
            r = image[row, col, 2]
            index = np.int(b/bsize)*16*16 + np.int(g/bsize)*16 + np.int(r/bsize)
            rgbHist[np.int(index), 0] += 1
    return rgbHist

def hist_compare(image_1, image_2):
    hist1 = create_rgb_hist(image_1)
    hist2 = create_rgb_hist(image_2)
    match1 = cv2.compare(hist1, hist2, cv2.HISTCMP_BHATTACHARYYA)#越小越相似
    match2 = cv2.compare(hist1, hist2, cv2.HISTCMP_CORREL)#越大越相似
    match3 = cv2.compare(hist1, hist2, cv2.HISTCMP_CHISQR)#越小越相似
    print("巴氏距离： %s， 相关性： %s， 卡方： %s"%(match1, match2, match3))

image1 = cv2.imread("C:/Users/yangchao/Desktop/OpenCV/picture/1.jpg")
image2 = cv2.imread("C:/Users/yangchao/Desktop/OpenCV/picture/2.jpg")
cv2.imshow("image1", image1)
cv2.imshow("image2", image2)
hist_compare(image1, image2)
c = cv2.waitKey(0)
if c == 27:
    cv2.destroyAllWindows()
