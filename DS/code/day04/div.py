# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.array([5, 5, -5, -5])
b = np.array([2, -2, 2, -2])
print(a, b)
# 真除
c = np.true_divide(a, b)
d = np.divide(a, b)
e = a / b
print(c, d, e)
# 地板除
f = np.floor_divide(a, b)
g = a // b
print(f, g)
# 天花板除
h = np.ceil(a / b).astype(int)
print(h)
# 截断除
i = np.trunc(a / b).astype(int)
print(i)
# 地板模
j = np.remainder(a, b)
k = np.mod(a, b)
l = a % b
print(j, k, l)
# 截断模
m = np.fmod(a, b)
print(m)
print(k + g * b, m + i * b)
