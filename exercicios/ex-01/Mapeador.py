from queue import Queue

from TipoAcao import TipoAcao
from TipoOrientacao import TipoOrientacao

"""
    FURB - Bacharelado em Ciências da Computação
    Inteligência Artificial
    Atividade Avaliativa: APA

    Adriner Maranho de Andrade, Fábio Luiz Fischer, Jordy Felipe da Silva
"""


class Mapeador:
    def __init__(self, mapa, agente):
        self.mapa = mapa
        self.agente = agente
        self.fila = self.define_mapeamento()

    # Popula a fila de mapeamento de acordo com a altura e comprimento do mapa
    def define_mapeamento(self):
        fila = Queue()
        orientacao_horizontal = TipoOrientacao.direita
        # Percorre o mapa de cima para baixo alternando a orientação horizontal
        for i in range(len(self.mapa) - 3):
            for j in range(len(self.mapa[i]) - 3):
                fila.put(orientacao_horizontal)
            fila.put(TipoOrientacao.abaixo)
            orientacao_horizontal = TipoOrientacao.esquerda \
                if orientacao_horizontal == TipoOrientacao.direita else TipoOrientacao.direita

        # Retorna o agente à posição inicial horizontalmente
        if orientacao_horizontal == TipoOrientacao.esquerda:
            for i in range(len(self.mapa[0]) - 3):
                fila.put(TipoOrientacao.esquerda)
        # Retorna o agente a posição inicial verticalmente
        for i in range(len(self.mapa) - 3):
            fila.put(TipoOrientacao.acima)
        return fila

    # Determina a ação a ser tomada para o próximo movimento da fila de mapeamento
    def define_acao(self):
        orientacao = self.fila.get()
        if orientacao == TipoOrientacao.direita:
            return TipoAcao.direita
        elif orientacao == TipoOrientacao.esquerda:
            return TipoAcao.esquerda
        elif orientacao == TipoOrientacao.acima:
            return TipoAcao.acima
        elif orientacao == TipoOrientacao.abaixo:
            return TipoAcao.abaixo
