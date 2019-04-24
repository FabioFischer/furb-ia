

class Cidade:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "(x:%s, y:%s)" % (self.x, self.y)

    def __str__(self):
        return "(x:%s, y:%s)" % (self.x, self.y)
