import cv2

image = cv2.imread("C:/Users/yangchao/Desktop/OpenCV/untitled1/qrcode.png")
cv2.imshow("image", image)
c = cv2.waitKey()
if c == 27:
    cv2.destroyAllWindows()