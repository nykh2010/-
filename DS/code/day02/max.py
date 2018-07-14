# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
# numpy.random随机数模块，
# 其中randint函数生成随机数数组：
# randint(下边界, 上边界, 维度)
a = np.random.randint(10, 100, (3, 3))
print(a)
b = np.max(a)
print(b)
c = np.min(a)
print(c)
print(b - c, np.ptp(a))
d = np.random.randint(10, 100, (3, 3))
print(d)
e = np.maximum(a, d)
print(e)
f = np.minimum(a, d)
print(f)
