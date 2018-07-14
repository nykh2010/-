# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.arange(1, 13).reshape(6, 2)
print(a)
b = np.vsplit(a, 3)
print(b)
c = a.T
print(c)
d = np.hsplit(c, 3)
print(d)
e = np.arange(11, 20).reshape(3, 3)
print(e)
f = np.arange(21, 30).reshape(3, 3)
print(f)
g = np.dstack((e, f))
print(g)
h = np.dsplit(g, 2)
print(h[0].T[0].T)
print(h[1].T[0].T)
