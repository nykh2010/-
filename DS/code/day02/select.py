# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.arange(1, 10)
print(a)
b = a % 2 == 0
print(b)
c = a[b]
print(c)
a[a % 2 == 0] *= 10
print(a)
a[(30 <= a) & (a <= 70)] **= 2
print(a)
d = np.arange(1, 10)
print(d)
e = np.where(d % 2 == 0)[0]
print(e)
f = np.take(d, e)
print(f)
d[np.where(d % 2 == 0)[0]] *= 10
print(d)
# 用下标数组作数组的下标，获取
# 数组中下标在下标数组中的元素
d[[1, 3, 5, 7]] = d[[7, 5, 3, 1]]
print(d)
