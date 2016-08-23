# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 02:26:41 2016

@author: Maharnab

Largest Palindrome number from the product of two n-digit numbers
min n is n1 and max n in n2
"""
import time

n1, n2 = raw_input().strip().split(' ')
start_time = time.time()
n1, n2 = [int(n1), int(n2)]
parr = []

for i in range(n2, n1-1, -1):
    for j in range(i, n1-1, -1):
        k = i * j
        s = str(k)
        if s == s[::-1]:
            parr.append(int(s))

print max(parr)
print("--- %s seconds ---" % (time.time() - start_time))
