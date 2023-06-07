#/usr/bin/env python3


import sys
import os

import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

input_file = open("input.txt", "r")
lines = input_file.readlines()

N, M = map(int, lines[0].split())

L = [[] for _ in range(N+1)]
V = [False for _ in range(N+1)]
S = [False for _ in range(N+1)]

for i in range(M):
    p, q = map(int, lines[i+1].split())
    L[p].append(q)

ciclo = []

# Trovare un ciclo diretto nel grafo (se esiste)
def dfs(n):
    global ciclo

    if V[n]:
        if S[n]:
            # Abbiamo trovato un ciclo
            return n
        return None
    
    V[n] = True
    S[n] = True

    for e in L[n]:
        c = dfs(e)
        if c is not None:
            ciclo.append(n)
            if n == c:
                return None
            else:
                return c
        elif len(ciclo) > 0:
            return None
    
    S[n] = False

# W[n] Contiene il path piu' lungo percorribile partendo dal nodo n
W = [None for _ in range(N+1)]
P = [None for _ in range(N+1)]

# Trovare il percorso piu' lungo in un grafo diretto aciclico
def dfs_lw(n):
    if W[n] is not None:
        return W[n]
    
    sol = 1
    next = None

    for e in L[n]:
        x = dfs_lw(e)
        if sol < x+1:
            sol = x + 1
            next = e
    
    W[n] = sol
    P[n] = next
    return W[n]




output_file = open("output.txt", "w")

for n in range(1, N+1):
    dfs(n)
    if len(ciclo) > 0:
        ciclo.reverse()
        print(f"-1 {len(ciclo)}", file=output_file)
        print(" ".join([str(x) for x in ciclo]), file=output_file)
        exit(0)


for n in range(1, N+1):
    dfs_lw(n)

best_val = 0
best_node = 0
for n in range(1, N+1):
    if W[n] > best_val:
        best_val = W[n]
        best_node = n

percorso = []
while best_node is not None:
    percorso.append(best_node)
    best_node = P[best_node]

print(len(percorso), file=output_file)
print(" ".join([str(x) for x in percorso]), file=output_file)


# print(sol, file=output_file)