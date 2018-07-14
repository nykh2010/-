# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.arange(1, 3)
print(a)
print(a.shape)
b = np.array([
    [1, 2, 3],
    [4, 5, 6]])
print(b)
print(b.shape)
c = np.array([
    [np.arange(1, 5),
     np.arange(5, 9),
     np.arange(9, 13)],
    [np.arange(13, 17),
     np.arange(17, 21),
     np.arange(21, 25)]])
print(c)
print(c.shape)
