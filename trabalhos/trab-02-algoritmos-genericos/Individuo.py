from Cromossomo import Cromossomo

class Individuo():
    def __init__(self, cenario, estado_inicial, estado_objetivo, pai_01=None, pai_02=None):
        self.cromossomo = Cromossomo(cenario, estado_inicial, estado_objetivo, pai_01, pai_02)
        self.aptidao = self.determina_aptidao(cenario)

    def determina_aptidao(self, cenario):
        if self.cromossomo is not None and self.cromossomo.genes is not None:
            return self.soma_custo(cenario, 1)
        return 0

    def soma_custo(self, cenario, i):
        if i < len(self.cromossomo.genes):
            return cenario.matriz_identidade[self.cromossomo.genes[i-1].id][self.cromossomo.genes[i].id] + self.soma_custo(cenario, i+1)
        return 0

    def __repr__(self):
        return "(apt:%s)" % (self.aptidao)

    def __str__(self):
        return "(apt:%s)" % (self.aptidao)
