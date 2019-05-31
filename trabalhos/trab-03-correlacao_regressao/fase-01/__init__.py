import matplotlib.pyplot as plt
from CorrelacaoRegressaoLinear import CorrelacaoRegressaoLinear
from DataSet import DataSet

# Datasets de teste
dss = [DataSet('Dataset 1', [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5], [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]),
       DataSet('Dataset 2', [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5], [9.14, 8.14, 8.47, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]),
       DataSet('Dataset 3', [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 19], [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 5.56, 7.91, 6.89, 12.50])]

fracao_plot = 0.2
limite_plot = 20

for ds in dss:
    crl = CorrelacaoRegressaoLinear(ds)

    fig = plt.figure(ds.id)
    plt.title("r: %s, β0: %s, β1: %s)" % (crl.r, crl.b0, crl.b1))
    plt.grid(True)

    print('r: ', crl.r)
    print('b0: ', crl.b0)
    print('b1: ', crl.b1)

    # Marca os pontos do dataset
    plt.scatter(ds.x, ds.y, alpha=0.5)

    # Gera valores de 0 até limite_plot de acordo com a regressão linear
    x_prev = [x * fracao_plot for x in range(round(limite_plot/fracao_plot))]
    y_prev = [crl.reta_regressao(x) for x in x_prev]
    # Merca os pontos da regressão linear
    plt.scatter(x_prev, y_prev, alpha=0.5, facecolor='red')

    plt.show()
