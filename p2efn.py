# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 22:09:17 2016

@author: Maharnab

Fibonacci sequence with values not exceeding maximum N 
Sum of all even-valued terms in the Fibonacci sequence
"""
import time

N = int(raw_input())
start_time = time.time()
n1 = 0
n2 = 1
#farr = [n1, n2]
feva = []

while n2 < N:
    nth = n1 + n2
#    farr.append(nth)
    if not (nth%2):
        feva.append(nth)
    n1 = n2
    n2 = nth
    
#print farr              #Fibonacci Sequence
#print feva              #Fibonacci Sequence of even values
print sum(feva)
print("--- %s seconds ---" % (time.time() - start_time))
