#/usr/bin/env python3


import sys
import os

import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

input_file = open("input.txt", "r")
lines = input_file.readlines()

N = int(lines[0])
P = []

for i in range(N):
    p = int(lines[i+1])
    P.append(p)

M = []


# Funzione: M[mid] > p
# Ritornare il primo valore che ritorna false o la fine dell'array

# Ritorna l'indice del primo valore di M che e' minore o uguale di p
# sapendo che M e' ordinato in ordine decrescente
def lower_bound(M, p):


    low = -1

    # M[high] <= p o la fine dell'array
    high = len(M)

    while high - low > 1:
        mid = (high + low) // 2
        if M[mid] > p:
            low = mid
        else:
            high = mid

    return high

# array M, dove M[i] e' la posizione del valore piu' alto a cui si arriva
# con una decreasing sequence di dimensione i+1

for i in range(N):
    x = lower_bound(M, P[i])
    if x == len(M):
        M.append(P[i])
    else:
        M[x] = P[i]

soluzione = len(M)

output_file = open("output.txt", "w")
print(soluzione, file=output_file)


# 0 1 2 3 4 5 6 7
# 3 6 4 8 2 9 4 2

# 2 2 3 4 4 6 8 9 
# 4 7 0 2 6 1 3 5

# 0 1 2 3 4 5 6 7
# 3 6 4 7 0 8 6 1


# 1 1 2 2 2 3 3 3