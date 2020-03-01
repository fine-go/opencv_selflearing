import cv2
import numpy as np

img = cv2.imread("qrcode.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# find Harris corners
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)
dst = cv2.dilate(dst,None)
ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
dst = np.uint8(dst)
# find centroids
#connectedComponentsWithStats(InputArray image, OutputArray labels, OutputArray stats,
#OutputArray centroids, int connectivity=8, int ltype=CV_32S)
ret1, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
# define the criteria to stop and refine the corners
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
#Python: cv2.cornerSubPix(image, corners, winSize, zeroZone, criteria)
#zeroZone – Half of the size of the dead region in the middle of the search zone
#over which the summation in the formula below is not done. It is used sometimes
# to avoid possible singularities of the autocorrelation matrix. The value of (-1,-1)
# indicates that there is no such a size.
# 返回值由角点坐标组成的一个数组（而非图像）
corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)
m  =np.zeros((len(corners), 1, 2))
for i in range(len(corners)):
    m[i, 0, 0] = corners[i, 0]
    m[i, 0, 1] = corners[i, 1]
print(m.shape)
print(corners.shape)
# print(corners)
m = np.trace(m)
print(m)
res = np.hstack((centroids,corners))
#np.int0 可以用来省略小数点后面的数字（非四􃮼五入）。
res = np.trunc(res)
print(res)
print(res.shape)
ctr = np.array(m).reshape((-1,1,2)).astype(np.int32)
print(m)
cv2.drawContours(img, m, -1, (0,255,0), 3)
cv2.imshow("img",img)
cv2.imwrite('subpixel5.png',img)
c = cv2.waitKey()
if c == 27:
    cv2.destroyAllWindows()
