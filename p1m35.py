# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 21:31:01 2016

@author: Maharnab

Sum of all the multiples of 3 and 5 below N
"""
import time

N = int(raw_input())
start_time = time.time()
marr = []

for i in range(1, N):
    if not (i%3 and i%5):
        marr.append(i)

#print marr                  #Array of multiples of 3 and 5
print sum(marr)
print("--- %s seconds ---" % (time.time() - start_time))