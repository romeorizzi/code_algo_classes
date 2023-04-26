#!/usr/bin/env python3
# -*- coding: latin-1 -*-
"""
 *  ricorsione pura in una fase, insieme 2023-04-16
"""
from sys import stderr

T = int(input())
for _ in range(T):
    num_figli = list(map(int, input().strip().split()))
    #print(f"\n\n{num_figli=}", file = stderr)

    pos_R = 0
    def specchio():
        global pos_R
        memorize_num_figli = num_figli[pos_R]; pos_R += 1
        risp = ""
        for _ in range(memorize_num_figli):
            risp = specchio() + risp
        risp = f"{memorize_num_figli} " + risp
        return risp

    def specchio_leonardo_da_vinci():
        global pos_R
        memorize_num_figli = num_figli[pos_R]; pos_R += 1
        risp = f"{memorize_num_figli} "
        for _ in range(memorize_num_figli):
            risp += specchio_leonardo_da_vinci()
        return risp
    
    pos_R = 0
    print(specchio())    
    pos_R = 0
    print(specchio_leonardo_da_vinci()[::-1])    
