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

MAXP = max(P)

M = [[0 for _ in range(MAXP+2)] for _ in range(2)]

for n in reversed(range(N)):
    for p in range(MAXP+2):
        sol1 = 0
        if P[n] < p:
            sol1 = M[(n + 1) % 2][P[n]] + 1
        sol2 = M[(n + 1) % 2][p]
        M[n % 2][p] = max(sol1, sol2)

sol = M[0][MAXP + 1]

output_file = open("output.txt", "w")
print(sol, file=output_file)