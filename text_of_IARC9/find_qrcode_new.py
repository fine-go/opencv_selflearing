import numpy as np
import cv2
import pyzbar.pyzbar as pyzbar
import time

def lateral_connect(image_1, image_2):
    image_1_mask = image_1[0:200,185:200]
    area = 3000
    #cv2.imshow("image_1_mask", image_1_mask)
    for index in range(0, 100, 5):
        #print(index)
        image_2_mask = image_2[:, index:index + 15]
        #cv2.imshow("image_2_mask", image_2_mask)
        image = cv2.subtract(image_1_mask, image_2_mask)
        #cv2.imshow("image", image)
        img, image_contours, he_image = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        m = 0
        #cv2.drawContours(image, image_contours, -1, (0, 255, 0), 1)
        #cv2.imshow("image_contours", image)
        #cv2.waitKey(0)
        for ct in image_contours:
            m_image = cv2.contourArea(ct)
            m = m + m_image
        #print(m)
        if m < (area - (0.95 * area)):
            #print(index + 30)
            pass
        break
    array = np.array((np.arange(index+15).reshape(index+15, 1)))
    #print(array)
    image_2 = np.delete(image_2, array, axis=1)
    #cv2.imshow("fiiiiisdhvcjsgdcia", image_2)
    image = np.hstack((image_1, image_2))
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    return image

def lengthways_connect(image_1, image_2):
    image_1_mask = image_1[0:15,:]
    area =  15*200
    #cv2.imshow("image_1_mask", image_1_mask)
    for index in range(0, 100, 5):
        #print(index)
        image_2_mask = image_2[index:index + 15, :]
        #cv2.imshow("image_2_mask", image_2_mask)
        image = cv2.subtract(image_1_mask, image_2_mask)
        #cv2.imshow("image", image)
        img, image_contours, he_image = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        m = 0
       #cv2.drawContours(image, image_contours, -1, (0, 255, 0), 1)
        #cv2.imshow("image_contours", image)
        #cv2.waitKey(0)
        for ct in image_contours:
            m_image = cv2.contourArea(ct)
            m = m + m_image
        #print(m)
        if m < (area - (0.95 * area)):
            #print(index + 30)
            pass
        break
    array = np.array((np.arange(index+15).reshape(1, index+15)))
    #print(array)
    image_2 = np.delete(image_2, array, axis=0)
    #cv2.imshow("fiiiiisdhvcjsgdcia", image_2)
    image = np.vstack((image_1, image_2))
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    return image

def first_position(file):
    for index in range(1,5, 1):
        print("第%d张图片"% index)
        print(file+str(index)+".jpg")
        image = cv2.imread(file+str(index)+".jpg")
        image = cv2.pyrDown(image, 8)
        #image = cv2.GaussianBlur(image, (3, 3), 0)
        cv2.imshow("image", image)
        gary = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        cv2.imshow("gary", gary)
        ret, binary = cv2.threshold(gary,150, 255, cv2.THRESH_BINARY_INV)
        #binary = cv2.adaptiveThreshold(gary, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 35, 10)

        cv2.imshow("binary", binary)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
        dilation = cv2.dilate(binary, kernel, iterations=1)  # 膨胀处理
        cv2.imshow("dilation", dilation)
        erosion = cv2.erode(dilation, kernel, iterations=1)
        cv2.imshow("erosion", erosion)

        canny = cv2.Canny(erosion,110, 200)
        cv2.imshow("canny", canny)

        img,contours,he = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area_min = 12000
            area_max = 20000
            m = cv2.contourArea(cnt)
            print("M = %d"% m)
            cv2.drawContours(image, cnt, 0, (0, 0, 255), 3)
            cv2.imshow("image", image)
            if m >area_min and m < area_max:

                rect = cv2.minAreaRect(cnt)

                w = rect[1][0]
                h = rect[1][1]
                print("w = %d"% w)
                print("h= %d"% h)
                #print(0)
                if w/h >0.7 and w/h <0.8:
                    box = cv2.boxPoints(rect)
                    box = np.int0(box)
                    cv2.drawContours(image, [box],0,(255, 0, 255), 1)
                    cv2.imshow("image", image)
                    print(box)


                    box = box.astype("float32")
                    dst_rect = np.array([[h, w],
                                        [0, w],
                                        [0, 0],
                                        [h, 0]],
                                        dtype=np.float32)
                    #print(dst_rect)
                    M = cv2.getPerspectiveTransform(box, dst_rect)


                    w = int(w)
                    h = int(h)

                    warped = cv2.warpPerspective(gary, M, (h, w))
                    cv2.imshow("warped",warped)
                    warped_ = cv2.resize(warped, (200, 150), cv2.cv2.INTER_CUBIC)
                    #img = np.ones((170, 220), dtype=np.uint8)
                    #img = cv2.bitwise_not(img)
                    #img[10:160,10:210] = warped_
                    #cv2.imshow("img", img)
                    M2 = cv2.getRotationMatrix2D((10, 210), -4, 1.0)
                    warped_a = cv2.warpAffine(warped_, M2, (230, 190), cv2.INTER_CUBIC, cv2.BORDER_REPLICATE)
                    cv2.imshow("warp_a",warped_a)
                    cv2.imwrite(file + "warped_" + str(index) + ".jpg", warped_a)


        cv2.waitKey(0)
        cv2.destroyAllWindows()

