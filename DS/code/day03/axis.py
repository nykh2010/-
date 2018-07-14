# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.arange(1, 10)
print(a)
# b = np.split(a, 3)
b = a.reshape(3, 3)
print(b)


def func(c):
    print(c)
    d = c ** 2
    return d


e = np.apply_along_axis(func, 0, b)
print(e)
