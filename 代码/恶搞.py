import cv2

image  = cv2.imread("C:/Users/yangchao/Desktop/OpenCV/picture/666.jpg",1)
#cv2.namedWindow("hhh")
#cv2.imshow("hhh", image)

print(image.shape)
height = image.shape[0]
width = image.shape[1]
channel = image.shape[2]

for row in range(height):
    for col in range(width):
        for c in range(channel):
            pv = image[row, col, c]
            image[row, col, c] = 90 - pv
cv2.imshow("hhhh",image)
cv2.imwrite("dhl.jpg",image)

cv2.waitKey(0)
cv2.destroyAllWindows()
