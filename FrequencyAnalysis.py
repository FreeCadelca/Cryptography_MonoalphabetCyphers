import pprint
import sys
from AlphabetConfig import *

print('Enter the text for analysis of letters in dictionary ALPHABET')
text = ''
for line in sys.stdin.readlines():
    text += line

text.lower()
number_of_letters = {i: 0 for i in ALPHABET}
total_letters = 0
for letter in text:
    if letter in ALPHABET:
        number_of_letters[letter] += 1
        total_letters += 1

frequency = {i: 100 * (number_of_letters[i] / total_letters) for i in number_of_letters.keys()}
pprint.pprint(frequency)
# pprint.pprint(number_of_letters)
# pprint.pprint(total_letters)