import csv
import math
import random
import os.path
import operator
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
from functools import reduce


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
            Resposta: A linha de regressão para N=8 é mais precisa para esse cenário pois obteve o menor erro quadrático médio: 0.05870934697361084
        h) Para evitar o overfitting, divida os dados aleatoriamente em Dados de Treinamento e Dados de Teste. Use os primeiros 10% dos dados como conjunto de teste, e o resto como de treinamento.
        i) Repita os passos de c - f, mas agora use apenas os dados de treinamento para ajustar a linha de regressão.
        J) Repita o passo g, mas agora utilize somente os dados de Teste para calcular o erro.
        k) Que método é o mais preciso neste caso?
"""


def strnum(x):
    return round(x, 2)


class DataSet:
    def __init__(self, x, y):
        self.x = np.array(x)
        self.y = np.array(y)
        self.lenght = len(self.x)

class RegressaoPolinomial:
    def __init__(self, dataset):
        self.dataset = dataset

    def regressaop(self, n, outro=None):
        # Chama a função polyfit e inverte seu resultado, pois sua numeração coeficiente é invertida
        b = np.polyfit(self.dataset.x, self.dataset.y, n)[::-1]

        def somatoriap(b, x):
            resultado = 0
            for i in range(n+1):
                resultado += b[i] * x ** i
            return np.array(resultado)
        # Quando outro objeto for passado como parâmetro o valor do polyfit será compartilhado entre o calculo de ambos
        if outro is None:
            return somatoriap(b, self.dataset.x)
        return somatoriap(b, self.dataset.x), somatoriap(b, outro.dataset.x)

    @staticmethod
    def eqm(y1, y2):
        # Se o tamanho dos vetores de entrada for diferente, deve ser feito um broadcasting do maior para o menor,
        # de forma que os elementos faltantes no array menor sejam iguais aos do array maior
        if len(y1) != len(y2):
            y1y = y1 if len(y1) > len(y2) else [y1[i] if i < len(y1) else 0 for i in range(len(y2))]
            y2y = y2 if len(y2) > len(y1) else [y2[i] if i < len(y2) else 0 for i in range(len(y1))]
            return reduce(operator.add, (y1y - y2y) ** 2) / len(y2y)
        return reduce(operator.add, (y1 - y2) ** 2) / len(y2)

# Realiza leitura do arquivo e parsing dos valores para float
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "data_preg.csv")) as file:
    raw_data = csv.reader(file, delimiter=',')
    data = [[float(elem) for elem in row] for row in raw_data]

if data is not None:
    ds = DataSet([elem[0] for elem in data], [elem[1] for elem in data])
    rp = RegressaoPolinomial(ds)

    # Cria diagrama de disperção dos pontos do dataset
    fig = plt.figure('Gráfico de disperção')
    plt.title('Vermelho: N1  Verde: N2  Preto: N3  Amarelo: N8')
    plt.grid(True)
    plt.scatter(ds.x, ds.y)

    # Gera a linha de regressão polinomial para N1 em vermelho
    y1 = rp.regressaop(1)
    plt.plot(ds.x, y1, 'r')

    # Gera a linha de regressão polinomial para N2 em verde
    y2 = rp.regressaop(2)
    plt.plot(ds.x, y2, 'g')

    # Gera a linha de regressão polinomial para N3 em preto
    y3 = rp.regressaop(3)
    plt.plot(ds.x, y3, 'k')

    # Gera a linha de regressão polinomial para N8 em amarelo
    y4 = rp.regressaop(8)
    plt.plot(ds.x, y4, 'y')

    # Calcula o erro quadratico médio EQM para cada uma das regressões
    eqm = [[y, RegressaoPolinomial.eqm(y, ds.y)] for y in [y1, y2, y3, y4]]
    for i in range(len(eqm)):
        print('EQM da regressão nº%s' % str(i+1), eqm[i][1])

    plt.show()

    # Treinamento para evitar underfitting e overfitting
    # Número de iterações para o treinamento
    iteracoes = 1
    # 'True' para exibir as regressões, 'False' para exeibir apenas o resultado final
    exibeDiagramaTreinamento = True

    for i in range(iteracoes):
        # Cria uma cópia dos dados do dataset e randomiza o endereçamento deles na matriz
        datai = deepcopy(data)
        random.shuffle(datai)

        # Seleciona 10% dos dados aleatórios como dados para teste e os outros 90% para dados de treinamento
        index = round((ds.lenght * 10) / 100)
        ds_teste = DataSet([elem[0] for elem in datai[0:index]], [elem[1] for elem in datai[0:index]])
        ds_treinamento = DataSet([elem[0] for elem in datai[index:ds.lenght]], [elem[1] for elem in datai[index:ds.lenght]])
        rp_teste = RegressaoPolinomial(ds_teste)
        rp_treinamento = RegressaoPolinomial(ds_treinamento)

        if exibeDiagramaTreinamento:
            fig = plt.figure('Treinamento de Regressão Polinominial')
            plt.grid(True)
            plt.scatter(ds_teste.x, ds_teste.y)
            plt.scatter(ds_treinamento.x, ds_treinamento.y, c='r')
            plt.xlabel('Número de Quartos')
            plt.ylabel('Preço')

        # Calcula a regressão polinomial dos datasets de treino e de teste com o mesmo polyfit
        y1_tre, y1_tes = rp_treinamento.regressaop(1, rp_teste)
        y2_tre, y2_tes = rp_treinamento.regressaop(2, rp_teste)
        y3_tre, y3_tes = rp_treinamento.regressaop(3, rp_teste)
        y4_tre, y4_tes = rp_treinamento.regressaop(8, rp_teste)

        if exibeDiagramaTreinamento:
            plt.plot(ds_treinamento.x, y1_tre, 'r')
            plt.plot(ds_treinamento.x, y2_tre, 'g')
            plt.plot(ds_treinamento.x, y3_tre, 'k')
            plt.plot(ds_treinamento.x, y4_tre, 'y')

        print(RegressaoPolinomial.eqm(y1_tre, y1_tes))
        print(RegressaoPolinomial.eqm(y2_tre, y2_tes))
        print(RegressaoPolinomial.eqm(y3_tre, y3_tes))
        print(RegressaoPolinomial.eqm(y4_tre, y4_tes))

        if exibeDiagramaTreinamento:
            plt.show()

else:
    print('Erro ao ler arquivo')


