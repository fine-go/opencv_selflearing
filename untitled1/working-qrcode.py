import cv2
import qrcode
import numpy as np
import pyzbar
from PIL import Image
import threading

global A, B, C, D
A = B = C = D = 0

#创建二维码
def create_qrcode():
    # 初步生成二维码图像
    qr = qrcode.QRCode(version=5,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=8,border=4)
    qr.add_data(0000)
    qr.make(fit=True)

    # 获得Image实例并把颜色模式转换为RGBA
    img = qr.make_image()
    img = img.convert("RGBA")

    img = qr.make_image(fill_color="black", back_color="white")
    img.save('qrcode.png')
    #img.show("qrcode")
    #print(img.dtype)
    #print(img)


    '''version：值为1~40的整数，控制二维码的大小（最小值是1，是个12×12的矩阵）。 如果想让程序自动确定，将值设置为 None 并使用 fit 参数即可。
    error_correction：控制二维码的错误纠正功能。可取值下列4个常量。
　　ERROR_CORRECT_L：大约7%或更少的错误能被纠正。
　　ERROR_CORRECT_M（默认）：大约15%或更少的错误能被纠正。
　　ROR_CORRECT_H：大约30%或更少的错误能被纠正。
    box_size：控制二维码中每个小格子包含的像素数。
    border：控制边框（二维码与图片边界的距离）包含的格子数（默认为4，是相关标准规定的最小值）
    image_factory：选择生成图片的形式，默认为 PIL 图像。
    mask_pattern：选择生成图片的的掩模'''

    return img

