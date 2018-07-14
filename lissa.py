import numpy as np
import matplotlib.pyplot as mp

t = np.linspace(0, 2 * np.pi, 201)
x = 10 * np.sin(9 * t + np.pi / 2)
y = 5 * np.sin(8 * t)

mp.figure('Lissajous',facecolor='lightgray')
mp.title('Lissajous', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(x,y,c='orangered', label='Lissajous')
mp.legend()
mp.show()