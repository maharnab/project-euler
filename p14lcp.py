# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 11:07:40 2016

@author: Maharnab

Which starting number, under one million, produces the longest chain?
Collattz Chain
"""

import numpy as np

N = 1000000
import timing
a = np.arange(1, N, 1, dtype='int64')
sa = []
lt = []
for i in a:
#    terms = []
    step = 1
    j = i
    while i != 1:
        if i%2 == 0:
            i = i/2        
        else:
            i = 3*i + 1 
    
        step += 1
#        terms.append(i)
    sa.append([j, step])
#    print j, step, terms
    lt.append(step)
#    print j

#print sa
l = max(lt)
for sublist in sa:
    if sublist[1] == l:
        print sublist
        break
#k = max(ssa[1] for ssa in sa)
#for ssa in sa:
#    if k in ssa:
#       print ssa[0], k
#       break
#print len(terms)
