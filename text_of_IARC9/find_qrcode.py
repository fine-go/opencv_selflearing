import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

def caijian_x(image_1, image_2):
    image_1_mask = image_1[:, 170:200]
    (w, h, ch) = image_1_mask.shape
    print(ch)

    area = w*h
    print("area %d"% area)
    cv2.imshow("image_1_mask", image_1_mask)
    for index in range(0,100,10):
        print(index)
        image_2_mask = image_2[:,index:index+30]
        cv2.imshow("image_2_mask", image_2_mask)
        image = cv2.subtract(image_1_mask, image_2_mask)
        cv2.imshow("image", image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        img, image_contours, he_image = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        m = 0
        cv2.drawContours(image, image_contours, -1, (0,255, 0), 1)
        cv2.imshow("image_contours", image)
        for ct in image_contours:
            m_image = cv2.contourArea(ct)
            m = m+ m_image
        print(m)
        if m<(area - (0.8*area)):
            print(index + 30)
        break
    array = np.array((np.arange(30).reshape(30,1)))
    print(array)
    image_2 = np.delete(image_2, array, axis = 1)
    cv2.imshow("fiiiiisdhvcjsgdcia", image_2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return image_2

def caijian_y(image_1, image_2):
    image_1_mask = image_1[170:200,: ]
    (w, h, ch) = image_1_mask.shape
    print(ch)

    area = w*h
    print("area %d"% area)
    cv2.imshow("image_1_mask", image_1_mask)
    for index in range(0,100,10):
        print(index)
        image_2_mask = image_2[index:index+30,:]
        cv2.imshow("image_2_mask", image_2_mask)
        image = cv2.subtract(image_1_mask, image_2_mask)
        cv2.imshow("image", image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        img, image_contours, he_image = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        m = 0
        cv2.drawContours(image, image_contours, -1, (0,255, 0), 1)
        cv2.imshow("image_contours", image)
        for ct in image_contours:
            m_image = cv2.contourArea(ct)
            m = m+ m_image
        print(m)
        if m<(area - (0.65*area)):
            print(index + 30)
        break
    array = np.array((np.arange(30).reshape(1,30)))
    print(array)
    image_2 = np.delete(image_2, array, axis = 0)
    cv2.imshow("fiiiiisdhvcjsgdcia",image_2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return image_2

def decode_Display(image):

    barcodes = pyzbar.decode(image)

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

def preprocesse(file):
    for i in range(1,5,1):
        print(i)
        image = cv2.imread(file+str(i)+".jpg")

        image = cv2.pyrDown(image, 8)
        #image = cv2.pyrDown(image, 8)
        #image = cv2.pyrDown(image, 8)
        #image = cv2.medianBlur(image, 1)
        #cv2.imshow("image"+str(i), image)
        gary = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        #cv2.imshow("gary" + str(i), gary)
        # binary = cv2.adaptiveThreshold(gary, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 14 )
        ret, binary = cv2.threshold(gary, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        cv2.imshow("binary"+str(i),binary)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
        kernel_1 = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))

        erosion = cv2.erode(binary, kernel_1, iterations=1)
        cv2.imshow("ercode" + str(i), erosion)
        dilation = cv2.dilate(erosion, kernel, iterations=1)  # 膨胀处理
        cv2.imshow("dilation" + str(i), dilation)

        #dilation_ed = cv2.erode(erosion, kernel_3, iterations=1)
        cv2.imshow("dilation_ed" + str(i), dilation)
        canny = cv2.Canny(erosion, 100, 200)
        O, contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
        # cv2.imshow("iamge - "+str(i), image)
        #cv2.waitKey(0)
        for cnt in contours:
            # rect （最小外接矩形的中心（x，y），（宽度，高度），旋转角度
            rect = cv2.minAreaRect(cnt)
            # 获取最小外接矩形的4个顶点
            box = cv2.boxPoints(rect)
            box = np.int16(box)
            # print(box)
            # cv2.drawContours(image, [box], 0, (0, 0, 255), 3)
            # cv2.wai tKey(0)
            m = cv2.contourArea(cnt)
            print("m = %s"% m)
            cv2.drawContours(image, [cnt],0,(0, 0, 255), 1)
            cv2.imshow("image_oj"+ str(i), image)
            # cv2.waitKey(0)
            if m<25000 and m>6500:
                print(0)
                rect = cv2.minAreaRect(cnt)
                print(rect[0]) # 中心点坐标x,y
                print(rect[1]) # 宽 高
                print(rect[2]) # 旋转角度
                w = rect[1][0]
                h = rect[1][1]
                print(w)
                print(h)
                print(w/h)
                if (w/h) <1.15 and (w/h) >0.9:
                    print("zhengfangxing")
                    box = cv2.boxPoints(rect)
                    box = np.int0(box)
                    print(box)
                    cv2.drawContours(image, [box], 0, (0, 255, 0), 1)
                    k1 = (box[0][1] - box[2][1])/(box[0][0] - box[2][0])
                    b1 = box[2][1] - k1*box[2][1]
                    k2 = (box[1][1] - box[3][1])/(box[1][0] - box[3][0])
                    b2 = box[3][1] - box[3][0]*k2

                    y = (b1*k2 - b2*k1)/(k2 - k1)
                    x = (y - b1)/k1
                    if abs(x - rect[0][0]) < 600 and abs(y - rect[0][1])<600:


                        box = box.astype("float32")
                        dst_rect = np.array([[0,h],
                                             [0, 0],
                                             [w, 0],
                                             [h, w]],
                                            dtype = np.float32)
                        M = cv2.getPerspectiveTransform(box, dst_rect)
                        # M = M.astype("uint8")
                        print(M)
                        w = int (w)
                        h = int(h)
                        print(gary.dtype)
                        warped = cv2.warpPerspective(gary, M, (w,  h))
                        #cv2.imshow("warped",warped)
                        warped_ = cv2.resize(warped, (200, 200), cv2.cv2.INTER_CUBIC)
                        cv2.imwrite(file + "warp_"+str(i)+".jpg", warped_)
                        cv2.imshow("warped", warped_)

                        ''' 
                         warped_med = cv2.medianBlur(warped_, 3)
                        warped_binnry = cv2.adaptiveThreshold(warped_med, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 10 )
                        cv2.imshow("warped_binny", warped_binnry)
                        '''
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def location(file):
    for i in range(1, 5 ,1):
        warped_imread = cv2.imread(file+"warp_"+str(i)+".jpg", cv2.IMREAD_GRAYSCALE)
        #cv2.imshow("warped_imread", warped_imread)
        warped_med = cv2.medianBlur(warped_imread, 7)
        cv2.imshow("warped_med", warped_med)
        # print(warped_med)
        #warp_binary = cv2.adaptiveThreshold(warped_med, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
        ret, warp_binary = cv2.threshold(warped_med, 2, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
        # warp_binary = cv2.adaptiveThreshold(warped_med, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        #cv2.imshow("warp_binary", warp_binary)
        warped_Canny = cv2.Canny(warp_binary, 50, 100)
        cv2.imshow("warped_Canny", warped_Canny)
        o, warped_contours, he = cv2.findContours(warped_Canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        print(type(he))
        cv2.drawContours(warped_imread, warped_contours, -1, (0, 255, 255), 1)
        #cv2.imshow("warped_imread_Contours", warped_imread)
        #cv2.waitKey(0)
        print(len(he[0]))
        print(he)
        flag = None
        for j in range(len(he[0])-5):
            #print("j is%s"% j)
            #print("he[0][j][2] %d"% he[0][j][2])
            if he[0][j][2] == he[0][j+1]                [2]-1:
                if he[0][j+1][2] == he[0][j+2][2]-1:
                    #if he[0][j+2][2] == he[0][j+3][2]-1:
                        #if he[0][j+3][2] == he[0][j+4][2]-1:
                            print("find it")
                            print("it is %d"% (j+2))
                            print("he[0][j][2] %d"% he[0][j][2])
                            flag = j+2
        print("flag%s"%flag)
        if flag is not None:
            warp_rect = cv2.minAreaRect(warped_contours[flag])
            print(warp_rect[0])
            warp_box = cv2.boxPoints(warp_rect)
            warp_box = np.int0(warp_box)
            warped_x = warp_rect[0][0]
            warped_y = warp_rect[0][1]
            print("warp_x %d"% warped_x)
            print("warp_y%d"% warped_y)
            if warped_x-100 > 0:
                cv2.imwrite(file+"new/2.jpg", warped_imread)
                print(file+"new/2.jpg")
            else:
                if warped_y - 100 > 0:
                    cv2.imwrite(file + "new/3.jpg", warped_imread)
                    print(file + "new/3.jpg")
                else:
                    cv2.imwrite(file + "new/1.jpg", warped_imread)
        else:
            cv2.imwrite(file + "new/4.jpg", warped_imread)
            print(file + " new/4.jpg")
        cv2.waitKey(0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def pinjie(file):
    changed = [[],[],[],[]]
    for i in range(1, 5, 1):
        changed[i-1] = cv2.imread(file + "new/"+str(i)+".jpg")
        cv2.imshow("changed"+str(i), changed[i-1])
        cv2.waitKey(0)
    changed[1] = caijian_x(changed[0], changed[1])
    changed[3] = caijian_x(changed[2], changed[3])

    text_x = np.hstack((changed[0], changed[1]))
    cv2.imshow("text_x",text_x)
    text_h = np.hstack((changed[2], changed[3]))
    cv2.imshow("text_h",text_h)
    cv2.waitKey(0)
    text_h = caijian_y(text_x, text_h)
    cv2.imshow("text_h",text_h)
    text = np.vstack((text_x, text_h))

    cv2.imshow("fine", text)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    text_dilation = cv2.dilate(text, kernel, iterations=1)
    text_erosion = cv2.erode(text_dilation, kernel, iterations=1)
    cv2.imshow("text_dilation", text_dilation)
    cv2.imshow("text_erosion", text_erosion)
    cv2.imwrite(file+"fine.jpg", text)
    text_erosion = cv2.cvtColor(text_erosion, cv2.COLOR_RGB2GRAY)
    ret, binary = cv2.threshold(text_erosion, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    # binary = cv2.adaptiveThreshold(text_erosion, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 10)
    finnnnnn = decode_Display(binary)
    cv2.imshow("binary", binary)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':

    file = "picture_5/"
    preprocesse(file)
    print(file)
    location(file)
    pinjie(file)