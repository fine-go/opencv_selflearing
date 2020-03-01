import cv2
import pyzbar.pyzbar as pyzbar
import qrcode
import numpy as np



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
        return image

def detect():

    frame = cv2.imread("C:/Users/yangchao/Desktop/OpenCV/untitled1/qrcode.png")
    print(frame.shape[:2])
    cv2.imshow("img", frame)
    return frame



def creat_qrcode():
    # 初步生成二维码图像
    qr = qrcode.QRCode(version=5,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=8,border=4)
    qr.add_data(1111)
    qr.make(fit=True)

    # 获得Image实例并把颜色模式转换为RGBA
    img = qr.make_image()
    img = img.convert("RGBA")

    img = qr.make_image(fill_color="black", back_color="white")
    img.save('qrcode.png')


def partition_QR_code(image):
    image_qrcode01 = image[0:200, 0:200]
    image_qrcode02 = image[160:360, 0:200]
    image_qrcode03 = image[160:360, 160:360]
    image_qrcode04 = image[0:200, 160:360]
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
    cv2.imwrite("image_qrcode01.png", image_qrcode01)
    cv2.imwrite("image_qrcode02.png", image_qrcode02)
    cv2.imwrite("image_qrcode03.png", image_qrcode03)
    cv2.imwrite("image_qrcode04.png", image_qrcode04)


if __name__ == '__main__':
    creat_qrcode()
    image = detect()
    partition_QR_code(image)
    decodeDisplay(image)
    c = cv2.waitKey()
    if c == 27:
        cv2.destroyAllWindows()