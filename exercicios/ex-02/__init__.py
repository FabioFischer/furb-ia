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
    Exercício 02

    Adriner Maranho de Andrade, Fábio Luiz Fischer, Jordy Felipe da Silva


    A partir da estrutura do Agente Reativo Simples, aumente o código para transformá-lo em
    Agentes Baseados em Objetivos, na qual:
    a) o agente tem que limpar toda a sala (função objetivo)
    b) o agente começa a partir quadrado (1, 1)
    Utilize também uma variável de contador (chamada pontos) que contém o número de passos que o
    agente leva até atingir o objetivo.

    Dicas:
    • escreva uma função de verificação (checkObj(sala)) fora do programa agente que verifica se
    há sujeira na sala (retorna 1 se tem sujeira, caso contrário retorna 0).
    • Acrescente a ação "NoOp" na lista de ações do agente e ajuste a ação para "NoOp" uma vez
    que a sala estiver limpa.
    A função de agente deve ser chamado agenteObjetivo(percepcao, objObtido) e deve retornar uma
    das 6 ações possíveis (5 inicialmente definidas + "NoOp"). O parâmetro objObtido é a saída da
    função checkObj(sala).

    Responda: É possível ter todo o espaço limpo efetivamente? Justifique sua resposta.

    Resposta:
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