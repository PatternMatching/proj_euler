#!/usr/local/bin/env python

import numpy as np

NUM = 2**1000

if __name__ == '__main__':
    iterable = [int(x) for x in str(NUM)]
    print np.sum(np.fromiter(iterable, np.int16))
