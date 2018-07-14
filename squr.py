import numpy as np
import matplotlib.pyplot as mp

def squarewave(N):
    k = np.arange(1, N+1)
    def f(x):
        return 4 / np.pi * np.sum(np.sin((2*k -1) * x)/(2*k - 1))
    return np.frompyfunc(f, 1, 1)

def sawtoothwave(N):
    k = np.arange(1, N+1)
    def f(x):
        return -2 / np.pi * np.sum(np.sin(2*k * np.pi * x)/k)
    return np.frompyfunc(f, 1, 1)


x = np.linspace(0, 2*np.pi, 201)
y1 = squarewave(1)(x)
y2 = squarewave(2)(x)
y3 = squarewave(10)(x)
y4 = squarewave(100)(x)
y5 = squarewave(1000)(x)
y6 = sawtoothwave(1000)(x)

mp.figure('Lissajous',facecolor='lightgray')
mp.title('Lissajous', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(x,y1,label='N=1')
mp.plot(x,y2,label='N=2')
mp.plot(x,y3,label='N=10')
mp.plot(x,y4,label='N=100')
mp.plot(x,y5,label='N=1000')
mp.plot(x,y6,label='sawtoothwave')
mp.legend()
mp.show()