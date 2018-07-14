import numpy as np

a = np.array([5,5,-5,-5])
b = np.array([2,-2,2,-2])
print(a,b)
c = np.true_divide(a,b)
d = np.divide(a,b)
e = a / b
print(c,d,e)

# 地板除
f = np.floor_divide(a,b)
g = a // b
print(f,g)

# 天花板除
h = np.ceil(a / b).astype(int)
print(h)

# 截断除
i = np.trunc(a / b).astype(int)
print(i)
j = (a/b).astype(int)
print(j)

# 地板余数
k = np.remainder(a,b)
print(k)
m = a % b
print(m)
l = np.mod(a,b)
print(l)

# 截断余数
n = np.fmod(a,b)
print(n)
