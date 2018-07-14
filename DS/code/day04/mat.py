# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.matrix([
    [1, 2, 6],
    [3, 5, 7],
    [4, 8, 9]])
print(a)
b = np.matrix(np.arange(1, 10))
print(b)
c = np.matrix('1 2 6; 3 5 7; 4 8 9')
print(c)
d = c
e = np.mat(d)
f = np.matrix(e, copy=False)
g = np.matrix(f)
c[1, 1] = 0
print(c, d, e, f, g, sep='\n')
print(g.T)
print(g.I)
print(g * g.I)
h = np.array(a)
print(a)
print(h)
print(a ** 2)
print(h ** 2)
i = [[1, 1, 1],
     [1, 1, 1],
     [1, 1, 1]]
j = ((2, 2, 2),
     (2, 2, 2),
     (2, 2, 2))
k = np.ones(9).reshape(3, 3) * 3
l = np.mat('4 4 4; 4 4 4; 4 4 4')
m = np.bmat('i j; k l')
print(m)
