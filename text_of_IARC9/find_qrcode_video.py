import cv2
import numpy as np
import threading
import pyzbar.pyzbar as pyzbar

class qrcode:

    def __init__(self, file):

        self.frame = None
        self.qrcode_1 = None
        self.qrcode_1_last = None
        self.qrcode_2 = None
        self.qrcode_2_last = None
        self.qrcode_3 = None
        self.qrcode_3_last =None
        self.qrcode_4 = None
        self.qrcode_4_flag = None
        self.qrcode = None
        self.qrcode_first = None
        self.qrcode_second = None
        self.read_flag = False
        self.file = file
        self.qrcode_1_flag = 0
        self.qrcode_2_flag = 0
        self.qrcode_3_flag = 0
        self.qrcode_4_flag = 0

        self.capVideo = threading.Thread(target=self.CapVideo)
        self.capVideo.start()
        self.cap = None

        self.Finder = threading.Thread(target=self.first_position)
        self.Finder.start()

        self.judgment= threading.Thread(target=self.judge)
        self.judgment.start()

        #self.Connection = threading.Thread(target=self.final_position)
        #self.Connection.start()

    def CapVideo(self):
        self.cap = cv2.VideoCapture("rtsp://192.168.10.103:8554/steam0")
        while True:
            while self.cap.isOpened() and self.read_flag == False :
                ret, self.frame = self.cap.read()
                if self.frame is not None:
                    cv2.imshow("frame", self.frame)
                self.read_flag = True
                #print(self.read_flag)
                cv2.waitKey(5)


    def first_position(self):
        while True:
            while self.read_flag == True and self.frame is not None:
                image = self.frame
                x, y, ch = image.shape
                M2 = cv2.getRotationMatrix2D((x/2, y/2), -4, 1.0)
                image = cv2.warpAffine(image, M2, (y, x), cv2.INTER_CUBIC, cv2.BORDER_REPLICATE)
                gary = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                ret, binary = cv2.threshold(gary, 50, 255, cv2.THRESH_BINARY_INV)
                #cv2.imshow("binary", binary)
                #cv2.waitKey(0)
                kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
                # pengzhang
                erosion = cv2.erode(binary, kernel, iterations=1)
                dilation = cv2.dilate(erosion, kernel, iterations=1)
                canny = cv2.Canny(erosion, 100, 200)
                img, contours, he = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                for cnt in contours:
                    rect = cv2.minAreaRect(cnt)
                    w = rect[1][0]
                    h = rect[1][1]
                    area = w * h
                    #print(area)
                    if area > 9000  and area < 15000 and w / h < 1.05 and w / h > 0.95:
                        box = cv2.boxPoints(rect)
                        box = np.int0(box)
                        #print("area = %d" % area)
                        # cv2.drawContours(image, [box], 0, (0, 255, 255), 1)
                        #cv2.imshow("find", image)
                        #cv2.waitKey(0)
                       # print(box)
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
                        warped = cv2.warpPerspective(image, M, (h, w))
                        self.qrcode_first = cv2.resize(warped, (400, 400), cv2.cv2.INTER_CUBIC)

                        cv2.imshow("self.qrcode_first", self.qrcode_first)
                        #time.sleep(1)
                cv2.waitKey(5)
                self.read_flag = False
                #print(self.read_flag)
                break

    def judge(self):
        temp = 0
        while True:
            if self.qrcode_1_flag == self.qrcode_2_flag == self.qrcode_3_flag == 2 and self.qrcode_4_flag == 9:
                self.final_position()
                print("---------------")
                break
            while self.qrcode_first is not None and temp == 0:

                temp = 1
                image = self.qrcode_first
                #cv2.imshow("iamge", image)
                image_roi = image[10:390, 10:390]
                image_roi = cv2.resize(image_roi, (400, 400), cv2.cv2.INTER_CUBIC)
               # cv2.imshow("image0", image_roi)
                gary = cv2.cvtColor(image_roi, cv2.COLOR_BGR2GRAY)
                #cv2.imshow("gary", gary)
                ret, binary = cv2.threshold(gary, 50, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
                #cv2.imshow("binary", binary)
                canny = cv2.Canny(binary, 100, 200)
                #cv2.waitKey(0)

                o, warped_contours, he = cv2.findContours(canny, cv2.RETR_TREE, cv2.cv2.CHAIN_APPROX_NONE)
                #print("///////")
                #print(he)
                #print(he[0])

                flag = None
                for j in range(len(he[0]) - 3):
                    if he[0][j][2] == he[0][j + 1][2] - 1:
                        if he[0][j + 1][2] == he[0][j + 2][2] - 1:
                            #if he[0][j + 2][2] == he[0][j + 3][2] - 1:
                                flag = j + 3
                #print("flag %d"% flag)
                if flag is not None:
                    warp_rect = cv2.minAreaRect(warped_contours[flag])
                    warped_x = warp_rect[0][1]
                    warped_y = warp_rect[0][0]

                    if warped_x - 200 > 0 and warped_y - 200 < 0 and self.qrcode_3_flag != 2:
                        self.qrcode_3 = binary
                        if self.qrcode_3_flag == 0:
                            self.qrcode_3_last = binary
                            self.qrcode_3_flag = 1
                            print(self.qrcode_3_flag)
                        else:
                            print(self.qrcode_3_last.shape)
                            print(self.qrcode_3.shape)
                            image_1 = cv2.subtract(self.qrcode_3, self.qrcode_3_last)
                            cv2.imshow("-----", image_1)
                            im, contours, hec = cv2.findContours(image_1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                            m_=0
                            for cn in contours:
                                m_ = cv2.contourArea(cn)
                                m_ = m_+m_


                            if m_< 800:
                                self.qrcode_3_flag = 2
                                #print("写入 ：%s" % file + "new/3.jpg")
                                cv2.imshow("self.qrcode_3", self.qrcode_3)
                                print("self.qrcode_3_flag%d" % self.qrcode_3_flag)
                                #print("warp_x %d" % warped_x)
                                #print("warp_y %d" % warped_y)
                            else:
                                self.qrcode_3_last = self.qrcode_3
                        cv2.waitKey(5)


                    if warped_y - 200 > 0 and warped_x - 200 < 0 and self.qrcode_2_flag != 2:

                        self.qrcode_2 = binary

                        #Wv2.waitKey(0)
                        if self.qrcode_2_flag == 0:
                            self.qrcode_2_last = self.qrcode_2
                            self.qrcode_2_flag = 1
                        else:
                            image_ = cv2.subtract(self.qrcode_2,self.qrcode_2_last)
                            im, contours, he_ = cv2.findContours(image_, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                            m_ = 0
                            for cn in contours:
                                m_ = cv2.contourArea(cn)
                                m_ = m_ + m_

                            print("m_2 = %d" % m_)

                            if m_ < 400:
                                self.qrcode_2_flag = 2

                                #print("warp_x %d" % warped_x)
                                #print("warp_y %d" % warped_y)
                                print("self.qrcode_2_flag%d"%self.qrcode_2_flag)
                                #print("写入 ：%s" % file + "new/2.jpg")

                                cv2.imshow("self.qrcode_2", self.qrcode_2)
                            else:
                                self.qrcode_2_last = self.qrcode_2
                        cv2.waitKey(5)

                    if warped_y - 200 < 0 and warped_x -200 < 0 and self.qrcode_1_flag != 2:
                        self.qrcode_1 = binary

                        if self.qrcode_1_flag == 0:
                            self.qrcode_1_last = self.qrcode_1
                            self.qrcode_1_flag = 1
                        else:
                            image = cv2.subtract(self.qrcode_1,self.qrcode_1_last)
                            im, contours, he_ = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                            m_ = 0
                            for cn in contours:
                                m_ = cv2.contourArea(cn)
                                m_ = m_ + m_
                            print("m_1 = %d" % m_)
                            if m_ < 400:
                                self.qrcode_1_flag = 2
                                #print("写入 ：%s" % file + "new/1.jpg")
                                print("self.qrcode_1_flag%d" % self.qrcode_1_flag)
                               # print("warp_x %d" % warped_x)
                               # print("warp_y %d" % warped_y)
                                cv2.imshow("self.qrcode_1", self.qrcode_1)
                            else:
                                self.qrcode_1_last = self.qrcode_1
                        cv2.waitKey(5)

                if self.qrcode_4_flag < 9 and flag is None:
                    self.qrcode_4 = binary
                    if self.qrcode_4_flag == 0:
                        self.qrcode_4_last = self.qrcode_4
                        self.qrcode_4_flag = 1
                    else:
                        image = cv2.subtract(self.qrcode_4, self.qrcode_4_last)
                        im, contours, he_ = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                        m_ = 0
                        for cn in contours:
                            m_ = cv2.contourArea(cn)
                            m_ = m_ + m_

                        print("m_4 = %d" % m_)
                        if m_ < 800:
                            self.qrcode_4_flag =self.qrcode_4_flag + 1
                            cv2.imshow("self.qrcode_4", self.qrcode_4)
                            print("self.qrcode_4_flag%d" % self.qrcode_4_flag)
                           # print("写入 ：%s" % file + "new/4.jpg")
                        else:
                            self.qrcode_4_last = self.qrcode_4
                    cv2.waitKey(5)
                temp = 0
                break

    def final_position(self):
        print("ok")

        image_x_1 = self.lateral_connect(self.qrcode_1, self.qrcode_2)
        cv2.imshow("image_x_1",image_x_1)
        cv2.waitKey(0)
        image_x_2 = self.lateral_connect(self.qrcode_3, self.qrcode_4)
        cv2.imshow("image_x_2", image_x_2)
        cv2.waitKey(0)
        image = self.lengthways_connect(image_x_1, image_x_2)
        ret, base = cv2.threshold(image, 50, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
        cv2.imshow("base", base)
        cv2.waitKey(0)
        self.qrcode = base

        self.decode_Display()


    def lateral_connect(self,image_1, image_2):
        index_ = 0
        for index_1 in range(0, 25, 1):
            if index_ != 0:
                break
            print("index_1 = %d" % index_1)
            image_1_mask = image_1[0:400, 385 - index_1:400 - index_1]
            cv2.imshow("image_1_mask", image_1_mask)
            area = 400*15
            cv2.imshow("imahge_2", image_2)
            cv2.imshow("image_1_mask", image_1_mask)
            for index in range(0, 25, 1):
                print("index %s" % index)
                image_2_mask = image_2[:, index:index + 15]
                cv2.imshow("image_2_mask", image_2_mask)
                image = cv2.subtract(image_1_mask, image_2_mask)
                cv2.imshow("image", image)
                base = np.zeros((500, 500), np.uint8)

                base[50:450, 50:65] = image
                cv2.imshow("image", base)
                img, image_contours, he_image = cv2.findContours(base, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                m = 0
                # cv2.drawContours(image, image_contours, -1, (0, 255, 0), 1)
                # cv2.imshow("image_contours", image)
                # cv2.waitKey(0)

                for ct in image_contours:
                    m_image = cv2.contourArea(ct)

                    m = m + m_image
                m = area - m
                print("m % d " % m)
                if m > (0.6 * area) and m < 1.01 * area:
                    # print(index + 30)
                    index_ = index + 15
                    break
                else:
                    index_ = 0


        array_1 = np.array((np.arange(400 - index_1, 400).reshape(index_1, 1)))

        array = np.array((np.arange(index_).reshape(index_, 1)))
        # print(array)
        image_2 = np.delete(image_2, array, axis=1)
        image_1 = np.delete(image_1, array_1, axis=1)
        cv2.imshow("fiiiiisdhvcjsgdcia", image_2)
        image = np.hstack((image_1, image_2))
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        # image = cv2.bitwise_not(image)
        image = cv2.resize(image, (800, 400), cv2.cv2.INTER_CUBIC)
        return image

    def lengthways_connect(self, image_1, image_2):
        index_ = 0
        for index_1 in range(0, 20, 1):
            if index_ != 0:
                break
            image_1_mask = image_1[390 - index_1:400 - index_1, :]
            print("index_1 = %d" % index_1)
            area = 8000
            cv2.imshow("image_1_mask", image_1_mask)
            for index in range(0, 30, 1):
                print("index_ = %d" % index_)
                image_2_mask = image_2[index:index + 10, :]
                cv2.imshow("image_2_mask", image_2_mask)
                image = cv2.subtract(image_1_mask, image_2_mask)
                cv2.imshow("bit", image)

                base = np.zeros((900, 900), np.uint8)

                base[50:60, 50:850] = image
                cv2.imshow("image---", base)
                img, image_contours, he_image = cv2.findContours(base, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                m = 0
                for ct in image_contours:
                    m_image = cv2.contourArea(ct)
                    m = m + m_image

                m = area - m
                print("mj = %d" % m)
                if m > (0.9 * area) and m < 1.01 * area:
                    print(index + 10)
                    index_ = index + 10
                    break
                else:
                    index_ = 0
                    # cv2.waitKey(0)
        array = np.array((np.arange(index_).reshape(1, index_)))
        # print(array)
        array_1 = np.array((np.arange(400 - index_1, 400).reshape(1, index_1)))
        image_2 = np.delete(image_2, array, axis=0)
        image_1 = np.delete(image_1, array_1, axis=0)
        cv2.imshow("fiiiiisdhvcjsgdcia", image_2)
        image = np.vstack((image_1, image_2))

        cv2.destroyAllWindows()
        return image

    def decode_Display(self):

                barcodes = pyzbar.decode(self.qrcode)

                # print(barcodes)
                for barcode in barcodes:
                    # 提取条形码的边界框的位置
                    # 画出图像中条形码的边界框
                    (x, y, w, h) = barcode.rect
                    cv2.rectangle(self.qrcode, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    # 条形码数据为字节对象，所以如果我们想在输出图像上
                    # 画出来，就需要先将它转换成字符串
                    barcodeData = barcode.data.decode("utf-8")
                    barcodeType = barcode.type
                    # 绘出图像上条形码的数据和条形码类型
                    text = "{} ({})".format(barcodeData, barcodeType)
                    cv2.putText(self.qrcode, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                                .5, (0, 0, 125), 2)
                    # 向终端打印条形码数据和条形码类
                    print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
                return self.qrcode


if __name__ == '__main__':
    file = "video/"
    cpa = qrcode(file)

