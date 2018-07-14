import numpy as np 
a = np.matrix([
	[1,2,6],
	[3,5,7],
	[4,8,9]])
print(type(a))

a = np.array([
	[1,2,6],
	[3,5,7],
	[4,8,9]])
print(type(a))

b = np.matrix(np.array([1,2,6,3,5,7,4,8,9])).reshape(3,3)
print(b)

c = np.matrix('1 2 6; 3 5 7; 4 8 9')
print(c)

d = c
e = np.mat(d)
f = np.matrix(e, copy=False)
g = np.matrix(f)

c[1,1] = 0
print(c)	# 0
print(d)    # 0
print(e)    # 0
print(f)	# 0
print(g)	# 5

print(g.T)
print(g.I)
print(g.I * g)
print(g ** 2)

h = np.array(g)
print(h ** 2)

i = np.ones((3,3))
print(i)
j = i*2
print(j)
k = i*3
print(k)
l = i*4
print(l)
m = np.bmat('i j; k l')
print(m)