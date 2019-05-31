import operator
from functools import reduce


class DataSet:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.med_x = self.mediana(self.x)
        self.med_y = self.mediana(self.y)

    def mediana(self, arr):
        sum = reduce(operator.add, arr)
        return sum / len(arr)