import scipy.io as scipy

"""
    FURB - Bacharelado em Ciências da Computação
    Inteligência Artificial
    Trabalho 04 - D1 - Classificação - KNN
    Equipe: Adriner Maranho de Andrade, Fábio Luiz Fischer, Felipe Anselmo dos Santos, Jorge Guilherme Kohn
"""

mat = scipy.loadmat('grupoDados1.mat')

grupoTest = mat['grupoTest']

print(grupoTest)