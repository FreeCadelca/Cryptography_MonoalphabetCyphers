from AlphabetConfig import *


def inv(n):
    return pow(n, -1, m)


class RecurrentAffineCypher:
    def __init__(self, key_alpha_1, key_alpha_2, key_beta_1, key_beta_2):
        self.__key_alpha_1 = key_alpha_1
        self.__key_alpha_2 = key_alpha_2
        self.__key_beta_1 = key_beta_1
        self.__key_beta_2 = key_beta_2

    def encrypt(self, x):
        keys_alpha = [self.__key_alpha_1, self.__key_alpha_2]
        keys_beta = [self.__key_beta_1, self.__key_beta_2]
        y = ''
        for i in range(len(x)):
            if x[i] not in A.values():
                y += x[i]
                continue
            if i < 2:
                y += A[((keys_alpha[-1] * A_ID[x[i]]) + keys_beta[-1]) % m]
            else:
                keys_alpha.append((keys_alpha[-1] * keys_alpha[-2]) % m)
                keys_beta.append((keys_beta[-1] + keys_beta[-2]) % m)
                y += A[((keys_alpha[-1] * A_ID[x[i]]) + keys_beta[-1]) % m]
        return y

    def decrypt(self, y):
        return_keys_alpha = [inv(self.__key_alpha_1), inv(self.__key_alpha_2)]
        keys_beta = [self.__key_beta_1, self.__key_beta_2]
        x = ''
        for i in range(len(y)):
            if y[i] not in A.values():
                x += y[i]
                continue
            if i < 2:
                x += A[((A_ID[y[i]] - keys_beta[-1]) * return_keys_alpha[-1]) % m]
            else:
                return_keys_alpha.append((return_keys_alpha[-1] * return_keys_alpha[-2]) % m)
                keys_beta.append((keys_beta[-1] + keys_beta[-2]) % m)
                x += A[((A_ID[y[i]] - keys_beta[-1]) * return_keys_alpha[-1]) % m]
        return x

    def info(self):
        print(f'keys:\n'
              f'\talpha: ({self.__key_alpha_1}, {self.__key_alpha_2})\n'
              f'\tbeta:  ({self.__key_beta_1}, {self.__key_beta_2})')
