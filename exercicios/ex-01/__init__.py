import time
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from copy import deepcopy
from random import randint
from Agente import Agente
from TipoRegiao import TipoRegiao
from TipoAcao import TipoAcao

"""

"""


def constroiMapa(tamanho):
    mapa = [[0 for x in range(tamanho)] for y in range(tamanho)]
    for x in range(tamanho):
        for y in range(tamanho):
            if y == 0 or y == (tamanho - 1):
                mapa[x][y] = TipoRegiao.parede.value
            elif x == 0 or x == (tamanho - 1):
                mapa[x][y] = TipoRegiao.parede.value
            else:
                ran = randint(0, 1)
                mapa[x][y] = TipoRegiao.sujo.value if ran == 1 else TipoRegiao.limpo.value
    return mapa

def mapaExibicao(mapa, agente):
    ref = deepcopy(mapa)
    ref[agente.x][agente.y] = TipoRegiao.agente.value
    return ref

def agenteReativoSimples(percepcao, agente):
    print("percepcao - ", percepcao)
    return TipoAcao.abaixo

def initAnimation():
    print('alo')

    im.set_array(mapaExibicao(mapa, agente))
    return im,

def draw(*args):
    global mapa, agente

    acao = agenteReativoSimples(mapa, agente)
    print("acao", acao.name)

    if acao == TipoAcao.acima:
        if agente.x > 1:
            agente.x -= 1
    elif acao == TipoAcao.abaixo:
        if agente.x < (tamanhoMapa - 2):
            agente.x += 1
    elif acao == TipoAcao.esquerda:
        if agente.y > 1:
            agente.y -= 1
    elif acao == TipoAcao.direita:
        if agente.y < (tamanhoMapa - 2):
            agente.y += 1
    elif acao == TipoAcao.aspirar:
        mapa[agente.x][agente.y] = TipoRegiao.limpo

    im.set_array(mapaExibicao(mapa, agente))
    return im,

frameRate = 60
tamanhoMapa = 6

mapa = constroiMapa(tamanhoMapa)
agente = Agente(1, 1)

fig = plt.figure()
cmap = matplotlib.cm.Pastel1
im = plt.imshow(mapaExibicao(mapa, agente), cmap, animated=True)
ani = animation.FuncAnimation(fig, draw, init_func=initAnimation, frames=frameRate, interval=500, blit=True)
plt.show()
plt.pause(0.5)
plt.clf()
