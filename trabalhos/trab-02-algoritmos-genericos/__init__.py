
from Cenario import Cenario
from Individuo import Individuo


cenario = Cenario(20)
estado_inicial = cenario.cidades[0]
estado_objetivo = cenario.cidades[0]
# População inicial de 20 individuos
populacao = [Individuo(cenario, estado_inicial, estado_objetivo) for i in range(20)]

for i in range(10001):
    # Seleção de individuos existentes e criação de novos elementos
    a = 0
