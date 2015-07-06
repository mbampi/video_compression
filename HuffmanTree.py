from operator import attrgetter

class Nodo:

    def __init__(self):
        self.item = None
        self.rep = None
        self.esq = None
        self.dir = None


class ArvoreHuffman:

    # Recebe dicionario e atribui a Nodos
    def __init__(self, dicionario):
        self.raiz = None
        self.num = 0
        self.i = 0
        self.vetor = []
        self.dicio = {}
        x = 0
        while x < len(dicionario):
            new_nodo = Nodo()
            new_nodo.item = dicionario.keys()[x]
            new_nodo.rep = dicionario.values()[x]
            self.vetor.append(new_nodo)
            x += 1

# Faz arvore de Huffman baseada no dicionario
    def create_tree(self):
        while len(self.vetor) > 1:
            self.vetor.sort(key=attrgetter('rep'), reverse=True)
            new_nodo = Nodo()
            new_nodo.rep = self.vetor[-1].rep + self.vetor[-2].rep
            new_nodo.esq = self.vetor.pop()
            new_nodo.dir = self.vetor.pop()
            self.vetor.append(new_nodo)
        self.raiz = self.vetor.pop()

    def generate_binary(self):
        binary = ''
        return self.generate_binary_rec(self.raiz, binary)

    def generate_binary_rec(self, nodo, binary):
        if nodo.esq is not None:
            self.generate_binary_rec(nodo.esq, (binary+'0'))
        if nodo.dir is not None:
            self.generate_binary_rec(nodo.dir, (binary+'1'))
        if nodo.esq is None and nodo.dir is None:
            self.dicio[nodo.item] = binary
            return

    def gera_codigo(self):
        self.generate_binary()
        print(self.dicio)
