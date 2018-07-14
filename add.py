import numpy as np

a = np.arange(1,7)
print(a)

b = np.add.reduce(a)                   # 数组求和
print(b)

c = np.add.accumulate(a)               # 记录求和过程
print(c)

d = np.add.reduceat(a, [0,2,4])        # 以 0,2,4下标作为分界线进行分段求和
print(d)

e = np.add.outer([10,20,30],a)         # 求外和，10和[1 2 3 4 5 6]相加，20和[1 2 3 4 5 6]，30和[1 2 3 4 5 6]
print(e)

f = np.outer([10,20,30],a)             # 外积，10和[1 2 3 4 5 6]相乘，20和[1 2 3 4 5 6]，30和[1 2 3 4 5 6]
print(f)
