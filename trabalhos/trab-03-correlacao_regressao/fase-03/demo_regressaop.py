import csv
import math
import os.path
import operator
import numpy as np
import matplotlib.pyplot as plt
from functools import reduce
from mpl_toolkits.mplot3d import Axes3D


"""
    FURB - Bacharelado em Ciências da Computação
    Inteligência Artificial
    Trabalho 03 - Fase 03 - Regressão Polinomial - Overfitting
    Equipe: Adriner Maranho de Andrade, Fábio Luiz Fischer, Felipe Anselmo dos Santos, Jorge Guilherme Kohn

    Faça um script demo_regressaop que faz o seguinte:
        a) Baixe o arquivo data_preg.mat ou data_preg.svg. A primeira coluna representa os valores de x e a segunda coluna representa os valores de y.
        b) Faça o Gráfico de dispersão dos dados.
        c) Use a função polyfit para gerar a linha de regressão para N = 1 e trace-o no gráfico de dispersão na cor vermelha (plot (x, y, 'r')). (observe que nesta função a numeração coeficiente é invertida! β0=βN, β1=βN−1, β2=βN−2 , ...βN=β0)
        d) Trace a linha de regressão para N = 2 no gráfico na cor verde.
        e) Trace a linha de regressão para N = 3 no gráfico na cor preta.
        f) Trace a linha de regressão para N = 8 no gráfico na cor amarela.
        g) Calcule o Erro Quadrático Médio (EQM) para cada linha de regressão. Qual é o mais preciso?
        h) Para evitar o overfitting, divida os dados aleatoriamente em Dados de Treinamento e Dados de Teste. Use os primeiros 10% dos dados como conjunto de teste, e o resto como de treinamento.
        i) Repita os passos de c - f, mas agora use apenas os dados de treinamento para ajustar a linha de regressão.
        J) Repita o passo g, mas agora utilize somente os dados de Teste para calcular o erro.
        k) Que método é o mais preciso neste caso?
"""


def strnum(x):
    return round(x, 2)


class DataSet:
    def __init__(self, id, x, y):
        self.id = id
        self.x = np.array(x)
        self.y = np.array(y)
        self.x_trans = self.x.transpose()
        self.y_trans = self.y.transpose()

    @staticmethod
    def mediana(arr):
        sum = reduce(operator.add, arr)
        return sum / len(arr)


class RegressaoLinearMultipla:
    def __init__(self, dataset):
        self.dataset = dataset

    def regmultipla(self):
        # 𝛽 = (Xt X)-1 Xty
        transp_x = self.dataset.x.transpose()
        return np.linalg.inv(transp_x.dot(self.dataset.x)).dot(transp_x.dot(self.dataset.y))

    def correlacao(self, dimensao):
        # Calcula mediana dos vetores
        x = self.dataset.x[:, dimensao + 1]
        med_x = DataSet.mediana(x)
        med_y = DataSet.mediana(self.dataset.y)
        # Σ(x−x̄)(y−ȳ)
        dividend = 0
        for i in range(len(x)):
            dividend += (x[i] - med_x) * (self.dataset.y[i] - med_y)

        # Σ(ds−ds̄)²
        def soma_linear(dataset, mediana):
            sum = 0
            for elem in dataset:
                sum += (elem - mediana) ** 2
            return sum
        # r = Σ(x−x̄)(y−ȳ) / √(Σ(x−x̄)² Σ(y−ȳ)²)
        return dividend / (math.sqrt(
            soma_linear(x, med_x) * soma_linear(self.dataset.y, med_y)))

    def regressao(self, dimensao):
        # Calcula mediana dos vetores
        x = self.dataset.x[:, dimensao + 1]
        med_x = DataSet.mediana(x)
        med_y = DataSet.mediana(self.dataset.y)
        # Σ(x−x̄)(y−ȳ)
        dividend = 0
        for i in range(len(self.dataset.x)):
            dividend += (x[i] - med_x) * (self.dataset.y[i] - med_y)
        # Σ(x−x̄)²
        divisor = 0
        for elem in x:
            divisor += (elem - med_x) ** 2
        # 𝛽1 = Σ(x−x̄)(y−ȳ) / Σ(x−x̄)²
        b1 = dividend / divisor
        # 𝛽0 = 𝑦̄− β1x,
        return med_y - (b1 * med_x), b1

    def reta_regressao(self, b0, b1, dimensao):
        x = self.dataset.x[:, dimensao + 1]
        # 𝑦̂=𝛽0+𝛽1x
        return b0 + (b1 * x)

    def reta_regressao_multipla(self, b, x=None):
        # 𝑦̂= X*𝛽
        if x is None:
            return self.dataset.x.dot(b)
        return np.array(x).dot(b)


