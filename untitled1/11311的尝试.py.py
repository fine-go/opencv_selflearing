import numpy as np
import cv2
from matplotlib import pyplot as plt

'''def location(image):

    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #ksize :表示卷积核的大小
    #dst1 = cv2.blur(image,(5, 5))
    #cv2.imshow("blur_demo",dst1)
    dst2 = cv2.medianBlur(image, 5)
    cv2.imshow("median_demo",dst2)
    dst3 = cv2.GaussianBlur(dst2,(3, 3), 0)
    cv2.imshow("gaussian_noise_blur", dst3)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray,235,255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    dst = cv2.erode(binary, kernel=kernel)

    cv2.imshow("dst", dst)'''

def goodpoint(img):
    kernel = np.array([[0, -1, 0],[-1, 7, -1],[0, -1, 0]], np.float32)
    dst = cv2.filter2D(img,-1, kernel=kernel)
    gray = cv2.cvtColor(dst,cv2.COLOR_BGR2GRAY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    ret, binary = cv2.threshold(gray,220,255, cv2.THRESH_BINARY)
    dst = cv2.dilate(binary, kernel=kernel)
    cv2.imshow("dst1", dst)
    l, contours1, hst1 = cv2.findContours(gray, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.imshow("i",l)
    corners = cv2.goodFeaturesToTrack(l,400,0.5,5)
    # 返回的结果是 [[ 311., 250.]] 两层括号的数组。
    corners = np.int0(corners)
    for i in corners:
        x,y = i.ravel()
        img = cv2.circle(img,(x,y),3,255,-1)
    cv2.imshow("img", img)

def stft(img1, img2):

    gray1= cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    sift1 = cv2.xfeatures2d.SIFT_create()
    kp1 = sift1.detect(gray1,None)
    print(kp1)
    #im12 = img1.copy
    img1=cv2.drawKeypoints(gray1,kp1, outImage=np.array([]), color = (0, 0, 255))
    #cv2.imwrite('sift_keypoints.jpg',img)
    cv2.imshow("img", img1)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    sift2 = cv2.xfeatures2d.SIFT_create()
    kp2 = sift2.detect(gray2,None)
    print(kp2)
    #img2 = img2.copy
    img2=cv2.drawKeypoints(gray2,kp2, outImage=np.array([]), color = (0, 0, 255))
    #cv2.imwrite('sift_keypoints.jpg',img)
    cv2.imshow("img2", img2)
    #sift1 = np.int(sift1)
    #sift2 = np.int(sift2)

    kp1, des1 = sift1.detectAndCompute(img1,None)
    kp2, des2 = sift2.detectAndCompute(img2,None)

    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1,des2, k=2)
    # Apply ratio test
    # 比值测试，首先获取与 A 距离最近的点 B（最近）和 C（次近），只有当 B/C
    # 小于阈值时（0.75）才被认为是匹配，因为假设匹配是一一对应的，真正的匹配的理想距离为 0
    good = []
    for m,n in matches:
        if m.distance < 0.75*n.distance:
            good.append([m])
            # cv2.drawMatchesKnn expects list of lists as matches.
            # img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good[:10],flags=2)
            img4 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good[:10], outImg=None, flags=2)
    plt.imshow(img4),plt.show()


def surf(img):
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    sift = cv2.xfeatures2d.SURF_create()
    kp = sift.detect(gray,None)
    print(kp)
    img2 = img.copy
    img=cv2.drawKeypoints(gray,kp, outImage=np.array([]), color = (0, 0, 255))
    #cv2.imwrite('sift_keypoints.jpg',img)
    cv2.imshow("img", img)

def kvze(img):
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    kaze = cv2.KAZE_create()
    kp = kaze.detect(gray,None)
    print(kp)
    img2 = img.copy
    img=cv2.drawKeypoints(gray,kp, outImage=np.array([]), color = (0, 0, 255))
    #cv2.imwrite('sift_keypoints.jpg',img)
    cv2.imshow("img", img)

