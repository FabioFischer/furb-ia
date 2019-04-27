

class Cidade:
    id = 0

    def __init__(self, x, y):
        self.id = Cidade.id
        self.x = x
        self.y = y

        Cidade.id += 1

    def __repr__(self):
        return "(id:%s)" % self.id

    def __str__(self):
        return "(id:%s)" % self.id

    def __eq__(self, other):
        return self.id == other