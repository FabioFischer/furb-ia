from queue import Queue
from TipoOrientacao import TipoOrientacao

"""
    FURB - Bacharelado em Ciências da Computação
    Inteligência Artificial
    Atividade Avaliativa: APA
    Exercício 02

    Adriner Maranho de Andrade, Fábio Luiz Fischer, Jordy Felipe da Silva
"""


class Objetivo:
    def __init__(self, agente, x, y):
        self.x = x
        self.y = y
        self.custo = abs(agente.x - self.x) + abs(agente.y - self.y)
        self.rota = self.define_rota(agente)

    # Define a rota para que o agente alcance o objetivo de acordo a diferença horizontal e vertical entre ambos
    # Não considera obstaculos
    def define_rota(self, agente):
        rota = Queue()
        for i in range(abs(agente.x - self.x)):
            rota.put(TipoOrientacao.acima if agente.x - self.x > 0 else TipoOrientacao.abaixo)
        for i in range(abs(agente.y - self.y)):
            rota.put(TipoOrientacao.esquerda if agente.y - self.y > 0 else TipoOrientacao.direita)
        return rota
