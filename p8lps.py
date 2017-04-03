# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 21:46:23 2016

@author: Maharnab

n adjacent digits in the 1000-digit number (very large N)
that have the greatest product and value of the product
"""


N = raw_input()
nn = int(raw_input())

import timing
ar = map(int, str(N))
ii = 0
l = []
while nn <= len(ar):
    ar1 = []
    k = 1
    for i in range(ii, nn):
        ar1.append(ar[i])
    for j in ar1:
        k *= j
    l.append(k)
    ii += 1
    nn += 1
    
print max(l)
