from Cromossomo import Cromossomo


class Individuo():
    def __init__(self, cenario, estado_inicial, estado_objetivo, prob_mutacao, genes=None):
        self.cromossomo = Cromossomo(cenario, estado_inicial, estado_objetivo, prob_mutacao, genes)
        self.aptidao = self.determina_aptidao(cenario)

    def __repr__(self):
        return "(apt:%s)" % self.aptidao

    def __str__(self):
        return "(apt:%s)" % self.aptidao

    def determina_aptidao(self, cenario):
        if self.cromossomo is not None and self.cromossomo.genes is not None:
            return self.soma_custo(cenario)
        return 0

    def soma_custo(self, cenario, i=1):
        if i < len(self.cromossomo.genes):
            return cenario.matriz_identidade[self.cromossomo.genes[i-1].id][self.cromossomo.genes[i].id] + self.soma_custo(cenario, i+1)
        return 0

    def reproduzir(self, pai2, cenario, estado_inicial, estado_objetivo, prob_mutacao):
        g1, g2 = self.cromossomo.reproduzir(pai2.cromossomo)
        print(g1)
        print(g2)
        print('*******')
        return Individuo(cenario, estado_inicial, estado_objetivo, prob_mutacao, g1), \
               Individuo(cenario, estado_inicial, estado_objetivo, prob_mutacao, g2)
