import numpy as np

def fun(a,b):
	x = a + b
	y = a - b
	z = a * b
	return x,y,z

a = 10
b = 20
x, y, z = fun(a,b)
print(x,y,z)

A = [10,100,1000]
B = [20,200,2000]
X,Y,Z = np.vectorize(fun)(A,B)
print(X,Y,Z)