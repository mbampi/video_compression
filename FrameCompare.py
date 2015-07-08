"""
 Projeto de Iniciacao Cientifica IFRS - Campus Farroupilha
 Tecnico em Informatica integrado ao Ensino Medio

 PROJETO    Compressao de Video
 AUTOR      Matheus Dussin Bampi
 ORIENTACAO Felipe Sampaio
 INICIO     Maio/2015
"""


from collections import Counter
from HuffmanTree import ArvoreHuffman
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



# MAIN

frames = []
optimized_frames = []
create_frames()
create_optimized_frames()
dictionary = optimized_frames[0].repetition_counter()
'''
f = Frame()
f.create_matrix(0)
dictionary = f.repetition_counter()'''
# repetition_count = Counter(repetition_count).most_common()  # Organiza por valores (>)
print(dictionary)
arv = ArvoreHuffman(dictionary)
arv.create_tree()
arv.gera_codigo()