# Realiza leitura do arquivo e parsing dos valores para float
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "data.csv")) as file:
    raw_data = csv.reader(file, delimiter=',')
    data = [[float(elem) for elem in row] for row in raw_data]

if data is not None:
    # Divide as colunas da matriz bruta de forma que as colunas 1 e 2 sejam as variaveis independentes (x) e a coluna 3 sejam as variaveis dependentes
    # Por convenção, as variáveis independentes devem possuir uma coluna preenchida com o número 1
    ds = DataSet('Dataset 1', [[1, elem[0], elem[1]] for elem in data], [elem[2] for elem in data])
    rlm = RegressaoLinearMultipla(ds)

    # Verificar a correlação e a regressão para Tamanho da casa e Preço e gerar o gráfico de dispersão
    x0 = ds.x[:, 1]
    x0_corr = rlm.correlacao(0)
    x0_b0, x0_b1 = rlm.regressao(0)
    x0_regressao = rlm.reta_regressao(x0_b0, x0_b1, 0)
    fig = plt.figure('Regressão entre o Tamanho da Casa e o Preço')
    plt.title("r: %s    β0: %s    β1: %s" % (strnum(x0_corr), strnum(x0_b0), strnum(x0_b1)))
    plt.grid(True)
    plt.scatter(x0, ds.y)
    plt.plot(x0, x0_regressao, c=[1, 0, 0, 0.5])
    plt.xlabel('Tamanho da Casa')
    plt.ylabel('Preço')
    plt.show()

    # Verificar a correlação e a regressão para Número de Quartos e Preço e gerar o gráfico de dispersão
    x1 = ds.x[:, 2]
    x1_corr = rlm.correlacao(1)
    x1_b0, x1_b1 = rlm.regressao(1)
    x1_regressao = rlm.reta_regressao(x1_b0, x1_b1, 1)
    fig = plt.figure('Regressão entre a NÃºmero de Quartos e o Preço')
    plt.title("r: %s    β0: %s    β1: %s" % (strnum(x1_corr), strnum(x1_b0), strnum(x1_b1)))
    plt.grid(True)
    plt.scatter(x1, ds.y)
    plt.plot(x1, x1_regressao, c=[1, 0, 0, 0.5])
    plt.xlabel('Número de Quartos')
    plt.ylabel('Preço')
    plt.show()

    # Cria o gráfico de dispersão em 3D com o tamanho da casa, número de quartos, e o preço da casa
    # Gera a linha de regressão para as 3 dimensões
    b = rlm.regmultipla()
    regressao_multipla = rlm.reta_regressao_multipla(b)
    fig = plt.figure('Linha da regressão no Gráfico de Dispersão 3D')
    ax = fig.gca(projection='3d')
    ax.scatter(ds.x[:, 1], ds.x[:, 2], ds.y)
    ax.plot(ds.x[:, 1], ds.x[:, 2], regressao_multipla, c=[1, 0, 0, 0.5])
    ax.set_xlabel('Tamanho da Casa')
    ax.set_ylabel('Qtde Quartos')
    ax.set_zlabel('Preço')

    # Calcule o preço de uma casa que tem tamanho de 1650 e 3 quartos. O resultado deve ser igual a 293081
    print('Preço de uma casa de tamanho 1650 e 3 quartos: ', strnum(rlm.reta_regressao_multipla(b, [1, 1650, 3])))
    plt.show()

else:
    print('Erro ao ler arquivo')


