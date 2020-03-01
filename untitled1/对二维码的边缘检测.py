import cv2

def canny(image):
    dst = cv2.Canny(image, 100, 150)
    cv2.imshow("dst", dst)

def find(image):
    gary = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, bianory = cv2.threshold(gary,0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)
    contours, hst = cv2.findContours(gary, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.imshow("c", contours)
    img = cv2.drawContours(gary,contours,-1,(0,0,255),4)
    cv2.imshow("gary", gary)
    dst = cv2.Canny(img, 100, 150)
    cv2.imshow("dst", dst)

image = cv2.imread("qrcode.png")
cv2.imshow("image", image)
#canny(image)
find(image)
c = cv2.waitKey()
if c == 27:
    cv2.destroyAllWindows()