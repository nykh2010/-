# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.array([50, 40, 30, 40, 20])
print(a)
b = np.array([100, 300, 500, 200, 600])
print(b)
c = np.lexsort((b, a))
print(c)
print(a[c])
print(b[c])
d = a + b * 1j
print(d)
e = np.sort_complex(d)
print(e)
f = np.array([12, 23, 11, 17, np.NaN, 19, 29])
print(np.argmax(f))
print(np.argmin(f))
print(np.max(f))
print(np.min(f))
print(np.nanargmax(f))
print(np.nanargmin(f))
# 被插入的有序数组
#             0  1  2  3  4  5  6
g = np.array([1, 2, 4, 5, 6, 8, 9])
# 插入数组
h = np.array([3, 7])
# 将h数组中的元素插入g数组的哪
# 些位置，所得到的数组依然有序？
i = np.searchsorted(g, h)
print(i)
j = np.insert(g, i, h)
print(j)
# 生成位于[10, 100)区间内的20个符合平均分布的随机整数
k = np.random.randint(10, 100, 20)
print(k)
print(k[k % 2 == 0])
print(k[np.where(k % 2 == 0)])
print(np.take(k, np.where(k % 2 == 0)[0]))
print(np.extract(k % 2 == 0, k))
# 生产单位矩阵
l = np.eye(3, 3)
print(l)
m = np.nonzero(l)
print(m)
print(np.array(m).T)
print(l[m])
