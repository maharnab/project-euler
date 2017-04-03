# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 21:22:29 2016

@author: Maharnab

Power Digit Sum
Sum of the digits in 2**1000
"""

import timing
A = 2**1000
print A
magic = lambda num: map(int, str(num))
b = magic(A)
print sum(b)