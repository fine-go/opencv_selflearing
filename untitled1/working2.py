import  cv2
import numpy as np
from matplotlib import  pyplot as plt

def harris(image):
    dst1 = cv2.GaussianBlur(image, (5, 5), 0)
    gray = cv2.cvtColor(dst1, cv2.COLOR_BGR2GRAY)

    cv2.imshow("gray", gray)
    ret, binary = cv2.threshold(gray, 0,255,  cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    cv2.imshow("binary", binary)

    kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (23, 23))
    erode = cv2.erode(binary, kernel=kernel1)
    cv2.imshow("erode", erode)

    kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    dilate = cv2.dilate(erode, kernel=kernel2)
    cv2.imshow("dilate", dilate)

    corners = cv2.goodFeaturesToTrack(dilate,4,0.1,135)
    corners = np.int0(corners)
    print(corners)
    for i in corners:
        x,y = i.ravel()
        cv2.circle(image,(x,y),3,255,-1)
    cv2.imshow("image", image)



    '''dilate1 = np.float32(dilate)
    img = cv2.cornerHarris(dilate1, 2, 23, 0.04)

    image[dst > 0.01 * dst.max()] = [0, 0 , 255]
    while True:
        cv2.imshow('Corner', image)
        if cv2.waitKey() & 0xff == ord('q'):
            break  '''


    '''dilate = np.float32(dilate)    #将gray转化为float32的输入图像 blocksize=2，ksize=3
    dst = cv2.cornerHarris(dilate,2,3,0.04)

     #result is dilated for marking the corners, not important
    dst = cv2.dilate(dst,None)

    # Threshold for an optimal value, it may vary depending on the image
    #将img图像中检测到的角点涂上红色
    image[dst>0.01*dst.max()]=[0,0,255]

    cv2.imshow('cornerHarris',image) '''





    pts1 = np.float32(corners)
    pts2 = np.float32([[0,330 ], [0, 0], [550, 330], [550, 0]])
    M = cv2.getPerspectiveTransform(pts1, pts2)

    # 进行透视变换

    img = cv2.warpPerspective(image, M, (550, 330))
    cv2.imshow("img", img)
    return img



capture = cv2.VideoCapture(0)
while(True):
    ret, frame = capture.read()
    frame = cv2.flip(frame, 1)
    img1 = harris(frame)
    img2 = harris(frame)
    img3 = harris(frame)
    img4 = harris(frame)
    cv2.imshow("img1",img1)
    cv2.imshow("img1",img1)
    cv2.imshow("img1",img1)
    cv2.imshow("img1",img1)

    harris(frame)
    if cv2.waitKey(10)==27:
        break

capture.release()
#cv2.destroyAllWindows()
