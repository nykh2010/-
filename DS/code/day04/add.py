# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.arange(1, 7)
print(a)
# 累加
b = np.add.reduce(a)
print(b)
c = np.add.accumulate(a)
print(c)
# 分段累加
d = np.add.reduceat(a, [0, 2, 4])
print(d)
# 外和
#   | 1  2  3  4  5  6
# --+-----------------
# 1 | 2  3  4  5  6  7
# 2 | 3  4  5  6  7  8
# 3 | 4  5  6  7  8  9
# 4 | 5  6  7  8  9 10
# 5 | 6  7  8  9 10 11
# 6 | 7  8  9 10 11 12
#
e = np.add.outer(a, a)
print(e)
# 外积
f = np.outer(a, a)
print(f)
