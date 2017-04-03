# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 12:41:03 2016

@author: Maharnab

The n-th prime number
"""


n = int(raw_input())
import timing

pn = [2]
i = 3

#generate prime numbers
while len(pn) < n:
    if all(i % j != 0 for j in pn):
            pn.append(i)
    i += 2
            
print pn[n-1]           