#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv, stdin, stderr, stdout, setrecursionlimit
setrecursionlimit(10**9)

filename = 'input.txt'

if len(argv) > 1:
    filename = argv[1]

if filename == 'stdin':
    fin = stdin
    fout = stdout
else:
    fin = open(filename, "r")
    fout = open("output.txt", "w")

n, m = map(int, fin.readline().strip().split() )
out_n = [ [] for _ in range(2*n) ]
in_n = [ [] for _ in range(2*n) ]
# oriento gli archi da sinistra a destra se sono nel matching, altrimenti da destra a sinistra

for _ in range(n):
    a, b = map(int, fin.readline().strip().split() )
    out_n[a].append(n+b)
    in_n[n+b].append(a)
for _ in range(n, m):
    a, b = map(int, fin.readline().strip().split() )
    out_n[n+b].append(a)
    in_n[a].append(n+b)

"""
print(f"{n=}, {m=}")
for a in range(n):
    print(f"dal nodo {a} escono i seguenti archi:")
    print(" ".join([str(b) for b in out_n[a]]))
    print(f"nel nodo {a} entrano i seguenti archi:")
    print(" ".join([str(x) for x in in_n[a]]))
"""

# BEGIN: se c'è un ciclo stampo il matching differenza simmetrica

opened = [False] * (2*n)
closed = [False] * (2*n)
eletto = [False] * (2*n)
C = []
def dfs(v, papi):
    global C, opened, closed, eletto
    #print(f"called dfs({v=}, {papi=})")
    if opened[v]:
        if closed[v]:
            return
        else:
            if len(C) == 0:
                C = [ (papi, v) ]
                z = v
                while z != papi:
                    C.append((z, eletto[z]))
                    z = eletto[z]
            return
    opened[v] = True
    for next_v in out_n[v]:
        eletto[v] = next_v
        dfs(next_v, v)
    closed[v] = True

for v in range(n):
    if not opened[v]:
        dfs(v, v)

#print(C)

if len(C) != 0:
    for i, arc in enumerate(C):
        if i % 2 == 0:
            femmina = arc[0]
            assert femmina >= n
            maschio = arc[1]
            assert maschio < n
            out_n[ maschio ][0] = femmina
    for u in range(n):
        print(f"{u} {out_n[u][0] - n}")

    exit(0)
# END: se c'è un ciclo stampo il matching differenza simmetrica
print("-1")
exit(0)
