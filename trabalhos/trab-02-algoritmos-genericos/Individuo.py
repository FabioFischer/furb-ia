from Cromossomo import Cromossomo

class Individuo():
    def __init__(self, cenario, estado_inicial, estado_objetivo, pai_01=None, pai_02=None):
        self.cromossomo = Cromossomo(cenario, estado_inicial, estado_objetivo, pai_01, pai_02)

"""
    def distancia(cidade_01, cidade_02):
        return math.sqrt((cidade_01.x - cidade_02.x) ** 2 + (cidade_01.y - cidade_02.y) ** 2)

    def constroi_distancias(cidades):
        return [[distancia(cidades[i], cidades[j]) for j in range(len(cidades))] for i in range(len(cidades))]

    def funcao_aptidao(self):
        identidade

        return
"""
