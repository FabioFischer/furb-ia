from random import randint
from Cenario import Cenario
from Individuo import Individuo

qtd_cidades = 20
iteracoes = 5

cenario = Cenario(qtd_cidades)
estado_inicial = cenario.cidades[0]
estado_objetivo = cenario.cidades[0]
# População inicial de 20 individuos
populacao = [Individuo(cenario, estado_inicial, estado_objetivo) for i in range(qtd_cidades)]
print(populacao)

def define_prioridade(populacao):
    pop_ordenada = sorted(populacao, key=lambda individuo: individuo.aptidao)
    metade_pop = pop_ordenada[0:round(qtd_cidades/2)]
    metade_pop_inversa = metade_pop[::-1]

    prioridade_pop = [(None, 0) for i in range(len(metade_pop_inversa))]

    for i in range(len(metade_pop_inversa)):
        prioridade_pop[i] = (metade_pop_inversa[i], i+1)

    p1 = define_pai(prioridade_pop[::-1])
    print(p1)
    p2 = define_pai(prioridade_pop[::-1], p1)
    print(p2)
    print(prioridade_pop)

def define_pai(prioridade_pop, pai_01 = None):
    if pai_01 is not None:
        prioridade_pop = [i for i in prioridade_pop if i[0] != pai_01[0]]
    index = randint(1, sum(int(i[1]) for i in prioridade_pop))
    for prioridade_ind in prioridade_pop:
        if index - prioridade_ind[1] <= 0:
            return prioridade_ind
        index -= prioridade_ind[1]
    return prioridade_pop[len(prioridade_pop)-1]

for i in range(iteracoes+1):
    pais = define_prioridade(populacao)
    # Seleção de individuos existentes e criação de novos elementos
