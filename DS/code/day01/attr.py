# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.array([
    [1+1j, 2+4j, 3+7j],
    [4+2j, 5+5j, 6+8j],
    [7+3j, 8+6j, 9+9j]])
print(a.dtype)
print(a.shape)
print(a.ndim)
print(a.size)
print(a.itemsize)
print(a.nbytes)
print(a.T)
print(a.real)
print(a.imag)
print([elem for elem in a.flat])
b = a.tolist()
print(b)
c = np.array(b)
print(c)