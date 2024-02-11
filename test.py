import sys

txt = ''
for line in sys.stdin.readlines():
    txt += line
print(list(txt))