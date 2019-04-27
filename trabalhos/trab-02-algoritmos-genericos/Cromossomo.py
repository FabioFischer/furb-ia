from random import randint
from copy import deepcopy


class Cromossomo:
    def __init__(self, cenario, estado_inicial, estado_objetivo, prob_mutacao, genes=None):
        self.genes = genes if genes is not None else self.genes_aleatorios(cenario, estado_inicial, estado_objetivo)
        self.verifica_mutacao(prob_mutacao)

    def genes_aleatorios(self, cenario, estado_inicial, estado_objetivo):
        # constrói o caminho de forma aleatória
        caminho = [None for i in range(len(cenario.cidades)+1)]
        for i in range(len(cenario.cidades)+1):
            if i == 0:
                caminho[i] = estado_inicial
            elif i == len(cenario.cidades):
                caminho[i] = estado_objetivo
            else:
                cidades_pendentes = [i for i in cenario.cidades if i not in caminho]
                caminho[i] = cidades_pendentes[randint(0, randint(0, len(cidades_pendentes)-1))]
        return caminho

    def reproduzir(self, other):
        index = randint(1, len(self.genes)-1)
        return self.conflitos_geneticos(self.recombinacao(deepcopy(self.genes), deepcopy(other.genes), index), [index])

    def recombinacao(self, g1, g2, index):
        aux = g1[index]
        g1[index] = g2[index]
        g2[index] = aux
        return g1, g2

    def conflitos_geneticos(self, genes, historico):
        g1, g2 = genes
        d1 = self.index_duplicado(g1[0:len(g1)-1], historico)
        d2 = self.index_duplicado(g2[0:len(g1)-1], historico)
        if d1 is None and d2 is None:
            return g1, g2
        if d1 is not None:
            historico.append(d1)
            return self.conflitos_geneticos(self.recombinacao(g1, g2, d1), historico)
        historico.append(d2)
        return self.conflitos_geneticos(self.recombinacao(g1, g2, d2), historico)

    def index_duplicado(self, genes, historico):
        visitados = {}
        for i in range(len(genes)):
            if genes[i].id not in visitados:
                visitados[genes[i].id] = 1
            else:
                if visitados[genes[i].id] == 1 and i not in historico:
                    return i
                visitados[genes[i].id] += 1
        return None

    def verifica_mutacao(self, prob_mutacao):
        if randint(0, 10000) <= prob_mutacao * 100:
            print("MUTAÇÂO!!", self.genes)
            i, j = randint(1, len(self.genes) - 1), randint(1, len(self.genes) - 1)
            aux = self.genes[i]
            self.genes[i] = self.genes[j]
            self.genes[j] = aux
            print("RESULTADO DA MUTAÇÂO: ", self.genes)

