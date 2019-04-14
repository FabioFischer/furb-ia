
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
        self.objetivo = None
        self.contador = 0

    # Função responsável por retornar a próxima ação do agente de acordo com a situação atual do mapa
    # obj_obtido será 1 quando houver objetivos disponíveis no mapa
    def agente_objetivo(self, mapa, obj_obtido):
        if obj_obtido == 1:
            # Sempre que uma região é limpa, o objetivo atual do agente deixa de existir.
            if self.objetivo is None:
                # Busca um objetivo
                self.busca_objetivo(mapa)
            if self.objetivo is not None:
                # Se o objetivo foi encontrado, executa a fila de ações necessárias para alcançar a região objetivo
                return self.executa_objetivo(mapa)
        return TipoAcao.NoOp

    # Busca o objetivo mais próximo do agente
    # Os objetivos terão seu custo e sua rota calculada em sua inicialização
    def busca_objetivo(self, mapa):
        self.objetivo = Mapeador.busca_objetivo(self, mapa)

    # Consome a fila de alções necessárias para alcançar o objetivo
    # Caso a região atual do agente esteja suja, a ação aspirar será retornada
    # Um contador será incrementado sempre que o agente se deslocar
    def executa_objetivo(self, mapa):
        if mapa[self.x][self.y] == TipoRegiao.sujo.value:
            return TipoAcao.aspirar
        orientacao = self.objetivo.rota.get()
        self.contador += 1
        print("Contador", self.contador)
        if orientacao == TipoOrientacao.direita:
            return TipoAcao.direita
        elif orientacao == TipoOrientacao.esquerda:
            return TipoAcao.esquerda
        elif orientacao == TipoOrientacao.acima:
            return TipoAcao.acima
        elif orientacao == TipoOrientacao.abaixo:
            return TipoAcao.abaixo

    # Executa a ação de entrada da função
    # Caso a ação seja aspirar, o objetivo atual do agente deixa de existir
    def executa_acao(self, acao, mapa):
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
