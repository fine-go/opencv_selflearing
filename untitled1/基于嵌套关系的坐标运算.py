'''
基于嵌套关系对二维码进行提取
'''

import cv2


def con (image):
    dst1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #img_gb = cv2.GaussianBlur(dst1, (5, 5), 0)
    #cv2.imshow("img_gb", img_gb)
    edges = cv2.Canny(dst1, 100, 200)
    cv2.imshow("edges", edges)
    des, contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.imshow("des", des)
    #image_out = cv2.drawContours(image, contours, 5, (0, 255, 0), 1)
    #cv2.imshow("image_out", image_out)
    print(len(contours))
    hierarchy = hierarchy[0]
    found = []
    for i in range(len(contours)):
        k = i
        c=0
        m = 0
        while(hierarchy[k][2]) != -1:
            k = hierarchy[k][2]
            c = c +1
            #print(c)
            if c >= 5:
                found.append(i)
            #print(c)
                print(i)
            if c < 5:
                m = m +1
                if m == len(contours):
                    print("this is 03")
                    #print(c)

    for i in found:
        #print(i)
        img_dc = image.copy()
        image_out0 = cv2.drawContours(img_dc, contours, i, (0, 255, 0), 2)
        cv2.imshow("image_out0", image_out0)
        print(contours[i])
        #if contours[i] != NULL:

        rect = cv2.minAreaRect(contours[i])
        angle = rect[2]
            #if angle > -85:
        print(angle)
    #print(found)
        #else:
            #print("this is 03 image")



if __name__ == '__main__':
    image0 = cv2.imread("image_qrcode01.png")
    #cv2.imshow("image", image0)
    image1 =cv2.imread("image_qrcode02.png")
    image2 = cv2.imread("image_qrcode03.png")
    image3 = cv2.imread("image_qrcode04.png")

    #cv2.imshow("image2", image1)
    con(image0)
    c = cv2.waitKey()
    if c == 27:
        #cv2.destroyAllWindows()
        con(image1)
        #cv2.destroyAllWindows()
    c = cv2.waitKey()
    if c == 27:
        con(image2)
        #cv2.destroyAllWindows()
    c = cv2.waitKey()
    if c == 27:
        con(image3)
        #cv2.destroyAllWindows()
    c = cv2.waitKey()

    if c == 27:
        cv2.destroyAllWindows()