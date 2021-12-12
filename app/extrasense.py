import random


class Extrasense(object):
    def __init__(self, name):
        self.name = name


    def guess(self) -> int:
        return random.randrange(10, 99)


    def accuracy(self, l1, l2: list) -> str:
        acc = 0
        for i, j in zip(l1, l2):
            if i == j:
                acc += 1
        return f"{acc}/{len(l1)}"


def extrasense_factory(names: list) -> list:
    extrasenses = []
    for name in names:
        extrasenses.append(Extrasense(name))
    return extrasenses
