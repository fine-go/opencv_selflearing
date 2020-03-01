import cv2
import random
import numpy as np

def creat(image1, image2):
    #image =
    x1, y1, ch1 = image1.shape
    print(image1.shape)
    print(image2.shape)
    print(image1.dtype)
    print(image2.dtype)
    for ch1 in range(ch1):
        for row1 in range(x1):
            for low1 in range(y1):
                mat1 = image1[row1, low1, ch1] & 248
                mat2 = image1[row1, low1, ch1] & 224
                mat2 = mat2>>5
                #print(mat1)
                #print(mat2)
                image1[row1, low1, ch1] = mat1 | mat2
                #print(image1[row1, low1, ch1])

        cv2.imshow("image1", image1)


def changed(image):
    x, y, ch= image.shape
    #交换行
    j = [i for i in range(x)]
    r = random.sample(range(x), x)

    if len(j)<=len(r):
        image[j, :, :] = image[r, :, :]
    #交换列
    j = [i for i in range(y)]
    r = random.sample(range(y), y)
    if len(j)<=len(r):
        image[:, j, :] = image[:, r, :]
    return image


if __name__ == '__main__':
    image1 = cv2.imread("C:/Users/yangchao/Desktop/OpenCV/picture/hhh/667.jpg")
    image2 = cv2.imread("C:/Users/yangchao/Desktop/OpenCV/picture/hhh/666.jpg")
    cv2.imshow("image2", image2)
    #creat(image1, image2)
    i = 0
    while(i<5):
        image = changed(image2)

        if i == 4:
            cv2.imshow("image", image)
        i+=1
    c = cv2.waitKey()
    if c== 27:
        cv2.destroyAllWindows()