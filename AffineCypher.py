from AlphabetConfig import *


def inv(n):
    return pow(n, -1, m)


class AffineCypher:
    def __init__(self, key_alpha, key_beta):
        self.__key_alpha = key_alpha
        self.__key_beta = key_beta

    def encrypt(self, x):
        y = ''
        for i in x:
            if i not in A.values():
                y += i
                continue
            y += A[(A_ID[i] * self.__key_alpha + self.__key_beta) % m]
        return y

    def decrypt(self, y):
        x = ''
        for i in y:
            if i not in A.values():
                x += i
                continue
            x += A[((A_ID[i] - self.__key_beta) % m) * inv(self.__key_alpha) % m]
        return x

    def info(self):
        print(f'keys: ({self.__key_alpha}, {self.__key_beta})')
