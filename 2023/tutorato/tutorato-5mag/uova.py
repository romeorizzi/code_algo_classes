#/usr/bin/env python3


import sys
import os



input_file = open("input.txt", "r")
lines = input_file.readlines()

N, K = map(int, lines[0].split())

M = [[None for _ in range(K+1)] for _ in range(N+1)]

def uova(n, k):

    if n == 0:
        return 0

    if n == 1:
        return 1
    
    if k == 1:
        return n
    
    if M[n][k] is not None:
        return M[n][k]
    
    sol = 100000000
    
    for p in range(1, (n+1)):
        # Non si rompe
        # [0,p] non si rompe
        # (p, n] non sappiamo niente
        nr = uova(n - p, k) + 1

        # Si rompe
        # [0,p) non sappiamo niente
        # [p,n] si rompe
        r = uova(p, k - 1) + 1

        # Caso peggiore se lanciamo un uovo dal piano p
        sp = max(nr, r)

        sol = min(sol, sp)


    print(f"SOL: {n}/{k} => {sol}")
    M[n][k] = sol
    return sol



output_file = open("output.txt", "w")

sol = uova(N, K)

print(sol, file=output_file)