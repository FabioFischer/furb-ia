from operator import attrgetter
from Objetivo import Objetivo
from TipoRegiao import TipoRegiao

"""
    FURB - Bacharelado em Ciências da Computação
    Inteligência Artificial
    Atividade Avaliativa: APA
    Exercício 02

    Adriner Maranho de Andrade, Fábio Luiz Fischer, Jordy Felipe da Silva
"""


class Mapeador:
    # Busca o objetivo mais próximo do agente
    # Os objetivos terão seu custo e sua rota calculada em sua inicialização
    @staticmethod
    def busca_objetivo(agente, mapa):
        objetivos = []
        for i in range(len(mapa)):
            for j in range(len(mapa[i])):
                if mapa[i][j] == TipoRegiao.sujo.value:
                    objetivos.append(Objetivo(agente, i, j))
        return min(objetivos, key=attrgetter('custo')) if len(objetivos) > 0 else None
