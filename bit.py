import numpy as np

a = np.arange(-5,6)
b = -a
print(a,-b)

c = a ^ b
d = a.__xor__(b)
e = np.bitwise_xor(a,b)
print(c,d,e)

f = np.arange(1, 21)
g = f-1
h = f & g
i = f.__and__(g)
j = np.bitwise_and(f,g)
print(f[np.where(h==0)])