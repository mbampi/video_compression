"""
 Projeto de Iniciacao Cientifica IFRS - Campus Farroupilha
 Tecnico em Informatica integrado ao Ensino Medio

 PROJETO    Compressao de Video
 AUTOR      Matheus Dussin Bampi
 ORIENTACAO Felipe Sampaio
 INICIO     Maio/2015
"""
from HuffmanTree import ArvoreHuffman

dicio = {'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1}


'''
                            # Conferir Arvore Huffman Codigos
dicio = {'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1}
arv = ArvoreHuffman(dicio)
arv.create_tree()
arv.gera_codigo()
'''

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

'''
                            # Atribui 0 para valores iguais   (on create_optimized_matrix_y())

 if frame1.matrixY[line, column] == frame2.matrixY[line, column]:
    self.matrixY[line, column] = 0
 else:
    self.matrixY[line, column] = frame2.matrixY[line, column]
'''