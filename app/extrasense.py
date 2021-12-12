import random


class Extrasense(object):
    def __init__(self, name):
        self.name = name

    def guess(self):
        return random.randrange(10, 99)

    def accuracy(l1, l2: list) -> str:
        acc = 0
        for i, j in zip(l1, l2):
            if i == j:
                acc += 1
        return f"{acc}/{len(l1)}"