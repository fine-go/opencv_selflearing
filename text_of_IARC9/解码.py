# -*- coding: utf-8 -*-
import threading
import socket
import Tkinter as tki
import time
import numpy as np
import libh264decoder
from PIL import Image
from PIL import ImageTk
import cv2

class h264:
    def __init__(self, ip='192.168.10.1', port=1234):
        self.decoder = libh264decoder.H264Decoder()
        self.frame = None
        self.last_frame = None
        self.is_freeze = False

        self.socket_video = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.tello_address = (ip, port)

        self.socket_video.bind(self.tello_address)
        self.root = tki.Tk()
        self.panel = None

        self.receive_video_thread = threading.Thread(target=self._receive_video_thread)
        self.receive_video_thread.daemon = True
        self.receive_video_thread.start()

        self.stopEvent = threading.Event()
        self.thread = threading.Thread(target=self.videoLoop, args=())
        self.thread.start()

    def video_freeze(self, is_freeze=True):
        self.is_freeze = is_freeze
        if is_freeze:
            self.last_frame = self.frame

    def read(self):
        if self.is_freeze:
            return self.last_frame
        else:
            return self.frame

    def __del__(self):

        self.socket_video.close()

    def _receive_video_thread(self):
        packet_data = ""
        while True:
            try:
                res_string, ip = self.socket_video.recvfrom(2048)
                packet_data += res_string
                # end of frame
                # print(len(packet_data))
                if len(packet_data) != 1460:
                    for frame in self._h264_decode(packet_data):
                        self.frame = frame
                    packet_data = ""

            except socket.error as exc:
                print ("Caught exception socket.error : %s" % exc)

                # 解码

    def _h264_decode(self, packet_data):
        # print(packet_data)
        res_frame_list = []
        frames = self.decoder.decode(packet_data)
        # print (type(frames))
        for framedata in frames:
            # print(type(framedata))
            (frame, w, h, ls) = framedata
            # print (type(frame))
            if frame is not None:
                # print 'frame size %i bytes, w %i, h %i, linesize %i' % (len(frame), w, h, ls)
                frame = np.fromstring(frame, dtype=np.ubyte, count=len(frame), sep='')
                frame = (frame.reshape((h, ls / 3, 3)))
                frame = frame[:, :w, :]

                res_frame_list.append(frame)
        # print(type(res_frame_list))
        # print(res_frame_list)
        return res_frame_list



    def videoLoop(self):
        try:
            self.frame = self.read()
            if self.frame is None or self.frame.size == 0:
                print("frame_GUI is None")

            image = Image.fromarray(self.frame)
            # 更新实时显示面板
            self._updateGUIImage(image)
        except RuntimeError as e:
            print("[INFO] caught a RuntimeError %s" % e)

    def _updateGUIImage(self, image):
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        # 如果面板没有，则进行初始化
        if self.panel is None:
            self.panel = tki.Label(image=image)
            self.panel.image = image

        # 或者更新面板
        else:
            self.panel.configure(image=image)
            self.panel.image = image

def main():
    drone = h264()

    # GUI的主进程
    drone.root.mainloop()

if __name__ == "__main__":
    main()