def harris(image):
    dst = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    dse = np.float32(dst)
    #blocksize表示窗口大小ksize表示所贝尔算子求导得到的矩阵m之后进行打分得到r自由参数k表示det（m) - k(trance(m))返回是一个打完分的灰度图像
    dst2 = cv2.cornerHarris(dse, 3,3, 0.04)
    cv2.imshow("dst2", dst2)
    dst2 = cv2.dilate(dst2,None)

    image[dst2>0.01*dst2.max()]=[0,255,255]
    cv2.imshow("imae2", image)
    #ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst2)
   # print(ret,labels,stats,centroids)

def no(image1, image2):
    image1_gary = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2_gary = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    cv2.imshow("image1_gary", image1_gary)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    ret1, binary1= cv2.threshold(image1_gary,220,255, cv2.THRESH_BINARY)
    dst1 = cv2.dilate(binary1, kernel=kernel)
    cv2.imshow("dst1", dst1)
    ret2, binary2 = cv2.threshold(image2_gary,220,255, cv2.THRESH_BINARY)
    dst2 = cv2.dilate(binary2, kernel=kernel)
    cv2.imshow("dst2", dst2)

    #ret, binary = cv2.threshold(image1_gary,127,255,cv2.THRESH_BINARY)
    l, contours1, hst1 = cv2.findContours(binary1, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    l, contours2, hst2 = cv2.findContours(binary2, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    img1 = cv2.drawContours(dst1,contours1,0,(0,0,255),1)
    cv2.imshow("image1_gary", img1)

    #contours2, hst2 = cv2.findContours(img1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #print(contours2)

    Min_Area = 800#除去小矩形
    Max_Area = 10000
    contours1 = [cnt for cnt in contours1 if cv2.contourArea(cnt) > Min_Area and cv2.contourArea(cnt)<Max_Area]
    image_contours = []
    for cnt in contours1:
        rect = cv2.minAreaRect(cnt)
        area_width, area_height = rect[1]
        if area_width < area_height:

            area_width, area_height = area_height, area_width

        wh_ratio = area_width / area_height

        #print("wh_ratio", wh_ratio)

        #要求矩形区域长宽比在2到5.5之间，2到5.5是长宽比，其余的矩形排除

        if wh_ratio > 0.99 and wh_ratio <=1.0:

            image_contours.append(rect)

            box = cv2.boxPoints(rect)
            box = np.int0(box)

            oldimg = cv2.drawContours(image1, [box], 0, (0, 255, 255), 2)

            cv2.imshow("edge4", oldimg)
        #print(rect)
       # print(rect[0])
        #print(cnt)
            #print(box)
        contours2 = [cnt for cnt in contours2 if cv2.contourArea(cnt) > Min_Area and cv2.contourArea(cnt)<Max_Area]
        image_contours = []
        for cnt in contours2:
            rect = cv2.minAreaRect(cnt)
            area_width, area_height = rect[1]
            if area_width < area_height:

                area_width, area_height = area_height, area_width

            wh_ratio = area_width / area_height

            #print("wh_ratio", wh_ratio)

            #要求矩形区域长宽比在2到5.5之间，2到5.5是长宽比，其余的矩形排除

            if wh_ratio > 0.99 and wh_ratio <=1.0:

                image_contours.append(rect)

                box = cv2.boxPoints(rect)
                box = np.int0(box)

                oldimg = cv2.drawContours(image2, [box], 0, (0, 255, 255), 2)

                cv2.imshow("edge5", oldimg)
            #print(rect)
            print(rect[0])
             #   print(cnt)
              #  print(box)


#def fast(img):


image1= cv2.imread("Try_1.jpg")
cv2.imshow("image1",image1)
image2= cv2.imread("image_qrcode02.png")
#cv2.imshow("image_qrcode02", image2)
print(image1.dtype)
print(image2.dtype)
print(image1.shape)
print(image2.shape)



no(image1, image2)
c = cv2.waitKey()
if c == 27:
    cv2.destroyAllWindows()
