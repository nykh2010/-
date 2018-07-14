# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.arange(1, 9)
print(a)
b = a.reshape(2, 4)
print(b)
c = b.reshape(2, 2, 2)
print(c)
d = c.ravel()
print(d)
e = c.flatten()
print(e)
a += 10
print(a, b, c, d, e, sep='\n')
f = a.reshape(2, 4).copy()
print(f)
a -= 10
print(f)
a.shape = (2, 2, 2)
print(a)
a.resize((2, 4))
print(a)
#a.resize((3, 5))
g = np.resize(a, (3, 5))
print(g)
# h = a.transpose()
h = a.T
print(h)
a += 10
print(h)
print(np.array([d]).T)
print(d.reshape(-1, 1))


