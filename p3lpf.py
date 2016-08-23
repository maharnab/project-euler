# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 23:02:14 2016

@author: Maharnab

Largest Prime Factor of a given number
"""
import time

N = int(raw_input())
start_time = time.time()
pfar = []
i = 2

while i*i <= N:
    while (N % i) == 0:
        pfar.append(i)
        N //= i             #eqv to N = N // i, assign floor to left
    i += 1
if N>1:
    pfar.append(N)
        
print max(pfar)
print("--- %s seconds ---" % (time.time() - start_time))
