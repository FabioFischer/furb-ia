import math
import random
from Cidade import Cidade


class Cenario:
    def __init__(self, tamanho):
        # Cidades construídas em posições aleatórias de (0, 0) a (1, 1)
        self.cidades = [Cidade(random.random(), random.random()) for i in range(tamanho)]
        self.matriz_identidade = self.constroi_matriz_identidade()
        print(self.matriz_identidade)

    def constroi_matriz_identidade(self):
        return [[self.distancia_cidades(self.cidades[i], self.cidades[j]) for j in range(len(self.cidades))] for i in range(len(self.cidades))]

    def distancia_cidades(self, cidade_01, cidade_02):
        return math.sqrt((cidade_01.x - cidade_02.x) ** 2 + (cidade_01.y - cidade_02.y) ** 2)
