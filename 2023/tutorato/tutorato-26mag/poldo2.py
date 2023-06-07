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

M = [0 for _ in range(N)]

for i in reversed(range(N)):
    sol = 0

    for j in range(i + 1, N):
        if P[j] < P[i]:
            sol = max(sol, M[j])
    M[i] = sol + 1


soluzione = max(M)

output_file = open("output.txt", "w")
print(soluzione, file=output_file)