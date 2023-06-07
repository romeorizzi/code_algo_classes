# Lista di oggetti, ogniuno con un valore v e un peso p

# Zaino, con un limite massimo di peso

# Task => data questi oggetti e lo zaino, trovare il valore massimo di oggetti che si possono
# prendere senza eccedere il peso massimo


#/usr/bin/env python3


import sys
import os

import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

input_file = open("input.txt", "r")
lines = input_file.readlines()

N, P = map(int, lines[0].split())

valori = [0 for _ in range(N)]
pesi = [0 for _ in range(N)]

for i in range(N):
    valore, peso = map(int, lines[i + 1].split())
    valori[i] = valore
    pesi[i] = peso


M = [[None for _ in range(P+1)] for _ in range(N)]

def knapsack(i, p):
    if i >= N:
        return 0
    
    if p == 0:
        return 0
    
    if M[i][p] is not None:
        return M[i][p]

    ottimo = 0
    # Ci concentriamo sull'oggetto i

    # Prendiamo l'oggetto
    if p >= pesi[i]:
        sol1 = knapsack(i + 1, p - pesi[i]) + valore[i]
        ottimo = max(ottimo, sol1)

    # Non prendiamo l'oggetto
    sol2 = knapsack(i + 1, p)
    ottimo = max(ottimo, sol2)

    M[i][p] = ottimo
    return ottimo
    
soluzione = knapsack(0, P)

output_file = open("output.txt", "w")

print(soluzione, file=output_file)