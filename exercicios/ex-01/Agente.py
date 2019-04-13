
from TipoAcao import TipoAcao
from TipoRegiao import TipoRegiao
from Mapeador import Mapeador

"""
    FURB - Bacharelado em Ciências da Computação
    Inteligência Artificial
    Atividade Avaliativa: APA

    Adriner Maranho de Andrade, Fábio Luiz Fischer, Jordy Felipe da Silva
"""


class Agente:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mapeador = None

    def inicializa_mapeamento(self, mapa):
        self.mapeador = Mapeador(mapa, self)

    def define_acao_mapeamento(self):
        return self.mapeador.define_acao()

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
