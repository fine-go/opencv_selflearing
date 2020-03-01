import numpy as np
import cv2

img = cv2.imread(r'C:\Users\yangchao\Desktop\OpenCV\picture\1.JPG' ,-1)

cv2.namedWindow("image")
cv2.imshow("image", img)
print(img.shape)#表示长，款，最后一个3表是为一个rgb图像
cv2.waitKey(0)

 
#创建/复制图像
emptyImage = np.zeros(img.shape, np.uint8)#现在的OenCV中没有ceaeimage这样的函数，创建图像需要使用numPY的函数
cv2.namedWindow("image1")
cv2.imshow("image1", emptyImage)
#创建了一个空白图像

#也可以复制原有的图像来获得一副新图像。
emptyImage2 = img.copy()
cv2.namedWindow("image2")
cv2.imshow("image2",emptyImage2)

#用cvtColor获得原图像的副本。
emptyImage3=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
emptyImage3[...] = 0
cv2.namedWindow("image3")
cv2.imshow("image3",emptyImage2)

#保存图像直接用cv2.imwrite就可以
#第一个参数是保存的路径及文件名，第二个是图像矩阵。
#其中，imwrite()有个可选的第三个参数第三个参数针对特定的格式：
#对于JPEG，其表示的是图像的质量，用0-100的整数表示，默认为95。
#注意，cv2.IMWRITE_JPEG_QUALITY类型为Long，必须转换成int。
#对于PNG，第三个参数表示的是压缩级别。
#cv2.IMWRITE_PNG_COMPRESSION，从0到9,压缩级别越高，图像尺寸越小。默认级别为3：

cv2.imwrite("C:/Users/yangchao/Desktop/OpenCV/picture./11.png", img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])   
cv2.imwrite("C:/Users/yangchao/Desktop/OpenCV/picture./12.png", img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9]) 


#图像宽， 高 通道的获取
#
cv2.waitKey (0)  
cv2.destroyAllWindows()  
