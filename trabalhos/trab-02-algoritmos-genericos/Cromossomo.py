from random import randint
from copy import deepcopy
import collections


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
        return self.conflitos_geneticos(self.recombinacao(deepcopy(self.genes), deepcopy(other.genes), randint(1, len(self.genes)-1)))

    def recombinacao(self, g1, g2, index):
        print(g1, " ---- ",  g2)
        print(index)
        aux = g1[index]
        g1[index] = g2[index]
        g2[index] = aux
        return g1, g2

    def conflitos_geneticos(self, genes):
        g1, g2 = genes

        print(g1, " ---- ",  g2)

        s1 = self.genes_duplicados(g1[0:len(g1)-1])
        s2 = self.genes_duplicados(g2[0:len(g1)-1])

        print(s1, " ---- ",  s2)

        if len(s1) == 0 and len(s2) == 0:
            return g1, g2

        if len(s1) > 0:
            return self.conflitos_geneticos(self.recombinacao(g1, g2, g1.index(s1[0])))
        return self.conflitos_geneticos(self.recombinacao(g1, g2, g2.index(s2[0])))

    def genes_duplicados(self, genes):
        visitados = {}
        duplicados = []
        for x in genes:
            if x.id not in visitados:
                visitados[x.id] = 1
            else:
                if visitados[x.id] == 1:
                    duplicados.append(x)
                visitados[x.id] += 1
        return duplicados

    def verifica_mutacao(self, prob_mutacao):
        if randint(0, 10000) <= prob_mutacao * 100:
            print("Realiza mutação")
            i, j = randint(1, len(self.genes) - 1), randint(1, len(self.genes) - 1)
            aux = self.genes[i]
            self.genes[i] = self.genes[j]
            self.genes[j] = aux
