# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.arange(1, 6)
print(a)
b = np.arange(6, 9)
print(b)
c = np.convolve(a, b)
print(c)
d = np.convolve(a, b, 'same')
print(d)
e = np.convolve(a, b, 'valid')
print(e)
