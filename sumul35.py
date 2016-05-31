# -*- coding: utf-8 -*-
"""
Created on Sun May 01 01:43:43 2016

@author: Maharnab
"""

T = int(raw_input())
N = []

for i in range(0, T):
    n1 = int(raw_input())
    N.append(n1)
    
for arr in N:
    mn3 = (arr - 1) // 3
    mn5 = (arr - 1) // 5
    mn15 = (arr - 1) // 15
    s3 = mn3 * (3 + (3 * mn3)) / 2
    s5 = mn5 * (5 + (5 * mn5)) / 2
    s15 = mn15 * (15 + (15 * mn15)) / 2
    s = (s3 + s5) - s15
    print s