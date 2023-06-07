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

M = [[None for _ in range(10001)] for _ in range(N)]

def poldo(n, p):

    if n == len(P):
        return 0
    
    if M[n][p] is not None:
        return M[n][p]

    sol1 = 0

    if P[n] < p:
        sol1 = poldo(n + 1, P[n]) + 1

    sol2 = poldo(n + 1, p)

    M[n][p] = max(sol1, sol2)
    print(f"Sol {n}/{p} => {M[n][p]}")
    return M[n][p]

sol = poldo(0, 10000)

output_file = open("output.txt", "w")
print(sol, file=output_file)