import cv2
'''
cv2.CAP_PROP_POS_MSEC                   0                    视频文件的当前位置（以毫秒为单位）或视频捕获时间戳
cv2.CAP_PROP_POS_FRAMES                 1                    基于0的索引将被解码/捕获下一帧
cv2.CAP_PROP_POS_AVI_RATIO              2                    视频文件的相对位置：0 - 视频的开始，1 - 视频的结束
cv2.CAP_PROP_FRAME_WIDTH                3                    帧的宽度
cv2.CAP_PROP_FRAME_HEIGHT               4                    帧的高度
cv2.CAP_PROP_FPS                        5                    帧速
cv2.CAP_PROP_FOURCC                     6                    4个字符表示的视频编码器格式
cv2.CAP_PROP_FRAME_COUNT                7                    帧数
cv2.CAP_PROP_FORMAT                     8                    byretrieve()返回的Mat对象的格式
cv2.CAP_PROP_MODE                       9                    指示当前捕获模式的后端特定值
cv2.CAP_PROP_BRIGHTNESS                 10                   图像的亮度（仅适用于相机）
cv2.CAP_PROP_CONTRAST                   11                   图像对比度（仅适用于相机）
cv2.CAP_PROP_SATURATION                 12                   图像的饱和度（仅适用于相机）
cv2.CAP_PROP_HUE                        13                   图像的色相（仅适用于相机）
cv2.CAP_PROP_GAIN                       14                   图像的增益（仅适用于相机）
cv2.CAP_PROP_EXPOSURE                   15                   曝光（仅适用于相机）
cv2.CAP_PROP_CONVERT_RGB                16                   表示图像是否应转换为RGB的布尔标志
cv2.CAP_PROP_WHITE_BALANCE              17                   目前不支持
cv2.CAP_PROP_RECTIFICATION              18                   立体摄像机的整流标志
'''
cap = cv2.VideoCapture("rtsp://192.168.10.103:8554/steam0")
light = cap.get(10)
print(light)
cmp = cap.get(11)
print(cmp)
cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
a = cap.set(cv2.CAP_PROP_CONVERT_RGB , 5)
print(a)
cm = cap.get(15)
cm2 = cap.get(13)

print(cm)
cap.set(3, 1280)
c = cap.set(3, 1000)
cap.set(4, 720)
print()
print(cm2)
print(c)
b = cap.set(10,20)
print(b)
cap.set(11,32)



while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow("frame", frame)
    cv2.waitKey(15)
