from enum import Enum

"""
    FURB - Bacharelado em Ciências da Computação
    Inteligência Artificial
    Atividade Avaliativa: APA
    Exercício 01

    Adriner Maranho de Andrade, Fábio Luiz Fischer, Jordy Felipe da Silva
"""


class TipoAcao(Enum):
    acima = 0
    abaixo = 1
    esquerda = 2
    direita = 3
    aspirar = 4
