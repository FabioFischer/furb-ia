from queue import Queue

from TipoAcao import TipoAcao
from TipoOrientacao import TipoOrientacao


class Mapeador:
    def __init__(self, mapa, agente):
        self.mapa = mapa
        self.agente = agente
        self.fila = self.define_mapeamento()
        self.orientacao_inicial = TipoOrientacao.direita

    def define_mapeamento(self):
        fila = Queue()

        fila.put(TipoOrientacao.direita)
        fila.put(TipoOrientacao.direita)
        fila.put(TipoOrientacao.direita)
        fila.put(TipoOrientacao.baixo)
        fila.put(TipoOrientacao.esquerda)
        fila.put(TipoOrientacao.esquerda)
        fila.put(TipoOrientacao.esquerda)
        fila.put(TipoOrientacao.baixo)
        fila.put(TipoOrientacao.direita)
        fila.put(TipoOrientacao.direita)
        fila.put(TipoOrientacao.direita)
        fila.put(TipoOrientacao.baixo)
        fila.put(TipoOrientacao.esquerda)
        fila.put(TipoOrientacao.esquerda)
        fila.put(TipoOrientacao.esquerda)
        fila.put(TipoOrientacao.cima)
        fila.put(TipoOrientacao.cima)
        fila.put(TipoOrientacao.cima)

        return fila

    def define_acao(self):
        orientacao = self.fila.get()
        if orientacao == TipoOrientacao.direita:
            return TipoAcao.direita
        elif orientacao == TipoOrientacao.esquerda:
            return TipoAcao.esquerda
        elif orientacao == TipoOrientacao.cima:
            return TipoAcao.acima
        elif orientacao == TipoOrientacao.baixo:
            return TipoAcao.abaixo