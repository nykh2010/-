# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np


def fibo(n):
    return 1 if n < 3 else fibo(n - 2) + fibo(n - 1)


n = 35
print(fibo(n))
f2, f1 = 1, 0
for i in range(n):
    fn = f2 + f1
    f2, f1 = f1, fn
print(fn)
print(int((np.mat('1. 1.; 1. 0.') ** (n - 1))[0, 0]))
r = np.sqrt(5)
print(int((((1+r)/2)**n-((1-r)/2)**n)/r))