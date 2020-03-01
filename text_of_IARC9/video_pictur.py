import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

def location(file):
    for index in range(1, 5, 1):
        image = cv2.imread(file + "1.bmp")
        #image = cv2.imread(file+str(index)+".jpg")
        cv2.imshow("image", image)
        M2 = cv2.getRotationMatrix2D((0, 720), -20, 1.0)
        image = cv2.warpAffine(image, M2, (1200, 1200), cv2.INTER_CUBIC, cv2.BORDER_REPLICATE)
        cv2.imshow("image", image)
        gary = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        ret, binary = cv2.threshold(gary, 50, 255, cv2.THRESH_BINARY_INV)

        cv2.imshow("binary", binary)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
        #pengzhang
        erosion = cv2.erode(binary, kernel, iterations=1)
        dilation = cv2.dilate(erosion, kernel, iterations=1)
        cv2.imshow("d", dilation)
        cv2.imshow("e", erosion)
        canny = cv2.Canny(erosion,50, 220)
        cv2.imshow("canny", canny)
        img, contours, he = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            rect = cv2.minAreaRect(cnt)
            w = rect[1][0]
            h = rect[1][1]
            area = w*h
            print("area = %d"% area)

            if area > 9000 and area < 12000 and w/h <1.1 and w/h> 0.9:

                box = cv2.boxPoints(rect)
                box = np.int0(box)

                #cv2.drawContours(image, [box], 0, (0, 255, 255), 1)
                cv2.imshow("find", image)
                #cv2.waitKey(0)
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

                warped = cv2.warpPerspective(image, M, (h-5, w-5))

                warped_ = cv2.resize(warped, (400, 400), cv2.INTER_CUBIC)
                warped_ = cv2.bitwise_not(warped_)
                cv2.imshow("warped", warped)
                print(warped_.shape)
                cv2.imwrite(file + "location" + str(index) + ".jpg", warped_)
            else:
                if h != 0:
                    print(w/h)
                elif w != 0:
                    print(h/ w)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def judge(file):
    for index in range(1, 5, 1):
        print("第%d张图"% index)
        image = cv2.imread(file + "location" + str(index) + ".jpg")
        cv2.imshow("iamge",image)
        image_roi = image[5:195, 5:195]
        image_roi = cv2.resize(image_roi, (200, 200), cv2.cv2.INTER_CUBIC)
        cv2.imshow("image", image_roi)
        gary = cv2.cvtColor(image_roi, cv2.COLOR_BGR2GRAY)
        #binary = cv2.adaptiveThreshold(gary, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 35, 10)
        ret, binary = cv2.threshold(gary, 120, 255, cv2.THRESH_BINARY)
        cv2.imshow("binary", binary)
        cv2.waitKey(0)
        canny = cv2.Canny(binary, 100, 200)
        o, warped_contours, he = cv2.findContours(canny, cv2.RETR_TREE, cv2.cv2.CHAIN_APPROX_NONE)
        # print(len(he[0]))
        print(he)
        flag = None
        for j in range(len(he[0]) - 5):
            # print("j is%s"% j)
            # print("he[0][j][2] %d"% he[0][j][2])
            if he[0][j][2] == he[0][j + 1][2] - 1:
                if he[0][j + 1][2] == he[0][j + 2][2] - 1:
                            # print("find it")
                            # print("it is %d" % (j + 5))
                            # print("he[0][j][2] %d" % he[0][j][2])
                            flag = j + 3
        if flag is not None:
            warp_rect = cv2.minAreaRect(warped_contours[flag])
            #print(warp_rect[0])
            warp_box = cv2.boxPoints(warp_rect)
            warp_box = np.int0(warp_box)
            warped_x = warp_rect[0][1]
            warped_y = warp_rect[0][0]
            print("warp_x %d" % warped_x)
            print("warp_y %d" % warped_y)
            #cv2.waitKey(0)
            if warped_x - 100 > 0:
                cv2.imwrite(file + "new/3.jpg", binary)
                print("写入 ：%s"% file + "new/3.jpg")
            else:
                if warped_y - 100 > 0:
                    cv2.imwrite(file + "new/2.jpg", binary)
                    print("写入 ：%s"% file + "new/2.jpg")
                else:
                    cv2.imwrite(file + "new/1.jpg", binary)
                    print("写入 ：%s" % file + "new/1.jpg")
        else:
            cv2.imwrite(file + "new/4.jpg", binary)
            print("写入 ：%s"% file + "new/4.jpg")
        #cv2.waitKey(0)
        cv2.waitKey(0)

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

