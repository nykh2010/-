# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.array([10, -4, 20, 30, -7, -6, 0])
b = np.sign(a)
print(b)
b = np.piecewise(a, [a < 0, a > 0], [-1, 1])
print(b)
