import numpy as np
import scipy.integrate as si
import matplotlib.pyplot as mp
import matplotlib.patches as mc

def f(x):
    y = 2*x ** 2 + 3 * x + 4
    return y

a,b = -5,5
x1 = np.linspace(a, b, 1001)
y1 = f(x1)
n = 120
x2 = np.linspace(a, b, n+1)
y2 = f(x2)
area = 0
for i in range(n):
    area += (y2[i] + y2[i+1]) * (x2[i+1]-x2[i])/2
print(area)
area = si.quad(f,a,b)[0]        # 求定积分
print(area) 

mp.figure('Integral', facecolor='lightgray')
mp.title('Integral', fontsize=16)
mp.xlabel('x', fontsize=12)
mp.ylabel('y', fontsize=12)
mp.tick_params(labelsize=12)
mp.grid(linestyle=':')
mp.plot(x1, y1, c='orangered', label=r'$y=2x**2 + 3 + 4')
for i in range(n):
    mp.gca().add_patch(mc.Polygon([[x2[i],0], [x2[i],y2[i]], [x2[i+1],y2[i+1]], [x2[i+1],0]], fc='deepskyblue', ec='dodgerblue', alpha=0.5))
mp.legend()
mp.show()