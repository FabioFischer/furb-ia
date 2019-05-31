import math


class CorrelacaoRegressaoLinear:
    def __init__(self, dataset):
        self.dataset = dataset
        self.r = self.correlacao()
        self.b0, self.b1 = self.regressao()

    def correlacao(self):
        # Σ(x−x̄)(y−ȳ)
        aux = 0
        for i in range(len(self.dataset.x)):
            aux += (self.dataset.x[i] - self.dataset.med_x) * (self.dataset.y[i] - self.dataset.med_y)
        # Σ(arr−arr̄)²
        def soma_linear(dataset, mediana):
            sum = 0
            for elem in dataset:
                sum += (elem - mediana) ** 2
            return sum
        # (Σ(x−x̄)(y−ȳ)) / √(Σ(x−x̄)² Σ(y−ȳ)²)
        return aux / (math.sqrt(soma_linear(self.dataset.x, self.dataset.med_x) * soma_linear(self.dataset.y, self.dataset.med_y)))

    def regressao(self):
        # Σ(x−x̄)(y−ȳ)
        dividend = 0
        for i in range(len(self.dataset.x)):
            dividend += (self.dataset.x[i] - self.dataset.med_x) * (self.dataset.y[i] - self.dataset.med_y)
        # Σ(x−x̄)²
        b1_div = 0
        for elem in self.dataset.x:
            b1_div += (elem - self.dataset.med_x) ** 2
        # 𝛽1 = Σ(x−x̄)(y−ȳ) / Σ(x−x̄)²
        b1 = dividend / b1_div
        # 𝛽0 = 𝑦̄− β1x,
        return self.dataset.med_y - (b1 * self.dataset.med_x), b1

    def reta_regressao(self, x):
        # 𝑦̂=𝛽0+𝛽1z
        return self.b0 + (self.b1 * x)
