# coding: utf-8
 
#学习opencv中基本的图像处理操作
import numpy as np
import cv2
 
#读取图像
def readImage_my(C:\Users\yangchao\Desktop\OpenCV\picture.1.jpg):
#cv2.imread(filename[,flags]),返回图像，作用：加载图像并返回该图像,flags>0:返回3通道颜色，=0:返回灰度图像，<0:返回的图像带有透明度,alpha是灰度通道，记录透明度信息
    img = cv2.imread("0_snap.png" , 0)
    img = cv2.imread("0_snap.png" , 1)
    img = cv2.imread("0_snap.png" , -1)
    cv2.imshow("image" , img)
    #0表示永久等待键盘输入，waitKey()是键盘绑定函数，时间尺度是毫秒级，特定的几毫秒内，如果有键盘输入，函数会返回按键的ASCII码值
    cv2.waitKey(0)
    #删除建立的窗口，删除特定的窗口用cv2.destroyWindow(),参数是想删除的窗口名
    cv2.destroyAllWindows()
 
#保存图像
#def imwrite_test():
    img = cv2.imread("0_snap.png" , 1)
    '''
    cv2.imwrrite(filename,img[,params])->返回值，参数:filename是文件名称,img是保存的图像，作用：将图像保存成指定格式的文件,注意这里的params是一个数组
    对于JPEG,可以是有质量的保存 CV_IMWRITE_JPEG_QUALITY 从0到100,100表示最高保存质量，默认95
    对于WEBP,                  CV_IMWRITE_WEBP_QUALITY
    对于PNG，可以是压缩级别     CV_IMWRITE_PNG_COMPRESSION:从0到9，越小表示保存的大小越大，压缩时间越少，默认为3
    alpha为0时表示透明，255时表示不透明
    '''
    #注意cv2.IMWRITE_PNG_COMPRESSION类型为Long，必须转换成int
   

