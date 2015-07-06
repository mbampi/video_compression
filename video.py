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


video = open("BQSquare_416x240_60.yuv", 'rb')

# imprime numero de characteres
video.seek(0, 2)
size = video.tell()
frames = size/(240*416)+(120*208)+(120*208)
print '\n\n O arquivo contem', size, 'characters'
print '\n O arquivo contem', frames, 'frames'

# Frames
print("\n\n Binary characters: ")
video.seek(0, 0)

# frame Y
print("Frame Y")
matrixY = np.empty((240, 416), int)
for line in range(0, 240):
    for column in range(0, 416):
        byte = video.read(1)
        byteToInt = struct.unpack('B', byte)[0]
        matrixY[line, column] = byteToInt

# frame Cb
print("Frame Cb")
matrixCb = np.empty((120, 208), int)
for line in range(0, 120):
    for column in range(0, 208):
        byte = video.read(1)
        byteToInt = struct.unpack('B', byte)[0]
        matrixCb[line, column] = byteToInt

# frame Cr
print("Frame Cr")
matrixCr = np.empty((120, 208), int)
for line in range(0, 120):
    for column in range(0, 208):
        byte = video.read(1)
        byteToInt = struct.unpack('B', byte)[0]
        matrixCr[line, column] = byteToInt

video.close()




'''
                            #Conferir Matriz
file.seek(416, 0)
byte = file.read(1)
byteToInt = struct.unpack('B', byte)[0]
print 'normal= ', byteToInt
'''

'''
                            # Imprimir matriz
for line in range(0, 240):
    for column in range(0, 416):
        print(matrixY[line, column])
'''

'''
                            # Teste Arvore Huffman
dicio = {'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1}
arv = ArvoreHuffman(dicio)
arv.create_tree()
'''

'''
                            # Salva optimized_frames como imagens cinza

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