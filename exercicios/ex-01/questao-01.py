import matplotlib.pyplot as plt

def exibir(I):
    plt.imshow(I, 'gray')
    plt.show(block=False)
    plt.pause(0.5)
    plt.clf()

matrix = [[0 for i in range(5)] for j in range(5)]

print(matrix)

exibir(matrix)
