#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv, stdin, stderr, stdout, setrecursionlimit

filename = 'input.txt'

if len(argv) > 1:
    filename = argv[1]

if filename == 'stdin':
    fin = stdin
    fout = stdout
else:
    fin = open(filename, "r")
    fout = open("output.txt", "w")

n, r = map(int, fin.readline().strip().split() )

ft = [0] * (n + 1)

def len_fwk_interval(i):
    return i & (-1)


def query(a, b):
    prefix_sum(b) - prefix_sum(a)

def prefix_sum(i):
    # return ft[i] + prefix_sum(i - len_fwk_interval(i) )
    risp = 0
    while i >= 0:
        risp += ft[i]
        i -= len_fwk_interval(i)
    return risp

def update(i, d):
    while i <= n:
        ft[i] + = d
        i += len_fwk_interval(i)



for i in range(r)
    r_type, a, b = map(int, fin.readline().strip().split() )
    if r_type == 0:
        print(query(a, b))
    else:
        update(i= a, d = b)
exit(0)
