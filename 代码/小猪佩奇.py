
import turtle as t
import threading
import pygame
import time


def fun1():
    while True:
        file=r'E:/CloudMusic/1.mp3'
        pygame.mixer.init()
        print("播放音乐1")
        pygame.mixer.music.load(file)

        pygame.mixer.music.play(loops = 0, start=20.0)
        time.sleep(60)
        pygame.mixer.music.stop()
 

def fun2():
    while True:

        t.pensize(4) # 设置画笔的大小

        t.colormode(255) # 设置GBK颜色范围为0-255

        t.color((255,155,192),"pink") # 设置画笔颜色和填充颜色(pink)

        t.setup(840,700) # 设置主窗口的大小为840*500

        t.speed(10) # 设置画笔速度为10

        #鼻子

        t.pu() # 提笔

        t.goto(-100,100) # 画笔前往坐标(-100,100)

        t.pd() # 下笔

        t.seth(-30) # 笔的角度为-30°

        t.begin_fill() # 外形填充的开始标志

        a=0.4

        for i in range(120):

           if 0<=i<30 or 60<=i<90:

               a=a+0.08

               t.lt(3) #向左转3度

               t.fd(a) #向前走a的步长

           else:

               a=a-0.08

               t.lt(3)

               t.fd(a)

        t.end_fill() # 依据轮廓填充

        t.pu() # 提笔

        t.seth(90) # 笔的角度为90度

        t.fd(25) # 向前移动25

        t.seth(0) # 转换画笔的角度为0

        t.fd(10)

        t.pd()

        t.pencolor(255,155,192) # 设置画笔颜色

        t.seth(10)

        t.begin_fill()

        t.circle(5) # 画一个半径为5的圆

        t.color(160,82,45) # 设置画笔和填充颜色

        t.end_fill()

        t.pu()

        t.seth(0)

        t.fd(20)

        t.pd()

        t.pencolor(255,155,192)

        t.seth(10)

        t.begin_fill()

        t.circle(5)

        t.color(160,82,45)

        t.end_fill()

        #头

        t.color((255,155,192),"pink")

        t.pu()

        t.seth(90)

        t.fd(41)

        t.seth(0)

        t.fd(0)

        t.pd()

        t.begin_fill()

        t.seth(180)

        t.circle(300,-30) # 顺时针画一个半径为300,圆心角为30°的园

        t.circle(100,-60)

        t.circle(80,-100)

        t.circle(150,-20)

        t.circle(60,-95)

        t.seth(161)

        t.circle(-300,15)

        t.pu()

        t.goto(-100,100)

        t.pd()

        t.seth(-30)

        a=0.4

        for i in range(60):

           if 0<=i<30 or 60<=i<90:

               a=a+0.08

               t.lt(3) #向左转3度

               t.fd(a) #向前走a的步长

           else:

               a=a-0.08

               t.lt(3)

               t.fd(a)

        t.end_fill()

        #耳朵

        t.color((255,155,192),"pink")

        t.pu()

        t.seth(90)

        t.fd(-7)

        t.seth(0)

        t.fd(70)

        t.pd()

        t.begin_fill()

        t.seth(100)

        t.circle(-50,50)

        t.circle(-10,120)

        t.circle(-50,54)

        t.end_fill()

        t.pu()

        t.seth(90)

        t.fd(-12)

        t.seth(0)

        t.fd(30)

        t.pd()

        t.begin_fill()

        t.seth(100)

        t.circle(-50,50)

        t.circle(-10,120)

        t.circle(-50,56)

        t.end_fill()

        #眼睛

        t.color((255,155,192),"white")

        t.pu()

        t.seth(90)

        t.fd(-20)

        t.seth(0)

        t.fd(-95)

        t.pd()

        t.begin_fill()

        t.circle(15)

        t.end_fill()

        t.color("black")

        t.pu()

        t.seth(90)

        t.fd(12)

        t.seth(0)

        t.fd(-3)

        t.pd()

        t.begin_fill()

        t.circle(3)

        t.end_fill()

        t.color((255,155,192),"white")

        t.pu()

        t.seth(90)

        t.fd(-25)

        t.seth(0)

        t.fd(40)

        t.pd()

        t.begin_fill()

        t.circle(15)

        t.end_fill()

        t.color("black")

        t.pu()

        t.seth(90)

        t.fd(12)

        t.seth(0)

        t.fd(-3)

        t.pd()

        t.begin_fill()

        t.circle(3)

        t.end_fill()

        #腮

        t.color((255,155,192))

        t.pu()

        t.seth(90)

        t.fd(-95)

        t.seth(0)

        t.fd(65)

        t.pd()

        t.begin_fill()

        t.circle(30)

        t.end_fill()

        #嘴

        t.color(239,69,19)

        t.pu()

        t.seth(90)

        t.fd(15)

        t.seth(0)

        t.fd(-100)

        t.pd()

        t.seth(-80)

        t.circle(30,40)

        t.circle(40,80)

        #身体

        t.color("red",(255,99,71))

        t.pu()

        t.seth(90)

        t.fd(-20)

        t.seth(0)

        t.fd(-78)

        t.pd()

        t.begin_fill()

        t.seth(-130)

        t.circle(100,10)

        t.circle(300,30)

        t.seth(0)

        t.fd(230)

        t.seth(90)

        t.circle(300,30)

        t.circle(100,3)

        t.color((255,155,192),(255,100,100))

        t.seth(-135)

        t.circle(-80,63)

        t.circle(-150,24)

        t.end_fill()

        #手

        t.color((255,155,192))

        t.pu()

        t.seth(90)

        t.fd(-40)

        t.seth(0)

        t.fd(-27)

        t.pd()

        t.seth(-160)

        t.circle(300,15)

        t.pu()

        t.seth(90)

        t.fd(15)

        t.seth(0)

        t.fd(0)

        t.pd()

        t.seth(-10)

        t.circle(-20,90)

        t.pu()

        t.seth(90)

        t.fd(30)

        t.seth(0)

        t.fd(237)

        t.pd()

        t.seth(-20)

        t.circle(-300,15)

        t.pu()

        t.seth(90)

        t.fd(20)

        t.seth(0)

        t.fd(0)

        t.pd()

        t.seth(-170)

        t.circle(20,90)

        #脚

        t.pensize(10)

        t.color((240,128,128))

        t.pu()

        t.seth(90)

        t.fd(-75)

        t.seth(0)

        t.fd(-180)

        t.pd()

        t.seth(-90)

        t.fd(40)

        t.seth(-180)

        t.color("black")

        t.pensize(15)

        t.fd(20)

        t.pensize(10)

        t.color((240,128,128))

        t.pu()

        t.seth(90)

        t.fd(40)

        t.seth(0)

        t.fd(90)

        t.pd()

        t.seth(-90)

        t.fd(40)

        t.seth(-180)

        t.color("black")

        t.pensize(15)

        t.fd(20)

        #尾巴

        t.pensize(4)

        t.color((255,155,192))

        t.pu()

        t.seth(90)

        t.fd(70)

        t.seth(0)

        t.fd(95)

        t.pd()

        t.seth(0)

        t.circle(70,20)

        t.circle(10,330)

        t.circle(70,30)






        x = -200

        y = 350





        def txt():

            t1 = (x, y)

            t2 = (x + 12, y - 12)

            penSize = 5

            t.screensize(400, 400, "#fff")

            t.pensize(penSize)

            t.pencolor("#ff0000")

            t.speed(15)

            t.hideturtle()

            # 点、

            t.up()

            t.goto(t1)

            t.down()  # 移动，画线

            t.goto(t2)



            # 横 -

            x1 = x - 18

            y1 = y - 22

            t3 = (x1, y1)

            t4 = (x1 + 60, y1)

            t.up()

            t.goto(t3)

            t.down()

            t.goto(t4)



            # 点、、

            x2 = x1 + 16

            y2 = y1 - 10

            t5 = (x2, y2)

            t6 = (x2 + 8, y2 - 16)

            t7 = (x2 + 26, y2)

            t8 = (x2 + 18, y2 - 18)

            t.up()

            t.goto(t5)

            t.down()

            t.goto(t6)

            t.up()

            t.goto(t7)

            t.down()

            t.goto(t8)



            # 长横-

            x3 = x1 - 15

            y3 = y2 - 24

            t9 = (x3, y3)

            t10 = (x3 + 90, y3)

            t.up()

            t.goto(t9)

            t.down()

            t.goto(t10)



            # 横 -

            x4 = x3 + 10

            y4 = y3 - 22

            t11 = (x4, y4)

            t12 = (x4 + 70, y4)

            t.up()

            t.goto(t11)

            t.down()

            t.goto(t12)



            # 竖 |

            x5 = x + 12

            y5 = y3

            t13 = (x5, y5)

            t14 = (x5, y5 - 90)

            t.up()

            t.goto(t13)

            t.down()

            t.goto(t14)



            # 勾

            x6 = x5

            y6 = y5 - 90

            t15 = (x6 - 12, y6 + 10)

            t.goto(t15)



            # 点、、

            x7 = x6 - 12

            y7 = y5 - 40

            t16 = (x7, y7)

            t17 = (x7 - 8, y7 - 20)

            t.up()

            t.goto(t16)

            t.down()

            t.goto(t17)

            t18 = (x7 + 24, y7 - 5)

            t19 = (x7 + 30, y7 - 16)

            t.up()

            t.goto(t18)

            t.down()

            t.goto(t19)



            # 撇

            x8 = x + 100

            y8 = y - 10

            t20 = (x8, y8)

            t21 = (x8 - 32, y8 - 20)

            t.up()

            t.goto(t20)

            t.down()

            t.goto(t21)



            # 撇

            t22 = (x8 - 40, y8 - 135)

            t.goto(t22)



            # 横

            x9 = x3 + 100

            y9 = y3 - 8

            t23 = (x9, y9)

            t24 = (x9 + 50, y9)

            t.up()

            t.goto(t23)

            t.down()

            t.goto(t24)



            # 竖

            x10 = x9 + 24

            y10 = y9

            t25 = (x10, y10)

            t26 = (x10, y10 - 80)

            t.up()

            t.goto(t25)

            t.down()

            t.goto(t26)

            nian()

            kuai()

            le()

            t.done()





        # 年

        def nian():

            # 撇

            x1 = x + 180

            y1 = y - 10

            t1 = (x1, y1)

            t2 = (x1 - 18, y1 - 28)

            t.up()

            t.goto(t1)

            t.down()

            t.goto(t2)



            # 横

            x2 = x1 - 8

            y2 = y - 25

            t3 = (x2, y2)

            t4 = (x2 + 60, y2)

            t.up()

            t.goto(t3)

            t.down()

            t.goto(t4)



            # 横

            x3 = x2 - 8

            y3 = y - 65

            t5 = (x3, y3)

            t6 = (x3 + 65, y3)

            t.up()

            t.goto(t5)

            t.down()

            t.goto(t6)



            # 小竖

            x4 = x3

            y4 = y3 - 25

            t7 = (x4, y4)

            t.up()

            t.goto(t5)

            t.down()

            t.goto(t7)



            # 长横

            x5 = x4 - 10

            y5 = y4

            t8 = (x5, y5)

            t9 = (x5 + 85, y5)

            t.up()

            t.goto(t8)

            t.down()

            t.goto(t9)



            # 长竖

            x6 = x2 + 25

            y6 = y2

            t10 = (x6, y6)

            t11 = (x6, y6 - 120)

            t.up()

            t.goto(t10)

            t.down()

            t.goto(t11)





        # 快

        def kuai():

            # 点

            x1 = x + 280

            y1 = y - 65

            t1 = (x1, y1)

            t2 = (x1 - 6, y1 - 25)

            t.up()

            t.goto(t1)

            t.down()

            t.goto(t2)



            # 竖

            x2 = x1 + 10

            y2 = y - 15

            t3 = (x2, y2)

            t4 = (x2, y2 - 130)

            t.up()

            t.goto(t3)

            t.down()

            t.goto(t4)



            # 点

            x3 = x2 + 10

            y3 = y1 - 8

            t5 = (x3, y3)

            t6 = (x3 + 6, y3 - 10)

            t.up()

            t.goto(t5)

            t.down()

            t.goto(t6)



            # 横

            x4 = x3 + 25

            y4 = y - 60

            t7 = (x4, y4)

            t8 = (x4 + 60, y4)

            t9 = (x4 + 60, y4 - 28)

            t.up()

            t.goto(t7)

            t.down()

            t.goto(t8)

            t.goto(t9)



            # 长横

            x5 = x4 - 10

            y5 = y4 - 28

            t10 = (x5, y5)

            t11 = (x5 + 90, y5)

            t.up()

            t.goto(t10)

            t.down()

            t.goto(t11)



            # 撇

            x6 = x4 + 30

            y6 = y2 - 5

            t12 = (x6, y6)

            t13 = (x6 - 18, y6 - 125)

            t.up()

            t.goto(t12)

            t.down()

            t.goto(t13)



            # 捺

            x7 = x6 + 8

            y7 = y5 - 20

            t14 = (x7, y7)

            t15 = (x7 + 12, y7 - 38)

            t.up()

            t.goto(t14)

            t.down()

            t.goto(t15)





        # 乐

        def le():

            # 撇

            x1 = x + 510

            y1 = y - 20

            t1 = (x1, y1)

            t2 = (x1 - 65, y1 - 20)

            t3 = (x1 - 68, y1 - 60)

            t4 = (x1 + 10, y1 - 60)

            t.up()

            t.goto(t1)

            t.down()

            t.goto(t2)

            t.goto(t3)

            t.goto(t4)



            # 竖

            x2 = x1 - 30

            y2 = y1 - 35

            t5 = (x2, y2)

            t6 = (x2, y2 - 92)

            t7 = (x2 - 12, y2 - 85)

            t.up()

            t.goto(t5)

            t.down()

            t.goto(t6)

            t.goto(t7)



            # 点、、

            x3 = x2 - 20

            y3 = y2 - 50

            t8 = (x3, y3)

            t9 = (x3 - 8, y3 - 20)

            t.up()

            t.goto(t8)

            t.down()

            t.goto(t9)

            t10 = (x3 + 40, y3 - 5)

            t11 = (x3 + 46, y3 - 16)

            t.up()

            t.goto(t10)

            t.down()

            t.goto(t11)





        # 新年快乐

        def xin():

            t.title('dalao 带带我')  # 设置标题栏文字

            # t.hideturtle()  # 隐藏箭头

            t.getscreen().bgcolor('#f0f0f0')  # 背景色

            t.color('#c1e6c6', 'red')  # 设置画线颜色、填充颜色，可以直接写 green，也可以用 #c1e6c6

            t.pensize(2)  # 笔的大小

            t.speed(1)  # 图形绘制的速度,1~10

            t.up()  # 移动，不画线

            t.goto(0, -150)



            t.down()  # 移动，画线

            # t.begin_fill()  # 开始填充

            # t.goto(0, -150)

            t.goto(-175.12, -8.59)

            t.left(140)

            pos = []

            for i in range(19):

                t.right(10)

                t.forward(20)

                pos.append((-t.pos()[0], t.pos()[1]))

            for item in pos[::-1]:

                t.goto(item)

            t.goto(175.12, -8.59)

            t.goto(0, -150)

            t.left(50)

            t.end_fill()  # 结束填充，显示填充效果



            t.done()




        # xin()

        txt()

threads = []
threads.append(threading.Thread(target=fun1))
threads.append(threading.Thread(target=fun2))

if __name__ == '__main__':
    for t1 in threads:
        t1.start()
