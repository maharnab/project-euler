# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 21:14:03 2016

@author: Maharnab

The sum of all the primes below N.
"""

import numpy as np

N = int(raw_input())
import timing
i = 3

def primesfrom3to(N):
    sieve = np.ones(N/2, dtype=np.bool)
    for i in xrange(3, int(N**0.5)+1, 2):
        if sieve[i / 2]:
            sieve[i*i / 2::i] = False
    return 2*np.nonzero(sieve)[0][1::]+1
    
k = primesfrom3to(N)
k = np.insert(k, 0, 2)
print np.sum(k)