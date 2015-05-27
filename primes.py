from __future__ import division
from numpy import *

def primes(n):
    x, primelist = 3, []
    
    while n % 2 == 0:
        primelist.append(2)
        n /= 2
    
    while x * x <= n:
        while n % x == 0:
            primelist.append(x)
            n /= x
            x += 2
            
    if n > 1: primelist.append(n)
    return primelist       
        