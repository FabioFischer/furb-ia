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

    def define_rota(self, agente):
        rota = Queue()
        vertical = agente.x - self.x
        horizontal = agente.y - self.y
        for i in range(abs(vertical)):
            rota.put(TipoOrientacao.acima if vertical > 0 else TipoOrientacao.abaixo)
        for i in range(abs(horizontal)):
            rota.put(TipoOrientacao.esquerda if horizontal > 0 else TipoOrientacao.direita)
        return rota
