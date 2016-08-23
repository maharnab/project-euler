# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 13:03:47 2016

@author: Maharnab

Smallest positive number that is evenly divisible 
by all numbers from 1 to n
"""
import time

n = int(raw_input())
start_time = time.time()

sn = 2
i = 1
iar = []

while i <= n:
    print sn
    if (sn % i) != 0:  
        for j in iar:
            if i % j == 0:
                print  i, j, '---'
                sn *= j
                break
        if i not in iar:
            iar.append(i)
    else:
        if i not in iar:
            iar.append(i)
        i += 1    
    
print iar       
print("--- %s seconds ---" % (time.time() - start_time))