def lateral_connect(image_1, image_2):
    index_ = 0
    for index_1 in range(0, 20 , 1):

        if index_ != 0:
            break
        print("index_1 = %d"%index_1)
        image_1_mask = image_1[0:200,190-index_1:200-index_1]
        cv2.imshow("image_1_mask",image_1_mask)
        area = 10*200
        cv2.imshow("imahge_2", image_2)
        cv2.imshow("image_1_mask", image_1_mask)
        for index in range(0, 50, 1):
            print("index %s"% index)
            image_2_mask = image_2[:, index:index + 10]
            cv2.imshow("image_2_mask", image_2_mask)
            image = cv2.subtract(image_1_mask, image_2_mask)
            cv2.imshow("image", image)
            base = np.zeros((300, 300), np.uint8)

            base[50:250,50:60] = image
            cv2.imshow("image", base)
            img, image_contours, he_image = cv2.findContours(base, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            m = 0
            #cv2.drawContours(image, image_contours, -1, (0, 255, 0), 1)
            #cv2.imshow("image_contours", image)
            #cv2.waitKey(0)

            for ct in image_contours:
                m_image = cv2.contourArea(ct)

                m = m + m_image
            m = area - m
            print("m % d " % m)
            if m> (0.6* area) and m<1.01*area:
                #print(index + 30)
                index_ = index+10
                break
            else:
                index_ = 0
        cv2.waitKey(0)

    array_1 = np.array((np.arange(200-index_1, 200).reshape(index_1, 1)))

    array = np.array((np.arange(index_).reshape(index_, 1)))
    #print(array)
    image_2 = np.delete(image_2, array, axis=1)
    image_1 = np.delete(image_1, array_1, axis=1)
    cv2.imshow("fiiiiisdhvcjsgdcia", image_2)
    image = np.hstack((image_1, image_2))
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    #image = cv2.bitwise_not(image)
    image = cv2.resize(image, (400, 200), cv2.cv2.INTER_CUBIC)
    return image

def lengthways_connect(image_1, image_2):
    index_ = 0
    for index_1 in range(0, 20, 1):
        if index_ != 0:
            break
        image_1_mask = image_1[190-index_1:200-index_1,:]
        print("index_1 = %d"%index_1)
        area =  4000
        cv2.imshow("image_1_mask", image_1_mask)
        for index in range(0, 100, 1):
            print("index_ = %d" % index_)
            image_2_mask = image_2[index:index + 10, :]
            cv2.imshow("image_2_mask", image_2_mask)
            image = cv2.subtract(image_1_mask, image_2_mask)
            cv2.imshow("bit", image)

            base = np.zeros((500, 500), np.uint8)

            base[50:60, 50:450] = image
            cv2.imshow("image---", base)
            img, image_contours, he_image = cv2.findContours(base, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            m = 0
            for ct in image_contours:
                m_image = cv2.contourArea(ct)
                m = m + m_image

            m = area - m
            print("mj = %d" % m)
            if m> (0.9 * area) and m<1.01*area:
                print(index + 10)
                index_ = index+10
                break
            else:
                index_ = 0
        #cv2.waitKey(0)
    array = np.array((np.arange(index_).reshape(1, index_)))
    #print(array)
    array_1 = np.array((np.arange(200-index_1,200).reshape(1, index_1)))
    image_2 = np.delete(image_2, array, axis=0)
    image_1 = np.delete(image_1, array_1, axis=0)
    cv2.imshow("fiiiiisdhvcjsgdcia", image_2)
    image = np.vstack((image_1, image_2))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return image

def final_position(file):
    count = [[], [], [], []]
    for index in range(1, 5, 1):
        image = cv2.imread(file+"new/"+str(index)+".jpg")
        count[index - 1] = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow("count[index-1]",count[index-1])
    image_x_1 = lateral_connect(count[0],count[1])
    cv2.imshow("image_x",image_x_1)
    cv2.waitKey(0)
    image_x_2 = lateral_connect(count[2],count[3])
    cv2.imshow("image_x", image_x_2)
    cv2.waitKey(0)
    image = lengthways_connect(image_x_1, image_x_2)
    ret, base = cv2.threshold(image, 220, 255, cv2.THRESH_BINARY)
    cv2.imshow("base", base)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return base


if __name__ == '__main__':
    file = "picture/"
    location(file)
    #judge(file)
    # 拼接
    #base = final_position(file)
    #cv2.imshow("base", base)
    # 扫码

    #image = decode_Display(base)
    #cv2.imshow("base", base)
    cv2.waitKey(0)