import random

from flask import session


class Extrasense(object):
    def __init__(self, name):
        self.name = name


    def guess(self) -> int:
        return random.randrange(10, 99)


    def accuracy(self, user_last, extrasense_last, extrasense_score : int) -> int:
        print("elast", extrasense_last)
        print("ulast", user_last)
        print("escore", extrasense_score)
        if user_last and extrasense_last != None:
            if user_last == extrasense_last:
                extrasense_score += 1

            else:
                extrasense_score -= 1

        
        return extrasense_score


def extrasense_factory(names: list) -> list:
    extrasenses = []
    for name in names:
        extrasenses.append(Extrasense(name))
    return extrasenses
