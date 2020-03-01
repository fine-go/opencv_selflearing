import cv2

def surf(src1, src2):
    cv2.xfeatures2d_SURF.create()



image = cv2.imread("qrcode.png")
cv2.imshow("image", image)
surf(image)
c = cv2.waitKey()
if c == 27:
    cv2.destroyAllWindows()