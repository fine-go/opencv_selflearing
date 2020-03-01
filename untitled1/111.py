import cv2
import pyzbar.pyzbar as pyzbar
import qrcode
import numpy as np

#创建二维码
def create_qrcode():
    qr = qrcode.QRCode(version=5,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=8,border=4)
    qr.add_data(2365)
    qr.make(fit=True)

    # 获得Image实例并把颜色模式转换为RGBA
    img = qr.make_image()
    img = img.convert("RGBA")

    img = qr.make_image(fill_color="black", back_color="white")
    img.save('qrcode1.png')

create_qrcode()
c = cv2.waitKey()
if c == 27:
    cv2.destroyAllWindows()
