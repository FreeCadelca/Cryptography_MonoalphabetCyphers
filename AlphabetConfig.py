ALPHABET = [chr(i) for i in list(range(ord('a'), ord('z') + 1))]
A = {i: ALPHABET[i] for i in range(len(ALPHABET))}
A_ID = {A[i]: i for i in A.keys()}
m = len(ALPHABET)
