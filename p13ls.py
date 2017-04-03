# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 11:43:37 2016

@author: Maharnab

Work out the first ten digits of the sum 
of the following one-hundred 50-digit numbers.
"""



A = 100
a = []
for a_i in xrange(A):
    a_temp = int(raw_input())
    a.append(a_temp)
    
print "-------------------------------------"
import timing
s = sum(a)
s = str(s)
print s[:10]