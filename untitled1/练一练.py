import  cv2
import numpy as np
from matplotlib import  pyplot as plt
import os
from PIL import Image


index = 0
changed_image_img_open = 0

def find_juxing(image):
    dst = cv2.GaussianBlur(image, (5,5),0, 0)
    cv2.imshow("gaussian", dst)

    gary = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gary, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    cv2.imshow("binary", binary)

    kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
    img_edge1 = cv2.morphologyEx(binary, cv2.MARKER_CROSS, kernel1)
    cv2.imshow("img_edge1", img_edge1)

    kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (10,11))
    img_edge2 = cv2.morphologyEx(img_edge1, cv2.MORPH_OPEN, kernel2)
    cv2.imshow("img_edge2", img_edge2)

    img_edge = cv2.Canny(img_edge2, 0, 255)
    cv2.imshow("img_edge", img_edge)

    contours, hierarchy = cv2.findContours(img_edge2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE )
    print(contours)
    Min_Area = 100#除去小矩形
    contours = [cnt for cnt in contours if cv2.contourArea(cnt) > Min_Area]

    #print('len(contours)', len(contours))

    image_contours = []

    for cnt in contours:

        rect = cv2.minAreaRect(cnt)

        area_width, area_height = rect[1]

        if area_width < area_height:

            area_width, area_height = area_height, area_width

        wh_ratio = area_width / area_height

        print("wh_ratio", wh_ratio)

#要求矩形区域长宽比在2到5.5之间，2到5.5是长宽比，其余的矩形排除

        if wh_ratio > 1.5 and wh_ratio < 1.7:

            image_contours.append(rect)

            box = cv2.boxPoints(rect)
            box = np.int0(box)

            oldimg = cv2.drawContours(image, [box], 0, (0, 255, 255), 2)

            cv2.imshow("edge4", oldimg)

            print(rect)



    print(len(image_contours))
    print(len(image_contours[0]))
    c = len(image_contours)
    print(image_contours[0])

    if c == 1:

        global index
        index = index +1


        rect = cv2.minAreaRect(contours)
        box = cv2.boxPoints(rect)
        box = np.int0(box)

        pts=np.float32([[0,0],[300,0],[0,300],[300,300]])#输出图像的分辨率
        M=cv2.getPerspectiveTransform(box,pts)

        changed_image=cv2.warpPerspective(image,M,(300,300))
        cv2.imshow("changed_image", changed_image)

        changed_image_gaussian = cv2.GaussianBlur(changed_image,(3,3))
        changed_image_gary = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
        ret, changed_image_binary = cv2.threshold(changed_image_gary, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
        cv2.imshow("changed_image_binary", changed_image_binary)

        global changed_image_img_open

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        changed_image_img_cross = cv2.morphologyEx(changed_image_binary, cv2.MARKER_CROSS, kernel1)
        cv2.imshow("img_edge1", changed_image_img_cross)

        changed_image_img_open = cv2.morphologyEx(img_edge1, cv2.MORPH_OPEN, kernel2)
        cv2.imshow("changed_image_img_open", changed_image_img_open)

    return  changed_image_img_open

    if c != 1:
        index = inedx

def cun(img):
    global index
    target_path="C:/Users/yangchao/Desktop/OpenCV/picture./change_size/0/"
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    cv2.imwrite(target_path+str(index)+".jpg",img)
    index = index+1
    return index

def shibie(a):
    target_path="C:/Users/yangchao/Desktop/OpenCV/picture./change_size/0/"
    if a == 4:
        img1 = cv2.imread(target_path+1+".jpg")
        img2 = cv2.imread(target_path+2+".jpg")
        img3 = cv2.imread(target_path+3+".jpg")
        img4 = cv2.imread(target_path+4+".jpg")
        img_1 = cv2.add(img1, img2)
        img_2 = cv2.add(img3, img4)
        img = cv2.add(img_1, img_2)
        textimage = Image.fromarray(img)
    #text = tess.image_to_string(textimage, lang='eng' config='--psm 6 --ome 3 -c tessedit_char_whitelist=0123456789').strip()
        text = tess.image_to_string(img, lang='eng', config='--psm 6 --ome -c tessedit_char_whitelist=012346789').strip()
        print("识别结果: %s"%text)
    index = 0
    return index

capture = cv2.VideoCapture(0)

while (True):
    ret, frame = capture.read()

    img = find_juxing(frame)

    a = cun(img)

    index = shibie(a)

    if (cv2.waitKey(10)==27):
        break







