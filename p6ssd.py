# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 03:59:39 2016

@author: Maharnab

Difference between the sum of the squares of the 
first n natural numbers and the square of the sum
"""



n = int(raw_input())
import timing

Ssq = (n*(n + 1)*((2*n) + 1)) / 6
Sn = (n*(n + 1)) / 2
SS = Sn**2
diff = SS - Ssq

print diff

