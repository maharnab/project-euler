# -*- coding: utf-8 -*-
"""
Created on Sun May 01 02:07:30 2016

@author: Maharnab
"""

n = int(raw_input())
fibseq = [1, 2]

for i in range(2, n):
    fib = fibseq[i-1] + fibseq[i-2]
    fibseq.append(fib)
    
print fibseq