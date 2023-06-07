#/usr/bin/env python3


import sys
import os

import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

input_file = open("input.txt", "r")
lines = input_file.readlines()

N, M, A, B = map(int, lines[0].split())

L = [[] for _ in range(N+1)]
I = [0 for _ in range(N+1)]

for i in range(M):
    a, b = map(int, lines[i+1].split())

    visitato = {
        "visitato": False
    }

    L[a].append((b, visitato))
    L[b].append((a, visitato))

soluzione = []

def visita(n, p):
    for i in range(I[n], len(L[n])):
        if L[n][i][1]["visitato"]:
            continue
        L[n][i][1]["visitato"] = True
        I[n] = i + 1
        visita(L[n][i][0], n)
        
    soluzione.append((p, n))

visita(A, None)

soluzione.reverse()

output_file = open("output.txt", "w")

for arco in soluzione[1:]:
    print(arco[0], arco[1], file=output_file)