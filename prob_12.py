#!/usr/bin/env python

import numpy as np

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] 
                 for i in range(1, int(n**0.5) + 1) 
                 if n % i == 0)))

def nth_tri_num(n):
    return np.sum([x for x in range(1,n+1)])

def calc_tri_num_w_fh_factors():
    count = 0
    num_div = 0
    while num_div <= 500:
        count += 1
        tri_num = nth_tri_num(count)
        num_div = len(factors(tri_num))
    return tri_num

if __name__ == '__main__':
    print calc_tri_num_w_fh_factors()
