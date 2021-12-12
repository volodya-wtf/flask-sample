import random


class Extrasense(object):
    def __init__(self, name):
        self.name = name

    def oracle(self):
        return random.randrange(10, 99)