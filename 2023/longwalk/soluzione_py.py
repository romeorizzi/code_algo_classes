#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv, stdin, stderr, stdout

filename = 'input.txt'

if len(argv) > 1:
    filename = argv[1]

if filename == 'stdin':
    fin = stdin
else:
    fin = open(filename, "r")

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
opened = [None] * n
closed = [None] * n

def dfs(v, dad):
    global time, opened, closed
    if opened[v] is not None:
        if opened[v] > opened[dad]: # cycle found!
            pass
    else:
        opened[v] = time; time += 1
        for next_v in out_n[v]:
            dfs(next_v, v)
        closed[v] = time; time += 1

for v in range(n):
    if opened[v] is None:
        dfs(v, v)
        
print(f"{closed=}")
            
with open("output.txt", "w") as fw:
    fw.write(str(n) + "\n")
