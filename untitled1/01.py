'''
目的：试一试关于并排显示图像合成的问题
'''
import cv2
import numpy as np
from pylab import *
import pyzbar.pyzbar as pyzbar
import importlib


def q():
    img1 = cv2.cvtColor(image_qrcode1, cv2.COLOR_BGR2RGB)
    img3 = cv2.cvtColor(image_qrcode2, cv2.COLOR_BGR2RGB)
    img4 = cv2.cvtColor(image_qrcode3, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(image_qrcode4, cv2.COLOR_BGR2RGB)

    fig = plt.figure()
    subplot(221)
    imshow(img1)
    title('img1')
    axis('off')
    subplot(222)
    imshow(img2)
    title('img2')
    axis('off')
    subplot(223)
    imshow(img3)
    title('img3')
    axis('off')
    subplot(224)
    imshow(img4)
    title('img4')
    axis('off')
    show()

def lianjie_h(src1, src2):
    k = 0
    m = 0
    src1_h, src1_w = src1.shape[:2]
    src2_h, src2_w = src2.shape[:2]
    if src1_h == src2_h and src1_w == src2_w:
        h = src1_h
        w = src1_w

    else:
        h = int((src1_h+src2_h)/2)
        w = int((src1_h+src2_h)/2)
        src1 = cv2.resize(src1, (h, w), cv2.INTER_CUBIC)
        src2 = cv2.resize(src2, (h, w), cv2.INTER_CUBIC)
    for w1 in range(w):
        for h1 in range(h):
            for w2 in range(w):

                    if src1[h1, w1, 1] != src2[h1, w2 - m, 1]:
                        k = k + 1
                        if k < 40:
                            src2 =  delete(src2, w2, axis = 1)#删除第二幅图片相同的部分列
                            m = m +1
    text_h = np.hstack((src1,src2))
    cv2.imshow("text_h", text_h)
    return text_h

#def num(image):

def lianjie_v(src1, src2):
    k = 0
    m = 0
    src1_h, src1_w = src1.shape[:2]
    src2_h, src2_w = src2.shape[:2]
    if src1_h == src2_h and src1_w == src2_w:
        h = src1_h
        w = src1_w

    else:
        h = int((src1_h+src2_h)/2)
        w = int((src1_h+src2_h)/2)
        src1 = cv2.resize(src1, (h, w), cv2.INTER_CUBIC)
        src2 = cv2.resize(src2, (h, w), cv2.INTER_CUBIC)
    for h1 in range(h):
        for w1 in range(w):
            for h2 in range(h):
                if src1[h1, w1, 1] != src2[h1- m, w1 ,1]:
                    k = k + 1
                    if k < 5:
                        src2 = delete(src2, h1, axis= 0)
                        src2 = delete(src2, h1+1, axis=0)

                        m = m + 1
    print(src2.shape)
    text_v = np.vstack((src1,src2))
    return text_v

def a():
    img1 = cv2.cvtColor(image_qrcode1, cv2.COLOR_BGR2RGB)
    img3 = cv2.cvtColor(image_qrcode2, cv2.COLOR_BGR2RGB)
    img4 = cv2.cvtColor(image_qrcode3, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(image_qrcode4, cv2.COLOR_BGR2RGB)
    cv2.imshow("image_qrcode", image_qrcode1)
    cv2.imshow("2", image_qrcode2)
    cv2.imshow("3", image_qrcode3)
    cv2.imshow("3", image_qrcode4)

    '''htitch1= np.hstack((img3,img4))
    htitch2 = np.hstack((img1, img2))
    vstack = np.vstack((htitch2, htitch1))
    cv2.imshow("vstack", vstack)
    #cv2.imshow("htitch1",htitch1)
    #cv2.imshow("htitch2",htitch2)'''


    text_h1 = lianjie_h(img3, img4)
    cv2.imshow("text_h1", text_h1)
    text_h2 = lianjie_h(img1, img2)
    cv2.imshow("text_h2", text_h2)
    text = lianjie_v(text_h2, text_h1)
    cv2.imshow("text", text)
    print(text.shape)

    '''print(image_qrcode1[10, 10])
    print(img1.shape)
    print(img3.shape)
    print(img2.shape)
    print(img1)
    print("kncosdcsckiasc")
    print(img2)
    return vstack'''


    return text

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
        barcodeType = barcode.type
       # 绘出图像上条形码的数据和条形码类型
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(vstack, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    .5, (0, 0, 125), 2)         # 向终端打印条形码数据和条形码类型
        print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))


if __name__ == '__main__':
    image_qrcode1 = cv2.imread("image_qrcode01.png")
    image_qrcode2 = cv2.imread("image_qrcode02.png")
    image_qrcode3 = cv2.imread("image_qrcode03.png")
    image_qrcode4 = cv2.imread("image_qrcode04.png")
    cv2.imshow("image_qrcode01", image_qrcode1)
    cv2.imshow("image_qrcode02", image_qrcode2)
    cv2.imshow("image_qrcode03", image_qrcode3)
    cv2.imshow("image_qrcode04", image_qrcode4)

    #image = a()
    lianjie_v(image_qrcode1,image_qrcode2)
    #decodeDisplay(image)
    c = cv2.waitKey()
    if c == 27:
        cv2.destroyAllWindows()
