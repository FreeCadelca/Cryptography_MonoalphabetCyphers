import math
import sys

from AffineCypher import AffineCypher
from RecurrentAffineCypher import *
from AlphabetConfig import *

text = ''
line = input()
while line != '':
    text += line + '\n'
    line = input()

for alpha1 in [i for i in range(1, 27) if math.gcd(26, i) == 1]:
    for alpha2 in [i for i in range(1, 27) if math.gcd(26, i) == 1]:
        for beta1 in range(1, 27):
            for beta2 in range(1, 27):
                cypher = RecurrentAffineCypher(alpha1, alpha2, beta1, beta2)
                decrypted = cypher.decrypt(text)
                if "the" in decrypted and "so" in decrypted and "will" in decrypted:
                    print(alpha1, alpha2, beta1, beta2)