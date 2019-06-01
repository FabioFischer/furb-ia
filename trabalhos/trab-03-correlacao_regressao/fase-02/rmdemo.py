import csv
import math
import os.path
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class DataSet:
    def __init__(self, id, x, y):
        self.id = id
        self.x = np.array(x)
        self.y = np.array(y)
        self.x_trans = self.x.transpose()


class RegressaoLinearMultipla:
    def __init__(self, dataset):
        self.dataset = dataset

# Realiza leitura do arquivo e parsing dos valores para float
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "data.csv")) as file:
    raw_data = csv.reader(file, delimiter=',')
    data = [[float(elem) for elem in row] for row in raw_data]

if data is not None:
    # Divide as colunas da matriz bruta de forma que as colunas 1 e 2 sejam as variaveis independentes (x)
    # e a coluna 3 sejam as variaveis dependentes
    ds = DataSet('Dataset 1', [[row[0], row[1]] for row in data], [row[2] for row in data])
    
    rlm = RegressaoLinearMultipla(ds)
    # Imprime os pontos do dataset
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot([row[0] for row in ds.x], [row[1] for row in ds.x], ds.y)
    ax.set_xlabel('Tamanho da Casa')
    ax.set_ylabel('Qtde Quartos')
    ax.set_zlabel('Preço')
    plt.show()
else:
    print('Erro ao ler arquivo')


