import math
import operator
from functools import reduce
import matplotlib.pyplot as plt
import numpy as np


"""
    FURB - Bacharelado em Ciências da Computação
    Inteligência Artificial
    Trabalho 03 - Fase 01 - Análise de Regressão e Correlação Linear
    Equipe: Adriner Maranho de Andrade, Fábio Luiz Fischer, Felipe Anselmo dos Santos, Jorge Guilherme Kohn

    1) Implemente duas funções chamadas correlacao e regressao. Cada uma deve ter dois vetores Nx1 como entrada, onde N é a dimensão do vetor (no caso de x N=11).
    A primeira função deve calcular o coeficiente de correlação r, e a segunda função deve calcular a regressão, isto é, β0 e β1.

    2) Faça um script no Python chamado demo onde para cada dataset faça os seguintes comandos:
      a. Faça um Gráfico de Dispersão (veja função scatter).
      b. Calcule o coeficiente de correlação.
      c. Trace a linha da regressão no Gráfico de Dispersão (veja a função plot)
      d. Mostre os coeficientes de correlação e regressão no Gráfico de Dispersão (utilize a função title)

    3) Qual dos datasets não é apropriado para regressão linear?
    Resposta: 2 ou 3 pois os dados não estão dsitribuídos em uma prograssão linear
"""


def strnum(x):
    return round(x, 2)


class DataSet:
    def __init__(self, id, x, y):
        self.id = id
        self.x = np.array(x)
        self.y = np.array(y)
        self.med_x = self.mediana(self.x)
        self.med_y = self.mediana(self.y)

    def mediana(self, arr):
        sum = reduce(operator.add, arr)
        return sum / len(arr)


class CorrelacaoRegressaoLinear:
    def __init__(self, dataset):
        self.dataset = dataset
        self.r = self.correlacao()
        self.b0, self.b1 = self.regressao()

    def correlacao(self):
        # Σ(x−x̄)(y−ȳ)
        dividend = 0
        for i in range(len(self.dataset.x)):
            dividend += (self.dataset.x[i] - self.dataset.med_x) * (self.dataset.y[i] - self.dataset.med_y)

        # Σ(arr−arr̄)²
        def soma_linear(dataset, mediana):
            sum = 0
            for elem in dataset:
                sum += (elem - mediana) ** 2
            return sum

        # (Σ(x−x̄)(y−ȳ)) / √(Σ(x−x̄)² Σ(y−ȳ)²)
        return dividend / (math.sqrt(
            soma_linear(self.dataset.x, self.dataset.med_x) * soma_linear(self.dataset.y, self.dataset.med_y)))

    def regressao(self):
        # Σ(x−x̄)(y−ȳ)
        dividend = 0
        for i in range(len(self.dataset.x)):
            dividend += (self.dataset.x[i] - self.dataset.med_x) * (self.dataset.y[i] - self.dataset.med_y)
        # Σ(x−x̄)²
        divisor = 0
        for elem in self.dataset.x:
            divisor += (elem - self.dataset.med_x) ** 2
        # 𝛽1 = Σ(x−x̄)(y−ȳ) / Σ(x−x̄)²
        b1 = dividend / divisor
        # 𝛽0 = 𝑦̄− β1x,
        return self.dataset.med_y - (b1 * self.dataset.med_x), b1

    def reta_regressao(self, x):
        # 𝑦̂=𝛽0+𝛽1x
        return self.b0 + (self.b1 * x)


# Datasets de teste
dss = [DataSet('Dataset 1', [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5], [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]),
       DataSet('Dataset 2', [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5], [9.14, 8.14, 8.47, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]),
       DataSet('Dataset 3', [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 19], [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 5.56, 7.91, 6.89, 12.50])]

for ds in dss:
    # Calcula a correlação e a regressão para o dataset
    crl = CorrelacaoRegressaoLinear(ds)

    fig = plt.figure(ds.id)
    plt.title("r: %s    β0: %s    β1: %s" % (strnum(crl.r), strnum(crl.b0), strnum(crl.b1)))
    plt.grid(True)
    # Marca os pontos do dataset
    plt.scatter(ds.x, ds.y)
    # Merca os pontos da regressão linear
    plt.plot(ds.x, crl.reta_regressao(ds.x), c=[1, 0, 0, 0.5])

    plt.show()
