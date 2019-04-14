import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from copy import deepcopy
from random import randint
from Agente import Agente
from TipoRegiao import TipoRegiao
from TipoAcao import TipoAcao

"""
    FURB - Bacharelado em Ciências da Computação
    Inteligência Artificial
    Atividade Avaliativa: APA
    Exercício 01

    Adriner Maranho de Andrade, Fábio Luiz Fischer, Jordy Felipe da Silva


    Escreva uma função de Agente Reativo Simples para o mundo 4 x 4 do aspirador de pó
    automático que garante limpar toda a sala, independentemente da posição inicial. A função
    deve ser chamada agenteReativoSimples(percepcao) e deve retornar uma das 5 possíveis ações
    ('acima', 'abaixo', 'esquerda', 'direita', 'aspirar'). A variável "percepcao" dentro dos parênteses é
    a entrada da função.

    Dicas:
    • Você pode considerar criar uma função de mapeamento (funcaoMapear) como um ponto de
    partida.
    • Tenha em mente que as ações contra a parede (por exemplo, mover para a esquerda
    quando já está posicionado no ponto (1, 1)) não têm nenhum efeito (isto não significa que
    são proibidas)

    Responda: A sua solução é extensível para um mundo 3 x 3? E para um mundo 6 x 6? Explique sua
    resposta.

    Resposta: Sim, enquanto a altura do mapa for igual ao comprimento, o mapeamento desenvolvido atende a necessidade,
        mesmo que não seja uma solução ótima para alguns casos. A rota do agente é construída com base no comprimento e
        na altura do mapa e é representada por um fila de direções. A fila é populada sempre que o agente esta em sua
        posição inicial(0, 0). Caso a região em que o agente esta posicionado esteja suja, a ação a ser tomada será
        "aspirar", caso contrário, a fila do mapeamento será consumida.
"""


# constrói um mapa com paredes e regiões aleatórias
def mapa_aleatorio(tamanho):
    mapa = [[0 for x in range(tamanho)] for y in range(tamanho)]
    for x in range(tamanho):
        for y in range(tamanho):
            if y == 0 or y == (tamanho - 1):
                mapa[x][y] = TipoRegiao.parede.value
            elif x == 0 or x == (tamanho - 1):
                mapa[x][y] = TipoRegiao.parede.value
            else:
                mapa[x][y] = TipoRegiao.sujo.value if randint(0, 1) == 1 else TipoRegiao.limpo.value
    return mapa


# Com o objetivo de simplificar a aplicação e garantir os resultados,
# o agente não faz parte do mapa da percepção e é incluído apenas na exibição do cenário
def mapa_exibicao(mapa, agente):
    ref = deepcopy(mapa)
    ref[agente.x][agente.y] = TipoRegiao.agente.value
    return ref


# Gerencia a posição do agente em relação ao mundo e determina a próxima ação
def agente_reativo_simples(percepcao, agente):
    print("Percepção", percepcao[agente.x][agente.y])
    # Se a região em que o agente esta posicionado está suja, a ação deve ser aspirar,
    # caso contrario deve seguir a rota do mapeamento
    if percepcao[agente.x][agente.y] == TipoRegiao.sujo.value:
        return TipoAcao.aspirar
    # Quando o agente estiver na posição inicial,
    # a fila de mapeamento deve ser preenchida com a rota que o agente deve percorrer
    if agente.x == 1 and agente.y == 1:
        agente.inicializa_mapeamento(mapa)
    return agente.define_acao_mapeamento()


# Função chamada na inicialização da animação
def inicia_animacao():
    im.set_array(mapa_exibicao(mapa, agente))
    return im,


# Função chamada a cada frame da animação
def animacao(*args):
    global mapa, agente
    # Determina a próxima ação do agente com base em sua posição atual
    acao = agente_reativo_simples(mapa, agente)
    print("Ação", acao.name)
    # Agente executa a ação
    agente.executa_acao(mapa, acao)
    im.set_array(mapa_exibicao(mapa, agente))
    return im,

intervalo_frames = 500
frame_rate = 60
# o tamanho do mapa considera o tamanho da parede
tamanho_mapa = 6

# Inicialização dos objetos da aplicação
mapa = mapa_aleatorio(tamanho_mapa)
agente = Agente(1, 1)

# Inicialização e configuração da animação
fig = plt.figure("Atividade Avaliativa: APA - Exercício 01")
cmap = matplotlib.cm.Pastel2
im = plt.imshow(mapa_exibicao(mapa, agente), cmap, animated=True)
# https://matplotlib.org/api/_as_gen/matplotlib.animation.FuncAnimation.html
ani = animation.FuncAnimation(fig, animacao, init_func=inicia_animacao, frames=frame_rate, interval=intervalo_frames, blit=True)
plt.show()
plt.pause(0.5)