def second():

    #得到4个mask和四块二维码
    def qrcode_partition(image):
        image_qrcode01 = image[0:200, 0:200]
        image_qrcode02 = image[181:360, 0:200]
        image_qrcode03 = image[181:360, 0:200]
        image_qrcode04 = image[181:306, 181:306]
        #顺时针的mask
        mask01 = image[180:200, 0:200]
        mask02 = image[181:360, 181:200]
        mask03 = image[181:200, 0:200]
        mask04 = image[181:200, 0:200]
        #cv2.imshow("image_qrcode01", image_qrcode01)
        #cv2.imshow("image_qrcode02", image_qrcode02)
        cv2.imshow("mask01", mask01)
        cv2.imshow("mask02", mask02)
        cv2.imshow("mask03", mask03)
        cv2.imshow("mask04", mask04)
        cv2.imwrite("image_qrcode1.png", image_qrcode01)
        cv2.imwrite("image_qrcode2.png", image_qrcode02)
        cv2.imwrite("image_qrcode3.png", image_qrcode03)
        cv2.imwrite("image_qrcode4.png", image_qrcode04)
        cv2.imwrite("mask1.png", mask01)
        cv2.imwrite("mask2.png", mask02)
        cv2.imwrite("mask3.png", mask03)
        cv2.imwrite("mask4.png", mask04)

    def bit(src1, src2):
        mask = cv2.bitwise_and(src1,src2)
        return mask

    def put(j,v,mask, src):
        if j == v:
            src[]
          

    #定位
    def location(i, image):
        image_qrcode_i = cv2.imread("image_qrcode"+i+".png")
        src = np.zeros(image.shape, np.uint8)
        src_x, src_y = image_qrcode_i.shape

        gary = cv2.cvtColor(image_qrcode_i, cv2.COLOR_BGR2GRAY)
        ret, bianory = cv2.threshold(gary,0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)
        contours, hst = cv2.findContours(gary, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        img = cv2.drawContours(gary,contours,-1,(0,0,255),4)
        cv2.imshow("gary", gary)

        contours2, hst2 = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        print(contours2)

        Min_Area = 20#除去小矩形
        contours = [cnt for cnt in contours if cv2.contourArea(cnt) > Min_Area]
        image_contours = []
        for cnt in contours2:
            rect = cv2.minAreaRect(cnt)
            area_width, area_height = rect[1]
            if area_width < area_height:

                area_width, area_height = area_height, area_width

            wh_ratio = area_width / area_height

            print("wh_ratio", wh_ratio)

            #要求矩形区域长宽比在2到5.5之间，2到5.5是长宽比，其余的矩形排除

            if wh_ratio > 0.99 and wh_ratio < 1.1:

                image_contours.append(rect)

                box = cv2.boxPoints(rect)
                box = np.int0(box)

                oldimg = cv2.drawContours(image_qrcode_i, [box], 0, (0, 255, 255), 2)

                cv2.imshow("edge4", oldimg)

                print(rect)
                print(rect[0])
                x, y = image_qrcode_i.shape[:2]
                a, b = rect[0]
                if a - x > 0 :#右上 A1, B0
                    src[src_x - x -20:src_x,0: src_y - y - 20] = image_qrcode_i[x - 20: x, 0:y - 20]
                    maskA1 = image_qrcode_i[0:20, 0:y]
                    maskB0 = image_qrcode_i[0:x, y - 21:y]
                    cv2.imwrite("maska1.png", maskA1)
                    cv2.imwrite("maskb0.png",maskB0)
                else:
                    if b - y < 0 :#左上A0, D1
                        src[0: x - 20, 0: y - 20 ] = image_qrcode_i[0 : x - 20, 0 : y - 20]
                        maskA0 = image_qrcode_i[0:20, 0:y - 20]
                        maslD1 = image_qrcode_i[0:x, y - 21:y]
                        cv2.imwrite("maska0.png", maskA0)
                        cv2.imwrite("masld1.png", maslD1)
                    else:#左下 D0, C1
                        src[0: x - 20,src_y - y - 20: src_y ] = image_qrcode_i[0 : x - 20, y - 20 : y ]
                        maskD0 = image_qrcode_i[0:x, 0:20]
                        maskC1 = image_qrcode_i[x - 20:x, 0:y]
                        cv2.imwrite("maskd0.png", maskD0)
                        cv2.imwrite("maskc1.png", maskC1)
                if len(box)  != 0 :#右下 B1, C0`
                    src[src_x - x - 20:src_x,  src_y - y - 20:src_y] = image_qrcode_i[x - 20:x ,y - 20:y]
                    maskB1 = image_qrcode_i[0:x, 0:20]
                    maskC0 = image_qrcode_i[0:20, 0:y]
                    cv2.imwrite("maskb1.png", maskB1)
                    cv2.imwrite("maskc0.png", maskC0)
                m = [A, B, C, D]
                for j in m:
                    src1 = cv2.imread("mask"+"j"+"0"+".png")
                    src2 = cv2.imread("mask"+"j"+"1"+".png")
                    src1_x, src1_y = src1.shape[:2]
                    src2_x, src2_y = src2.shape[:2]
                    if src1_x== src2_x and src1_y == src2_y:
                        mask  = bit(src1, src2)
                    else:
                        mask_x = int((src1_x + src2_x)/2)
                        mask_y = int((src1_y + src2_y)/2)
                        src1_changed = cv2.resize(src1, (mask_x, mask_y), interpolation=cv2.INTER_CUBIC)
                        src2_changed = cv2.resize(src2, (mask_x, mask_y), interpolation=cv2.INTER_CUBIC)
                        mask = bit(src1_changed, src2_changed)








        return  src


    def decodeDisplay(image):
        barcodes = pyzbar.decode(image)
        for barcode in barcodes:
            # 提取二维码的边界框的位置
                #  画出图像中条形码的边界框
            (x, y, w, h) = barcode.rect
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
           # 提取二维码数据为字节对象，所以如果我们想在输出图像上
            #画出来，就需要先将它转换成字符串
            barcodeData = barcode.data.decode("utf-8")
            barcodeType = barcode.type         #
           # 绘出图像上条形码的数据和条形码类型
            text = "{} ({})".format(barcodeData, barcodeType)
            cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        .5, (0, 0, 125), 2)         # 向终端打印条形码数据和条形码类型
            print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
            #return image



threads = []
threads.append(threading.Thread(target=create_qrcode))
threads.append(threading.Thread(target=second))

if __name__ == '__main__':
    for t1 in threads:
        t1.start()



c = cv2.waitKey()
if c == 27:
    cv2.destroyAllWindows()




