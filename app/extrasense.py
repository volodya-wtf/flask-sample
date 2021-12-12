import random


class Extrasense(object):
    def __init__(self, name):
        self.name = name
        self.scores = 0
        self.last = None


    def guess(self) -> int:
        return random.randrange(10, 99)


    def accuracy(self, i: int) -> int:
        if self.last and i != None:
            if self.last == i:
                self.scores += 1
            else:
                self.scores -= 1

        print("self", self.last)
        print("user", i)
        return self.scores


def extrasense_factory(names: list) -> list:
    extrasenses = []
    for name in names:
        extrasenses.append(Extrasense(name))
    return extrasenses
