

class Nodo:

    def __init__(self):
        self.item = None
        self.rep = None
        self.esq = None
        self.dir = None



class ArvoreBinaria:

    def __init__(self, dicionario):
        self.raiz = None
        self.num = 0
        self.i = 0
        self.vetor = []
        x = 0
        while x < len(dicionario):
            new_nodo = Nodo()
            new_nodo.item = dicionario.keys()[x]
            new_nodo.rep = dicionario.values()[x]
            self.vetor.append(new_nodo)
            x += 1


    def create_tree(self):
        while len(self.vetor) > 1:
            self.vetor.sort()
            new_nodo = Nodo()
            new_nodo.rep = self.vetor[-1].rep + self.vetor[-2].rep
            new_nodo.esq = self.vetor.pop()
            new_nodo.dir = self.vetor.pop()
            self.vetor.append(new_nodo)



dicio = {'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1}
arv = ArvoreBinaria(dicio)
arv.create_tree()
