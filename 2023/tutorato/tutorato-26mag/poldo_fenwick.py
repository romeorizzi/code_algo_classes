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
F = [0 for _ in range(N + 1)]


def query(F, x):
    sol = 0
    while x > 0:
        sol = max(sol, F[x])
        x -= x & -x
    return sol

def update(F, x, val):
    while x < len(F):
        F[x] = max(F[x], val)
        x += x & -x

X = [(P[i], i) for i in range(N)]
X.sort()

I = [0 for _ in range(N)]
for i in range(N):
    I[X[i][1]] = i + 1


for i in reversed(range(N)):

    el_fen = I[i]
    sol = query(F, el_fen)
    M[i] = sol + 1
    update(F, el_fen, M[i])


soluzione = max(M)

output_file = open("output.txt", "w")
print(soluzione, file=output_file)


# 0 1 2 3 4 5 6 7
# 3 6 4 8 2 9 4 2

# 2 2 3 4 4 6 8 9 
# 4 7 0 2 6 1 3 5

# 0 1 2 3 4 5 6 7
# 3 6 4 7 0 8 6 1


# 1 1 2 2 2 3 3 3