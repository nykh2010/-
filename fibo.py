import numpy as np

n = 25

# 递归方法
def fibo(n):
    if n < 3:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)
print(fibo(n))

# 循环方法
f2, f1 = 1, 0
for i in range(n):
    fn = f2 + f1
    f2, f1 = f1, fn
print(fn)

# numpy的方法
print((np.mat('1. 1.; 1. 0.') ** (n-1))[0,0])

print((((1+np.sqrt(5))/2) ** n - (((1-np.sqrt(5))/2) ** n))/(np.sqrt(5)))