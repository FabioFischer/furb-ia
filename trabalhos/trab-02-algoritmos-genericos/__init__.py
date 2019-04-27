from random import randint
from Cenario import Cenario
from Individuo import Individuo

qtd_cidades = 20
qtd_individuos = 20
iteracoes = 1
prob_mutacao = 0.05

cenario = Cenario(qtd_cidades)
estado_inicial = cenario.cidades[0]
estado_objetivo = cenario.cidades[0]
# População inicial de 20 individuos
populacao = [Individuo(cenario, estado_inicial, estado_objetivo, prob_mutacao) for i in range(qtd_individuos)]
print(populacao)


def realiza_selecao():
    global populacao
    prob_pop = [(populacao[i], i+1) for i in range(len(populacao))][::-1]
    pais = [(None, None) for i in range(round(len(prob_pop)/2))]
    for i in range(round(len(prob_pop)/2)):
        pai1 = define_pais(prob_pop)
        pais[i] = (pai1, define_pais(prob_pop, pai1))
    return pais


def define_pais(prob_pop, pai1=None):
    if pai1 is not None:
        prob_pop = [i for i in prob_pop if i[0] != pai1]
    index = randint(1, sum(int(i[1]) for i in prob_pop))
    for prioridade_ind in prob_pop:
        if index - prioridade_ind[1] <= 0:
            return prioridade_ind[0]
        index -= prioridade_ind[1]
    return prob_pop[len(prob_pop) - 1][0]


for i in range(iteracoes):
    # Seleciona a metade da população com maior aptidao
    populacao = sorted(populacao, key=lambda individuo: individuo.aptidao)[::-1][0:round(qtd_cidades/2)]
    for pais in realiza_selecao():
        # Cada casal gera um par de individuos
        f1, f2 = pais[0].reproduzir(pais[1], cenario, estado_inicial, estado_objetivo, prob_mutacao)
        #populacao.append(f1, f2)
