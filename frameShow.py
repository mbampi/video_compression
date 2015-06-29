"""
 Projeto de Iniciacao Cientifica IFRS - Campus Farroupilha
 Tecnico em Informatica integrado ao Ensino Medio

 PROJETO    Compressao de Video
 AUTOR      Matheus Dussin Bampi
 ORIENTACAO Felipe Sampaio
 INICIO     Maio/2015
"""

import struct
import numpy as np
import Image as Im
from Tkinter import *


video = open("videos/BQSquare_416x240_60.yuv", 'rb')
# characters and frames
video.seek(0, 2)
size = video.tell()
frames = size/((240*416)+(120*208)+(120*208))
time = frames/30
matrixY = np.empty((240, 416), int)
matrixCb = np.empty((120, 208), int)
matrixCr = np.empty((120, 208), int)

def create_matrix(num):
    # frames
    print("\n\n Binary characters: ")
    video.seek(num, 0)
    print(num)
    # frame Y
    print("Frame Y")
    for line in range(0, 240):
        for column in range(0, 416):
            byte = video.read(1)
            byte_to_int = struct.unpack('B', byte)[0]
            matrixY[line, column] = byte_to_int
    # frame Cb
    print("Frame Cb")
    for line in range(0, 120):
        for column in range(0, 208):
            byte = video.read(1)
            byte_to_int = struct.unpack('B', byte)[0]
            matrixCb[line, column] = byte_to_int
    # frame Cr
    print("Frame Cr")
    for line in range(0, 120):
        for column in range(0, 208):
            byte = video.read(1)
            byte_to_int = struct.unpack('B', byte)[0]
            matrixCr[line, column] = byte_to_int


def frame(num, img_name):
    num = int(num)
    num = (num * ((240*416)+(120*208)+(120*208)))
    create_matrix(num)
    grey = matrixY.astype('uint8')
    grey = Im.fromarray(grey, "L")
    grey.save("saved_img/" + img_name + ".bmp")


def set_gui():
    gui = Tk()
    frame_num = IntVar()
    img_name = StringVar()
    gui.title(" Video Frame Manipulation ")
    Label(text="Video Frame Manipulation").grid(row=0, column=0, columnspan=2)
    Label(text="  ").grid(row=1, column=0, columnspan=2)
    Label(text=(size, "characters")).grid(row=2, column=0, columnspan=2)
    Label(text=(frames, "frames")).grid(row=3, column=0, columnspan=2)
    Label(text=(time, "Seconds")).grid(row=4, column=0, columnspan=2)
    Label(text="Frame: ").grid(row=5, column=0)
    Entry(gui, textvariable=frame_num, width=6).grid(row=5, column=1)
    Label(text="Img Name: ").grid(row=6, column=0)
    Entry(gui, textvariable=img_name, width=12).grid(row=6, column=1)
    Label(text="  ").grid(row=7, column=0, columnspan=2)
    Button(text="Show Frame", command=lambda: frame((frame_num.get()), img_name.get())).grid(row=8, column=0,
                                                                                               columnspan=2)
    gui.mainloop()

# MAIN:
set_gui()
video.close()
