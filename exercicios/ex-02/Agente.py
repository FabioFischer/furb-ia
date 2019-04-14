
from Mapeador import Mapeador
from TipoAcao import TipoAcao
from TipoRegiao import TipoRegiao
from TipoOrientacao import TipoOrientacao

"""
    FURB - Bacharelado em Ciências da Computação
    Inteligência Artificial
    Atividade Avaliativa: APA
    Exercício 02

    Adriner Maranho de Andrade, Fábio Luiz Fischer, Jordy Felipe da Silva
"""


class Agente:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mapeador = Mapeador(self)
        self.objetivo = None

    def busca_objetivo(self, mapa):
        self.objetivo = self.mapeador.busca_objetivo(mapa)

    def executa_objetivo(self, mapa):
        if mapa[self.x][self.y] == TipoRegiao.sujo.value:
            return TipoAcao.aspirar
        orientacao = self.objetivo.rota.get()
        if orientacao == TipoOrientacao.direita:
            return TipoAcao.direita
        elif orientacao == TipoOrientacao.esquerda:
            return TipoAcao.esquerda
        elif orientacao == TipoOrientacao.acima:
            return TipoAcao.acima
        elif orientacao == TipoOrientacao.abaixo:
            return TipoAcao.abaixo

    def executa_acao(self, mapa, acao):
        if acao == TipoAcao.acima:
            if self.x > 1:
                self.x -= 1
        elif acao == TipoAcao.abaixo:
            if self.x < (len(mapa) - 1):
                self.x += 1
        elif acao == TipoAcao.esquerda:
            if self.y > 1:
                self.y -= 1
        elif acao == TipoAcao.direita:
            if self.y < (len(mapa) - 1):
                self.y += 1
        elif acao == TipoAcao.aspirar:
            mapa[self.x][self.y] = TipoRegiao.limpo.value
            self.objetivo = None
