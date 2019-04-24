
import random
import math
from Cidade import Cidade


def constroi_cidades(quantidade):
    return [Cidade(random.random(), random.random()) for i in range(quantidade)]

def distancia(cidade_01, cidade_02):
    return math.sqrt((cidade_01.x - cidade_02.x) ** 2 + (cidade_01.y - cidade_02.y) ** 2)

def constroi_distancias(cidades):
    return [[distancia(cidades[i], cidades[j]) for j in range(len(cidades))] for i in range(len(cidades))]

cidades = constroi_cidades(20)

distancias = constroi_distancias(cidades)

print(cidades)
print("")
print(distancias)
