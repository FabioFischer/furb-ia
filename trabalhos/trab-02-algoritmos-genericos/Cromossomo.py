import math
from random import randint

class Cromossomo:
    def __init__(self, cidades, estado_inicial, estado_objetivo, pai_01, pai_02):
        self.genes = self.define_genes(cidades, estado_inicial, estado_objetivo, pai_01, pai_02)
        self.aptidao = self.define_aptidao()

    def define_genes(self, cidades, estado_inicial, estado_objetivo, pai_01=None, pai_02=None):
        # Quando nenhum pai é informado, constrói o caminho de forma aleatória
        if self.pai_01 is None or pai_02 is None:
            caminho = [None for i in range(len(cidades)+1)]
            for i in range(len(cidades)+1):
                if i == 0:
                    caminho[i] = estado_inicial
                elif i == len(cidades):
                    caminho[i] = estado_objetivo
                else:
                    cidades_pendentes = [i for i in cidades if i not in caminho]
                    caminho[i] = cidades_pendentes[randint(0, randint(0, len(cidades_pendentes)-1))]
            print(caminho)
            return caminho
        else:
            print("Processo de recombinação")
            return []


    def define_aptidao(self):
        return 0
