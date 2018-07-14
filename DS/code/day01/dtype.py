# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
# Numpy自定义的内建类型
a = np.array([12.34], dtype=np.int32)
print(a)
print(a.dtype, a.dtype.str, a.dtype.char, a.dtype.itemsize)
# Numpy自定义的泛化类型
a = np.array([12.34], dtype=np.integer)
print(a)
print(a.dtype, a.dtype.str, a.dtype.char, a.dtype.itemsize)
# Python的内建类型
a = np.array([12.34], dtype=int)
print(a)
print(a.dtype, a.dtype.str, a.dtype.char, a.dtype.itemsize)
# 类型字符串
# ABC
# A: 字节序</>/=，小端/大端/系统
# B: 类型字符i/u/f/c，整型/无符号整型/浮点/复数
# C: 字节数
a = np.array([12.34], dtype='<i4')
print(a)
print(a.dtype, a.dtype.str, a.dtype.char, a.dtype.itemsize)
a = np.array([12.34], dtype='>u2')
print(a)
print(a.dtype, a.dtype.str, a.dtype.char, a.dtype.itemsize)
# (变长类型, 长度)
a = np.array(['1234'], dtype=(np.str_, 3))
print(a.dtype, a.dtype.str, a.dtype.char, a.dtype.itemsize)
print(a)
# (定长类型, 维度)
a = np.array([(1, 2, 3, 4), (5, 6, 7, 8)],
             dtype=(np.int32, 4))
print(a.dtype, a.dtype.str, a.dtype.char, a.dtype.itemsize)
print(a.shape)
# 以逗号分隔的类型字符串
a = np.array([('ABCD', (1, 2, 3, 4))],
             dtype='U4, 4i4')
print(a.dtype, a.dtype.str, a.dtype.char, a.dtype.itemsize)
print(a)
print(a[0]['f0'])
print(a[0]['f1'][0])
print(a[0]['f1'][1])
print(a[0]['f1'][2])
print(a[0]['f1'][3])
# [(域名, 类型, 维度), ...]
a = np.array([('ABCD', ((1, 2), (3, 4)))],
    dtype=[('name', np.str_, 4), ('scores', np.int32, (2, 2))])
print(a.dtype, a.dtype.str, a.dtype.char, a.dtype.itemsize)
print(a)
print(a[0]['name'])
print(a[0]['scores'][0, 0])
print(a[0]['scores'][0, 1])
print(a[0]['scores'][1, 0])
print(a[0]['scores'][1, 1])
# (原始类型, 解释类型)
a = np.array([0x1234],
    dtype=('>u2', {'lo': ('u1', 0), 'hi': ('u1', 1)}))
print('{:x} {:x}'.format(a['lo'][0], a['hi'][0]))







