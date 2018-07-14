# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np


def func(x, y):
    return x + y, x - y, x * y


a = np.arange(1, 6)
print(a)
b = np.arange(6, 11)
print(b)
c = np.vectorize(func)(a, b)
print(c)
