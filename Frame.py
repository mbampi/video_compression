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


class Frame:

    def __init__(self):
        self.matrixY = np.empty((240, 416), int)
        self.matrixCb = np.empty((120, 208), int)
        self.matrixCr = np.empty((120, 208), int)
        self.video = None

# Imprime o Frame em numeros (Bytes, que equivalem a cor)
    def to_string(self):
        for line in range(0, 240):
            print("\n")
            for column in range(0, 416):
                print(self.matrixY[line, column]),
        print("\n\n\n\n\n")
        '''for line in range(0, 120):
            print("\n")
            for column in range(0, 208):
                print(self.matrixCb[line, column]),
                print(self.matrixCr[line, column]),'''

# Cria um dicionario com repeticoes ocorridas em uma matriz
    def repetition_counter(self):
        count_dict = {}
        for x in range(0, 256):
            count_dict[x] = np.sum(self.matrixY == x)
        return count_dict

# Cria um Frame de Matrizes (a partir do numero do frame)
    def create_matrix(self, frame_num):
        self.video = open("videos/BQSquare_416x240_60.yuv", 'rb')
        char_num = (frame_num * ((240*416)+(120*208)+(120*208)))
        self.video.seek(char_num, 0)
        self.create_matrix_y()
        self.create_matrix_cb()
        self.create_matrix_cr()
        self.video.close()

# Cria um Frame de Matrizes Otimizadas (a partir de 2 frames)
    def create_optimized_matrix(self, frame1, frame2):
        self.create_optimized_matrix_y(frame1, frame2)
        self.create_optimized_matrix_cb(frame1, frame2)
        self.create_optimized_matrix_cr(frame1, frame2)


# Chamados pelo create_matrix()
    def create_matrix_y(self):
        for line in range(0, 240):
            for column in range(0, 416):
                byte = self.video.read(1)
                byte_to_int = struct.unpack('B', byte)[0]
                self.matrixY[line, column] = byte_to_int

    def create_matrix_cb(self):
        for line in range(0, 120):
            for column in range(0, 208):
                byte = self.video.read(1)
                byte_to_int = struct.unpack('B', byte)[0]
                self.matrixCb[line, column] = byte_to_int

    def create_matrix_cr(self):
        for line in range(0, 120):
            for column in range(0, 208):
                byte = self.video.read(1)
                byte_to_int = struct.unpack('B', byte)[0]
                self.matrixCr[line, column] = byte_to_int


# Chamados pelo create_optimized_matrix()
    def create_optimized_matrix_y(self, frame1, frame2):
        for line in range(0, 240):
            for column in range(0, 416):
                self.matrixY[line, column] = 255 - abs(frame1.matrixY[line, column] - frame2.matrixY[line, column])

    def create_optimized_matrix_cb(self, frame1, frame2):
        for line in range(0, 120):
            for column in range(0, 208):
                if frame1.matrixCb[line, column] == frame2.matrixCb[line, column]:
                    self.matrixCb[line, column] = 0
                else:
                    self.matrixCb[line, column] = frame2.matrixCb[line, column]

    def create_optimized_matrix_cr(self, frame1, frame2):
        for line in range(0, 120):
            for column in range(0, 208):
                if frame1.matrixCr[line, column] == frame2.matrixCr[line, column]:
                    self.matrixCr[line, column] = 0
                else:
                    self.matrixCr[line, column] = frame2.matrixCr[line, column]

'''
#No def create_optimized_matrix_y()

 if frame1.matrixY[line, column] == frame2.matrixY[line, column]:
 self.matrixY[line, column] = 0
 else:
    self.matrixY[line, column] = frame2.matrixY[line, column]
'''
'''if abs(frame1.matrixY[line, column] - frame2.matrixY[line, column]) < 10:
                    self.matrixY[line, column] = 0
                else:
                    self.matrixY[line, column] = 255'''