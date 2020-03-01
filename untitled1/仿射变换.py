import  cv2
import numpy as np
from matplotlib import  pyplot as plt

def a(pv):
    if pv != 0:
        return pv
    else:
        return 0


img=cv2.imread('C:/Users/yangchao/Desktop/OpenCV/picture/1.jpg')
row,col=img.shape[:2]
points=np.float32([[0,0],[0,0],[0,0],[0,0]])#变换的四个边界点信息

def h(pv):
    if pv !=0:
        return pv
    else:
        return 0

click_times = 0

def get_Points(event,x,y,flags,param):

    global click_times, row, col, points



    if event==cv2.EVENT_LBUTTONDOWN:
        #click_times = 0
        h(click_times)

        #global click_times, row, col, points
        click_times = click_times + 1
        points[click_times - 1]=[x,y]#将点击点的左边传给我们的points，用来变换的第一批参数

        print(points[click_times - 1])

        cv2.circle(img,(x,y),4,(25,25,255),-1)#标记我们点击的位置信息

        cv2.rectangle(img,(col-60,row-20), (col,row), (255,255,255), -1)#空出一小块地方用来现实鼠标点击的位置

        cv2.putText(img,'%d,%d'%(x,y),(col-60,row-8),cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,0,0),1)

        print(click_times)
        return click_times



cv2.namedWindow('image')
cv2.setMouseCallback('image',get_Points)

while(1):

    cv2.imshow('image',img)

    c = cv2.waitKey(10)
    if c == 27 or click_times>=4:#当按下q或者满4个点退出，进行变换

        break

cv2.destroyAllWindows()


pts2=np.float32([[0,0],[300,0],[0,300],[300,300]])#输出图像的分辨率

M=cv2.getPerspectiveTransform(points,pts2)

dst=cv2.warpPerspective(img,M,(300,300))#透视变换



plt.subplot(121),plt.imshow(img,'gray'),plt.title('Input')

plt.subplot(122),plt.imshow(dst,'gray'),plt.title('Output')

plt.show()

c = cv2.waitKey(0)
if c == 27:
    cv2.destroyAllWindows()