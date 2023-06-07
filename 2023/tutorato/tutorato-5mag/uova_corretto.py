#/usr/bin/env python3


import sys
import os

import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

input_file = open("input.txt", "r")
lines = input_file.readlines()

K, N = map(int, lines[0].split())

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

    start = 1
    end = n + 1

    def f(p, k):
        nr = uova(n - p, k) + 1
        r = uova(p - 1, k - 1) + 1
        return nr > r

    
    # for p in range(1, (n+1)):

    while end - start > 1:

        m = (end + start) // 2

        if f(m, k):
            start = m
        else:
            end = m

    nr = uova(n - start, k) + 1
    r = uova(start - 1, k - 1) + 1
    sp_start = max(nr, r)

    nr = uova(n - end, k) + 1
    r = uova(end - 1, k - 1) + 1
    sp_end = max(nr, r)

    sol = min(sp_start, sp_end)

        # Non si rompe
        # [1,p] non si rompe
        # (p, n] non sappiamo niente
        
        # n diminuisce all'aumentare di p
        # come si comporta nr al variare di (n - p)?
        # n - p => piccolo ==> nr sara' piccolo
        # n - p => grande ==> nr sara' grande

        # all'aumentare di p => nr diminuisce
        # nr = uova(n - p, k) + 1
        

        # Si rompe
        # [1,p) non sappiamo niente
        # [p,n] si rompe

        # n aumenta all'aumentare di p

        # all'aumentare di p => r aumenta
        # r = uova(p - 1, k - 1) + 1

        # Caso peggiore se lanciamo un uovo dal piano p

    M[n][k] = sol
    return sol



output_file = open("output.txt", "w")

sol = uova(N, K)

print(sol, file=output_file)