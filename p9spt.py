# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 23:02:17 2016

@author: Maharnab

A Pythagorean triplet is a set of 3 natural numbers, a < b < c, for which,
            a**2 + b**2 = c**2
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
To find the product abc.
"""

#k = []
import timing
for a in range(1, 1000):
    for b in range(a+1, 1000):
        for c in range(b+1, 1000):
            if a+b+c == 1000:
                if a < b < c:               
                    if a**2 + b**2 == c**2 :
                        l = a * b * c                                            
#                        k.append([a, b, c])
                        break
                else:
                    break
            
#print k
print l             

