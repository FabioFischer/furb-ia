
from Gene import Gene


class Cidade(Gene):
    id = 0

    def __init__(self, x, y):
        self.id = Cidade.id
        self.x = x
        self.y = y

        Cidade.id += 1

    def __repr__(self):
        return "(id:%s - x:%s, y:%s)" % (self.id, self.x, self.y)

    def __str__(self):
        return "(id:%s - x:%s, y:%s)" % (self.id, self.x, self.y)

    def __eq__(self, other):
        return self.id == other
