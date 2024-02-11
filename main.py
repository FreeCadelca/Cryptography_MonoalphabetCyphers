import sys
from AlphabetConfig import *
from AffineCypher import *
from RecurrentAffineCypher import *
from SimpleReplaceCypher import *


def text_input():
    text = ''
    line = input()
    while line != '':
        text += line + '\n'
        line = input()
    return text


state = 'chooseCypher'
cypher = None
while True:
    if state == 'chooseCypher':
        cypher_name = input('Введите номер шифра (1 - простые замены, 2 - Аффинный, 3 - Аффинный рекуррентный):\n')
        if cypher_name == '1':
            state = 'replaces'
            key = input("Введите ключ для данного шифра в виде символов через пробел во второй строке подстановки "
                        "математического описания этого шифра. \n"
                        "Помимо латинских строчных букв не забудьте следующие символы: "
                        "\' \', \'.\', \',\', \'-\', \'\"\', \';\', \'!\'\n"
                        "Или введите пустую строку, если хотите использовать автоматическую генерацию ключа\n")
            if key:
                cypher = SimpleReplaceCypher(key)
            else:
                cypher = SimpleReplaceCypher()
        elif cypher_name == '2':
            state = 'Affine'
            key = input("Введите ключ для данного шифра в виде двух чисел через пробел - значения alpha и beta:\n")
            key = list(map(int, key.split()))
            cypher = AffineCypher(key[0], key[1])
        elif cypher_name == '3':
            state = 'RecAffine'
            key = input(
                "Введите ключ для данного шифра в виде четырех чисел через пробел - значения alpha_1, alpha_2, beta_1 и beta_2:\n")
            key = list(map(int, key.split()))
            cypher = RecurrentAffineCypher(key[0], key[1], key[2], key[3])
        cypher.info()
    if state in ('replaces', 'Affine', 'RecAffine'):
        print("Введите текст для зашифрования/расшифрования\n(Заглавные буквы автоматически заменятся на строчные, введите пустую строку для остановки):")
        text = text_input().lower()
        mode = input("Введите операцию (E/D - Encrypt/Decrypt)\n")
        if mode == "E":
            print(cypher.encrypt(text))
        elif mode == "D":
            print(cypher.decrypt(text))
