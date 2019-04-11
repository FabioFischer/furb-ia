import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import randint

IMG_WALL_TILE = 1
IMG_CLEAN_TILE = 0
IMG_DIRTY_TILE = 2
IMG_AGENT_TILE = 3
frameRate = 3

def buildMatriz(size):
    m = [[0 for x in range(size)] for y in range(size)]
    for x in range(size):
        for y in range(size):
            if y == 1 and x == 1:
                m[x][y] = IMG_AGENT_TILE
            elif y == 0 or y == (size - 1):
                m[x][y] = IMG_WALL_TILE
            elif x == 0 or x == (size - 1):
                m[x][y] = IMG_WALL_TILE
            else:
                ran = randint(0, 1)
                m[x][y] = IMG_DIRTY_TILE if ran == 1 else IMG_CLEAN_TILE
    return m

def updatefig(*args):
    global matrix
    matrix = buildMatriz(6)
    im.set_array(matrix)
    return im,

matrix = buildMatriz(6)
print(matrix)

fig = plt.figure()
cmap = matplotlib.cm.Pastel1
im = plt.imshow(matrix, cmap, animated=True)
ani = animation.FuncAnimation(fig, updatefig, interval=1000/frameRate, blit=True)
plt.show()