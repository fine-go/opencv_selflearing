import  cv2
import numpy as np


def charm(pv):
    if pv > 255:
        return 255
    if pv<0:
        return 0
    else:
        return pv

def gaussian_noise(image):
    h, w, c = image.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0, 20, 3)#0是所有随机数的平均值， 20是标准差，3是形状（一行三列）
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            image[row, col, 0] = charm(b + s[0])
            image[row, col, 1] = charm(g + s[1])
            image[row, col, 2] = charm(r + s[2]) #产生高斯噪声
    cv2.imshow("noise_image", image)
    dst = cv2.GaussianBlur(image,(3, 3), 0)
    cv2.imshow("gaussian_noise_blur", dst)


image = cv2.imread("C:/Users/yangchao/Desktop/OpenCV/picture/1.jpg")
cv2.imshow("image", image)

t1 = cv2.getTickCount()
gaussian_noise(image)
t2 = cv2.getTickCount()
time = (t2 - t1)/cv2.getTickFrequency()
print("time :%s" %( time*1000))

dst = cv2.GaussianBlur(image,(0, 0), 15)
cv2.imshow("gaussian_blur", dst)

c = cv2.waitKey(0)
if c == 27:
    cv2.destroyAllWindows()