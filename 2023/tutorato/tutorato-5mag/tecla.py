#/usr/bin/env python3


import sys
import os



input_file = open("input.txt", "r")
lines = input_file.readlines()

N, M = map(int, lines[0].split())

L = [[] for _ in range(N)]
P = [None for _ in range(N)]

for i in range(M):
    a, b = map(int, lines[i+1].split())
    L[a].append(b)
    L[b].append(a)

ciclo_dispari = []
percorso_ciclo_0 = []

def dfs(n, p):
    global L, P, ciclo_dispari, percorso_ciclo_0

    if P[n] is not None:
        if P[n] % 2 == p % 2:
            return None
        else:
            ciclo_dispari.append(n)
            return n
        
    P[n] = p

    for a in L[n]:
        f = dfs(a, p + 1)
        if f is not None:
            ciclo_dispari.append(n)
            if f == n:
                return None
            else:
                return f
        elif len(ciclo_dispari) > 0:
            percorso_ciclo_0.append(n)
            return None


dfs(0, 0)

# print("ciclo_dispari:", ciclo_dispari)
# print("percorso_ciclo_0:", percorso_ciclo_0)

output_file = open("output.txt", "w")

print(2 * len(percorso_ciclo_0) + len(ciclo_dispari) - 1, file=output_file)


percorso_0_ciclo = percorso_ciclo_0.copy()
percorso_0_ciclo.reverse()

S = percorso_0_ciclo.copy() + ciclo_dispari + percorso_ciclo_0
print(" ".join([str(s) for s in S]), file=output_file)

