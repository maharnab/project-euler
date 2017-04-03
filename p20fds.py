# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 21:32:45 2016

@author: Maharnab

Factorial Digit Sum
Find the sum of digits of 100!
"""

import timing
num = 100
fact = 1
for i in range(1, num+1):
    fact = fact*i

print fact
magic = lambda num: map(int, str(num))
b = magic(fact)
print sum(b)
