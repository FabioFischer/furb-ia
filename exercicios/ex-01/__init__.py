import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from copy import deepcopy
from random import randint
from Agente import Agente
from Mapeador import Mapeador
from TipoRegiao import TipoRegiao
from TipoAcao import TipoAcao

"""

"""


def mapa_aleatorio(tamanho):
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


def mapa_exibicao(mapa, agente):
    ref = deepcopy(mapa)
    ref[agente.x][agente.y] = TipoRegiao.agente.value
    return ref


def agente_reativo_simples(percepcao, agente):
    global mapeador
    if agente.x == pos_inicial_agente[0] and agente.y == pos_inicial_agente[1]:
        mapeador = Mapeador(mapa, agente)
    if percepcao[agente.x][agente.y] == TipoRegiao.sujo.value:
        return TipoAcao.aspirar
    else:
        return mapeador.define_acao()


def executa_acao(mapa, agente, acao):
    print(acao)
    if acao == TipoAcao.acima:
        if agente.x > 1:
            agente.x -= 1
    elif acao == TipoAcao.abaixo:
        if agente.x < (tamanho_mapa - 2):
            agente.x += 1
    elif acao == TipoAcao.esquerda:
        if agente.y > 1:
            agente.y -= 1
    elif acao == TipoAcao.direita:
        if agente.y < (tamanho_mapa - 2):
            agente.y += 1
    elif acao == TipoAcao.aspirar:
        mapa[agente.x][agente.y] = TipoRegiao.limpo.value


def inicia_animacao():
    im.set_array(mapa_exibicao(mapa, agente))
    return im,


def animacao(*args):
    global mapa, agente
    executa_acao(mapa, agente, agente_reativo_simples(mapa, agente))
    im.set_array(mapa_exibicao(mapa, agente))
    return im,

frame_rate = 60
tamanho_mapa = 6
pos_inicial_agente = (1, 1)

mapa = mapa_aleatorio(tamanho_mapa)
agente = Agente(pos_inicial_agente[0], pos_inicial_agente[1])
mapeador = Mapeador(mapa, agente)

fig = plt.figure()
cmap = matplotlib.cm.Pastel2
im = plt.imshow(mapa_exibicao(mapa, agente), cmap, animated=True)
# https://matplotlib.org/api/_as_gen/matplotlib.animation.FuncAnimation.html
ani = animation.FuncAnimation(fig, animacao, init_func=inicia_animacao, frames=frame_rate, interval=500, blit=True)
plt.show()
plt.pause(0.5)
plt.clf()
