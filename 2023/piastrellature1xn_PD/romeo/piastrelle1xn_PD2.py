#!/usr/bin/python

memo_risp = [None] * 3
memo_risp[0] = memo_risp[1] = 1

N = int(input("N="))

for n in range(2, N + 1):
    memo_risp[n % 3] = memo_risp[(n - 1) % 3] + memo_risp[(n - 2) % 3]

print(f"Le piastrellature sono {memo_risp[n%3]}.")
