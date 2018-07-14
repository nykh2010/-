# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.array((
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)))
print(a)
print(a.dtype)
a += 10
print(a)
print(len(a), a.size, a.shape)
b = a.reshape(9,)
print(b)
b[0] -= 1
print(b)
print(a)
c = a.astype(str)
print(c)
a[0][0] += 1
print(a)
print(c)
