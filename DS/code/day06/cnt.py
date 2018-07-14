# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
x = np.linspace(-3, 3, 256)
y = np.linspace(-3, 3, 256)
x, y = np.meshgrid(x, y)
z = (1 - x / 2 + x ** 5 + y ** 3) * np.exp(
    -x ** 2 - y ** 2)
mp.figure(num='Contour', facecolor='lightgray')
mp.title('Contour', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.contourf(x, y, z, 8, alpha=0.75, cmap='jet')
cnt = mp.contour(x, y, z, 8, colors='black',
                 linewidths=0.5)
mp.clabel(cnt, inline=1, fontsize=10)
mp.show()