def second_position_location(file):
    for index in range(1, 5, 1):
        image = cv2.imread(file + "warped_" + str(index) + ".jpg")
        cv2.imshow("image", image)
        image_gary = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, binary = cv2.threshold(image_gary, 222, 255, cv2.THRESH_BINARY)
        #binary = cv2.adaptiveThreshold(image_gary, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 35, 10)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
        kernel_1 = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
        cv2.imshow("th", binary)
        dilation = cv2.dilate(binary, kernel, iterations=1)  # 膨胀处理
        cv2.imshow("dilation" + str(index), dilation)
        erosion = cv2.erode(dilation, kernel_1, iterations=1)
        cv2.imshow("ercode" + str(index), erosion)
        img, contours, he = cv2.findContours(erosion, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        for cnt in contours:
            m = cv2.contourArea(cnt)
            print(m)
            if m >13000 and m < 18000:
                rect = cv2.minAreaRect(cnt)
                w = rect[1][0]
                h = rect[1][1]
                box = cv2.boxPoints(rect)
                box = np.int0(box)

                cv2.drawContours(image, [box], 0, (0, 255, 255), 1)
                cv2.imshow("find", image)
                cv2.waitKey(0)
                print(box)
                box = box.astype("float32")
                dst_rect = np.array([[h, w],
                                     [0, w],
                                     [0, 0],
                                     [h, 0]],
                                    dtype=np.float32)
                print(dst_rect)
                M = cv2.getPerspectiveTransform(box, dst_rect)

                w = int(w)
                h = int(h)

                warped = cv2.warpPerspective(image, M, (h, w))
                cv2.imshow("warped", warped)
                warped_ = cv2.resize(warped, (200, 200), cv2.cv2.INTER_CUBIC)
                M2 = cv2.getRotationMatrix2D((0, 200), -4, 1.0)
                warped_a = cv2.warpAffine(warped_, M2, (300, 300), cv2.INTER_CUBIC, cv2.BORDER_REPLICATE)
                cv2.imshow("warped_a", warped_a)
                cv2.imwrite(file + "location" + str(index) + ".jpg", warped_a)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def third_position(file):
    for index in range(1, 5, 1):
        #print("第%d张图"% index)
        warped_imread = cv2.imread(file + "location" + str(index) + ".jpg", cv2.IMREAD_GRAYSCALE)
        #cv2.imshow("image", warped_imread)
        # warp_binary = cv2.adaptiveThreshold(warped_med, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
        ret, warp_binary = cv2.threshold(warped_imread, 220, 255, cv2.THRESH_BINARY_INV)
        #cv2.imshow("warp_binary", warp_binary)
        warped_Canny = cv2.Canny(warp_binary, 50, 100)
        #cv2.imshow("warped_Canny", warped_Canny)
        #cv2.waitKey(0)
        o, warped_contours, he = cv2.findContours(warped_Canny, cv2.RETR_TREE, cv2.cv2.CHAIN_APPROX_NONE)
        #print(type(he))
        #cv2.drawContours(warped_imread, warped_contours, -1, (0, 255, 255), 1)
        #cv2.imshow("warped_imread_Contours", warped_imread)

        #print(len(he[0]))
        #print(he)
        flag = None
        for j in range(len(he[0]) - 5):
            # print("j is%s"% j)
            # print("he[0][j][2] %d"% he[0][j][2])
            if he[0][j][2] == he[0][j + 1][2] - 1:
                if he[0][j + 1][2] == he[0][j + 2][2] - 1:
                    if he[0][j+2][2] == he[0][j+3][2]-1:
                        if he[0][j+3][2] == he[0][j+4][2]-1:
                            #print("find it")
                            #print("it is %d" % (j + 5))
                            #print("he[0][j][2] %d" % he[0][j][2])
                            flag = j + 5
                            #print(warped_contours[j+5])
                            #cv2.drawContours(warped_imread, [warped_contours[j+5]], 0, (0, 255, 255), 1)
                            #cv2.imshow("wa", warped_imread)

        #print("flag%s" % flag)
        if flag is not None:
            warp_rect = cv2.minAreaRect(warped_contours[flag])
            #print(warp_rect[0])
            warp_box = cv2.boxPoints(warp_rect)
            warp_box = np.int0(warp_box)
            warped_x = warp_rect[0][0]
            warped_y = warp_rect[0][1]
            #print("warp_x %d" % warped_x)
            #print("warp_y %d" % warped_y)
            #cv2.waitKey(0)
            if warped_x - 100 > 0:
                cv2.imwrite(file + "new/2.jpg", warped_imread)
                #print("写入 ：%s"% file + "new/2.jpg")
            else:
                if warped_y - 100 > 0:
                    cv2.imwrite(file + "new/3.jpg", warped_imread)
                    #print("写入 ：%s"% file + "new/3.jpg")
                else:
                    cv2.imwrite(file + "new/1.jpg", warped_imread)
                   # print("写入 ：%s" % file + "new/1.jpg")
        else:
            cv2.imwrite(file + "new/4.jpg", warped_imread)
            #print("写入 ：%s"% file + "new/4.jpg")
        #cv2.waitKey(0)

    #cv2.destroyAllWindows()

def final_position(file):
    count = [[], [], [], []]
    base = np.zeros((380, 380),np.uint8)
    for index in range(1, 5, 1):
        image = cv2.imread(file+"new/"+str(index)+".jpg")
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
       # cv2.imshow("image",image)
        M2 = cv2.getRotationMatrix2D((0, 200), 4, 1.0)
        warped_a_ed = cv2.warpAffine(image, M2, (300, 300), cv2.INTER_CUBIC, cv2.BORDER_REPLICATE)
        #cv2.imshow("warp_a_ed", warped_a_ed)
        count[index-1] = warped_a_ed[0:200, 0:200]
       # cv2.imshow("count[index-1]",count[index-1])
        cv2.imwrite(file+"new/_"+str(index)+".jpg", count[index-1])
        #cv2.waitKey(0)
        # cv2.destroyAllWindows()

    image_x_1 = lateral_connect(count[0],count[1])
    #cv2.imshow("image_x",image_x_1)
    image_x_2 = lateral_connect(count[2],count[3])
    #cv2.imshow("image_x", image_x_2)
    image = lengthways_connect(image_x_1, image_x_2)
    ret, base = cv2.threshold(image, 220, 255, cv2.THRESH_BINARY)
   # cv2.imshow("base", base)
   # cv2.waitKey(0)
  #  cv2.destroyAllWindows()
    return base

def decode_Display(image):

    barcodes = pyzbar.decode(image)

    #print(barcodes)
    for barcode in barcodes:
        # 提取条形码的边界框的位置
        # 画出图像中条形码的边界框
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        # 条形码数据为字节对象，所以如果我们想在输出图像上
        # 画出来，就需要先将它转换成字符串
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        # 绘出图像上条形码的数据和条形码类型
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    .5, (0, 0, 125), 2)
        # 向终端打印条形码数据和条形码类
        print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
    return image
# 200,200 gary

one = time.time()
if __name__ == '__main__':
    file = "picture_8/"
    # 初步提取 保存 warped
    first_position(file)
    # 得到二维码 保存 new location 旋转角度4
    second_position_location(file)
    # 排序
    third_position(file)
    # 拼接
    base = final_position(file)
    #cv2.imshow("base", base)
    #扫码
    decode_Display(base)
    two = time.time()
    print("cost time %s"%(two-one))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
