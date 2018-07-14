# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.arange(-5, 6)
print(a)
b = -a
print(b)
c = a ^ b
d = a.__xor__(b)
e = np.bitwise_xor(a, b)
print(c, d, e, sep='\n')
print(np.where(e < 0)[0])
f = np.arange(1, 21)
print(f)
g = f - 1
print(g)
h = f & g
i = f.__and__(g)
j = np.bitwise_and(f, g)
print(h, i, j, sep='\n')
print(np.where(j == 0)[0])
