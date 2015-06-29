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
from Tkinter import *
import Image as Im
from collections import Counter
from BinaryTree import ArvoreBinaria
from Frame import Frame


def create_frames():
    for x in range(0, 11):
        f = Frame()
        f.create_matrix(x)
        frames.append(f)

def create_optimized_frames():
    for x in range(0, 10):
        f = Frame()
        f.create_optimized_matrix(frames[x], frames[x+1])
        optimized_frames.append(f)

video = open("videos/BQSquare_416x240_60.yuv", 'rb')
video.seek(0, 2)
video_size = video.tell()
video_frames = video_size/((240*416)+(120*208)+(120*208))
video_time = video_frames/30

frames = []
optimized_frames = []
create_frames()
create_optimized_frames()
repetition_count = optimized_frames[0].repetition_counter()
# repetition_count = Counter(repetition_count).most_common()
print repetition_count



'''
grey = optimized_frames[0].matrixY.astype('uint8')
greyIm = Im.fromarray(grey, "L")
greyIm.save("saved_img/" + "frameOpt0" + ".bmp")
grey = optimized_frames[4].matrixY.astype('uint8')
greyIm = Im.fromarray(grey, "L")
greyIm.save("saved_img/" + "frameOpt1" + ".bmp")
grey = optimized_frames[7].matrixY.astype('uint8')
greyIm = Im.fromarray(grey, "L")
greyIm.save("saved_img/" + "frameOpt2" + ".bmp")
grey = optimized_frames[9].matrixY.astype('uint8')
greyIm = Im.fromarray(grey, "L")
greyIm.save("saved_img/" + "frameOpt3" + ".bmp")
'''