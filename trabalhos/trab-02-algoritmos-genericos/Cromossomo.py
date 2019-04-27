from random import randint


class Cromossomo:

    probabilidade_mutacao = 0.05

    def __init__(self, cenario, estado_inicial, estado_objetivo, pai_01, pai_02):
        self.genes = self.define_genes(cenario, estado_inicial, estado_objetivo, pai_01, pai_02)
        self.verifica_mutacao()

    def define_genes(self, cenario, estado_inicial, estado_objetivo, pai_01=None, pai_02=None):
        # Quando nenhum pai é informado, constrói o caminho de forma aleatória
        if pai_01 is None or pai_02 is None:
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
        else:
            print("Processo de recombinação")
            return []

    def verifica_mutacao(self):
        if randint(0, 10000) <= Cromossomo.probabilidade_mutacao * 100:
            print("Realiza mutação")
