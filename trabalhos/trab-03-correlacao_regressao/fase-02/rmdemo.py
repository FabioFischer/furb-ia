import csv
import math
import os.path
import operator
import numpy as np
import matplotlib.pyplot as plt
from functools import reduce
from mpl_toolkits.mplot3d import Axes3D


class DataSet:
    def __init__(self, id, x, y):
        self.id = id
        self.x = np.array(x)
        self.y = np.array(y)
        self.x_trans = self.x.transpose()

    @staticmethod
    def mediana(arr):
        sum = reduce(operator.add, arr)
        return sum / len(arr)


class RegressaoLinearMultipla:
    def __init__(self, dataset):
        self.dataset = dataset
        
    def regmultipla(self):
        # (Xt X)-¹ Xt y
        transp_x = self.dataset.x.transpose()
        return np.linalg.inv(transp_x.dot(self.dataset.x)).dot(transp_x).dot(self.dataset.y)

    def correlacao_simples(self, dimensao):
        # Calcula mediana dos vetores
        x = self.dataset.x[:,dimensao]
        med_x = DataSet.mediana(x)
        med_y = DataSet.mediana(self.dataset.y)
        # Σ(x−x̄)(y−ȳ)
        dividend = 0
        for i in range(len(x)):
            dividend += (x[i] - med_x) * (self.dataset.y[i] - med_y)

        # Σ(arr−arr̄)²
        def soma_linear(dataset, mediana):
            sum = 0
            for elem in dataset:
                sum += (elem - mediana) ** 2
            return sum

        # (Σ(x−x̄)(y−ȳ)) / √(Σ(x−x̄)² Σ(y−ȳ)²)
        return dividend / (math.sqrt(
            soma_linear(x, med_x) * soma_linear(self.dataset.y, med_y)))

    def regressao_simples(self, dimensao):
        # Calcula mediana dos vetores
        x = self.dataset.x[:,dimensao]
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

    @staticmethod
    def reta_regressao_simples(b0, b1, x):
        # 𝑦̂=𝛽0+𝛽1x
        return b0 + (b1 * x)

    @staticmethod
    def reta_regressao_multipla(b, x):
        # 𝑦̂= X*𝛽
        return np.array(x).dot(b)


# Realiza leitura do arquivo e parsing dos valores para float
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "data.csv")) as file:
    raw_data = csv.reader(file, delimiter=',')
    data = np.array([[float(elem) for elem in row] for row in raw_data])

if data is not None:
    # Divide as colunas da matriz bruta de forma que as colunas 1 e 2 sejam as variaveis independentes (x)
    # e a coluna 3 sejam as variaveis dependentes
    ds = DataSet('Dataset 1', data[:,0:2], data[:,2])

    rlm = RegressaoLinearMultipla(ds)

    x0_corr = rlm.correlacao_simples(0)
    x0_b0, x0_b1 = rlm.regressao_simples(0)

    fig = plt.figure('Regressão entre o Tamanho da Casa e o Preço')
    plt.title("r: %s, β0: %s, β1: %s)" % (x0_corr, x0_b0, x0_b1))
    plt.grid(True)
    plt.scatter(ds.x[:, 0], ds.y)
    x_prev = np.linspace(0, 5000, num=100)
    y_prev = [RegressaoLinearMultipla.reta_regressao_simples(x0_b0, x0_b1, x) for x in x_prev]
    plt.scatter(x_prev, y_prev, alpha=0.2, facecolor='red')
    plt.xlabel('Tamanho da Casa')
    plt.ylabel('Preço')
    plt.show()

    x1_corr = rlm.correlacao_simples(1)
    x1_b0, x1_b1 = rlm.regressao_simples(1)

    fig = plt.figure('Regressão entre a Número de Quartos e o Preço')
    plt.title("r: %s, β0: %s, β1: %s)" % (x1_corr, x1_b0, x1_b1))
    plt.grid(True)
    plt.scatter(ds.x[:, 1], ds.y)
    x_prev = np.linspace(0, 10, num=50)
    y_prev = [RegressaoLinearMultipla.reta_regressao_simples(x1_b0, x1_b1, x) for x in x_prev]
    plt.scatter(x_prev, y_prev, alpha=0.2, facecolor='red')
    plt.xlabel('Número de Quartos')
    plt.ylabel('Preço')
    plt.show()

    b = rlm.regmultipla()
    regressao_multipla = RegressaoLinearMultipla.reta_regressao_multipla(b, ds.x)

    fig = plt.figure('Linha da regressão no Gráfico de Dispersão 3D')
    ax = fig.gca(projection='3d')
    ax.plot(ds.x[:, 0], ds.x[:, 1], ds.y)
    ax.plot(ds.x[:, 0], ds.x[:, 1], regressao_multipla, c=[1, 0, 0, 0.5])
    ax.set_xlabel('Tamanho da Casa')
    ax.set_ylabel('Qtde Quartos')
    ax.set_zlabel('Preço')
    plt.show()

    print('Preço de uma casa de tamanho 1650 e 3 quartos: ', RegressaoLinearMultipla.reta_regressao_multipla(b, [1650, 3]))

else:
    print('Erro ao ler arquivo')


