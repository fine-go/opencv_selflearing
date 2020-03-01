import  cv2
import numpy as np
from matplotlib import  pyplot as plt
from PIL import Image
import  pytesseract as tess

def recognize_test(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, binnary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    cv2.imshow("binnary", binnary)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(2, 2))
    dst1 = cv2.morphologyEx(binnary, cv2.MORPH_OPEN, kernel)
    cv2.imshow("open", dst1)

    cv2.bitwise_not(dst1, dst1)
    textimage = Image.fromarray(dst1)
    #text = tess.image_to_string(textimage, lang='eng' config='--psm 6 --ome 3 -c tessedit_char_whitelist=0123456789').strip()
    text = tess.image_to_string(dst1, lang='eng', config='--psm 6 --ome -c tessedit_char_whitelist=012346789').strip()
    print("识别结果: %s"%text)


image = cv2.imread("C:/Users/yangchao/Desktop/OpenCV/picture/timg[2].png")
cv2.imshow("image", image)
recognize_test(image)
c = cv2.waitKey(0)
if c == 27:
    cv2.destroyAllWindows()
