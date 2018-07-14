from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md

a = np.arange(1,6)
print(a)
b = a.clip(min=2)
print(b)
c = a.clip(max=4)
print(c)
d = a.clip(2, 4)
print(d)
e = a.compress(2 <= a)
print(e)
g = a.compress((a >= 2) & (a <= 4))		# &运算符优先级高于 >= 和 <=
print(g)
h = a.prod()	# 所有元素相乘
print(h)

print(np.arange(1,11).prod())		# 10的阶乘
j = a.cumprod()			# 累乘的过程
print(j)