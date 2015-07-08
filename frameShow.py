"""
 Projeto de Iniciacao Cientifica IFRS - Campus Farroupilha
 Tecnico em Informatica integrado ao Ensino Medio

 PROJETO    Compressao de Video
 AUTOR      Matheus Dussin Bampi
 ORIENTACAO Felipe Sampaio
 INICIO     Maio/2015
"""

from Tkinter import *
from Frame import Frame
import Image as Im


def save_frame(num, img_name):
    f = Frame()
    num = int(num)
    num = (num * ((240*416)+(120*208)+(120*208)))
    f.create_matrix(num)
    grey = f.matrixY.astype('uint8')
    grey = Im.fromarray(grey, "L")
    grey.save("saved_img/" + img_name + ".bmp")

def set_gui():
    gui = Tk()
    frame_num = IntVar()
    img_name = StringVar()
    dicio = Frame.video_specifications()
    gui.title(" Video Frame Manipulation")
    Label(text="Video Frame Manipulation").grid(row=0, column=0, columnspan=2)
    Label(text="  ").grid(row=1, column=0, columnspan=2)
    Label(text=(dicio['size'], "Bytes")).grid(row=2, column=0, columnspan=2)
    Label(text=(dicio['frames'], "Frames")).grid(row=3, column=0, columnspan=2)
    Label(text=(dicio['time'], "Seconds")).grid(row=4, column=0, columnspan=2)
    Label(text="Frame: ").grid(row=5, column=0)
    Entry(gui, textvariable=frame_num, width=6).grid(row=5, column=1)
    Label(text="Img Name: ").grid(row=6, column=0)
    Entry(gui, textvariable=img_name, width=12).grid(row=6, column=1)
    Label(text="  ").grid(row=7, column=0, columnspan=2)
    Button(text="Show Frame", command=lambda: save_frame((frame_num.get()), img_name.get()).grid(row=8, column=0, columnspan=2))
    gui.mainloop()

# MAIN:
set_gui()


