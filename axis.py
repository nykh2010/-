from __future__ import unicode_literals
import numpy as np

def fun(a):
	return a[0]+a[-1]

a = np.array([
		[1,2,3],
		[4,5,6],
		[7,8,9]
	])
b = np.apply_along_axis(fun, 0, a)
print('b')
print(b)
c = np.apply_along_axis(fun, 1, a)
print('c')
print(c)