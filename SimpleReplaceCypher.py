import random

from AlphabetConfig import *


class SimpleReplaceCypher:
    def __init__(self, key=None):  # ключ - подстановка математического описания шифра в виде словаря
        if key is None:
            shuffled_values = list(A.values()).copy()
            random.shuffle(shuffled_values)
            i = 0
            self.__key = {}
            for symbol in A.values():
                self.__key[symbol] = shuffled_values[i]
                i += 1
        else:
            key = key.split()
            i = 0
            self.__key = {}
            for symbol in A.values():
                self.__key[symbol] = key[i]
                i += 1
        self.__return_key = {self.__key[i]: i for i in self.__key.keys()}

    def encrypt(self, x):
        return ''.join(self.__key[i] for i in x)

    def decrypt(self, y):
        return ''.join(self.__return_key[i] for i in y)

    def info(self):
        print(f'key =        /{' '.join(self.__key.keys())}\\\n'
              f'             \\{' '.join(self.__key.values())}/\n'
              f'return_key = /{' '.join(self.__return_key.keys())}\\\n'
              f'             \\{' '.join(self.__return_key.values())}/')
