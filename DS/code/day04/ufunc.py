# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np


def func(a, b):
    c = a + b
    d = a - b
    e = a * b
    return c, d, e


A = np.array([1, 2, 3, 4, 5])
B = np.array([5, 4, 3, 2, 1])
ufunc = np.frompyfunc(func, 2, 3)
C, D, E = ufunc(A, B)
print(C, D, E, sep='\n')


def func1(a):
    def func2(b):
        c = a + b
        d = a - b
        e = a * b
        return c, d, e
    return np.frompyfunc(func2, 1, 3)


ufunc = func1(100)
C, D, E = ufunc(A)
print(C, D, E, sep='\n')








