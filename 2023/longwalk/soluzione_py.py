#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv, stdin, stderr, stdout

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
n += 1
out_n = [ [] for _ in range(n) ]
in_n = [ [] for _ in range(n) ]
for _ in range(m):
    a, b = map(int, fin.readline().strip().split() )
    out_n[a].append(b)
    in_n[b].append(a)

"""
print(f"{n=}, {m=}")
for a in range(n):
    print(f"dal nodo {a} escono i seguenti archi:")
    print(" ".join([str(b) for b in out_n[a]]))
    print(f"nel nodo {a} entrano i seguenti archi:")
    print(" ".join([str(x) for x in in_n[a]]))
"""

time = 0
opened = [None] * n   # conterrà i valori di open dei nodi
closed = [False] * n  # dice se un nodo è stato chiuso
ts = [] # conterrà un topologcal sort dei nodi (la lista dei nodi ordinata per valore di closed crescente)
curr_child = [None] * n   # conterrà il figlio corrente per quei nodi che hanno un figlio attualmente attivo (open ma non closed)


def dfs(v, dad):
    global time, opened, closed
    if opened[v] is not None:
        if not closed[v] and opened[v] < opened[dad]: # cycle found!
            cycle = [dad, v]
            while curr_child[v] != dad:
                v = curr_child[v]
                cycle.append(v)
            print(f"-1 {len(cycle)}", file = fout)
            print(" ".join(map(str, cycle) ) )
            exit(0)
    else:
        opened[v] = time; time += 1
        for next_v in out_n[v]:
            curr_child[v] = next_v 
            dfs(next_v, v)
            curr_child[v] = None             
        closed[v] = True
        ts.append(v)

for v in range(n):
    if opened[v] is None:
        dfs(v, v)

# ts = ts[::-1]
print(f"{ts=}", file = stderr)

max_len_from = [1] * n
nxt_v = list(range(n))
global_max = 0
best_start = None
for v in ts:
    for w in out_n[v]:
        if max_len_from[v] < 1 + max_len_from[w]:
            max_len_from[v] = 1 + max_len_from[w]
            nxt_v[v] = w
            if global_max < max_len_from[v]:
                global_max = max_len_from[v]
                best_start = v
print(global_max, file = fout)
print(best_start, file = fout, end = " ")
while nxt_v[best_start] != best_start:
    best_start = nxt_v[best_start]
    print(best_start, file = fout, end = " ")
print()
exit(0)
