import matplotlib.pyplot as plt
from random import randint

def exibir(I):
    plt.imshow(I, 'gray')
    plt.show(block=True)
    plt.pause(0.5)
    plt.clf()

def buildMatriz(size):
	m = [[0 for x in range(size)] for y in range(size)]
	for x in range(size):
		for y in range(size):
			if y == 0 or y == (size - 1):
				m[x][y] = 1
			elif x == 0 or x == (size - 1):
				m[x][y] = 1
			else:
				ran = randint(0,1)
				m[x][y] = 2 if ran == 1 else 0
	return m
	
matrix = buildMatriz(6)
print(matrix)

exibir(matrix)
