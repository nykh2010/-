# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.arange(1, 10)
print(a)
b = a.clip(min=4)
print(b)
c = a.clip(max=6)
print(c)
d = a.clip(min=4, max=6)
print(d)
e = a.compress(4 <= a)
print(e)
f = a.compress(a <= 6)
print(f)
g = a.compress((4 <= a) & (a <= 6))
print(g)
h = 1
for i in a:
    h *= i
print(h)
j = a.prod()
print(j)
print(np.arange(1, 16).prod())
k = a.cumprod()
print(k)
