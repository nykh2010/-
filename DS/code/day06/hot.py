# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
x = np.linspace(-3, 3, 256)
y = np.linspace(-3, 3, 256)
x, y = np.meshgrid(x, y)
z = (1 - x / 2 + x ** 5 + y ** 3) * np.exp(
    -x ** 2 - y ** 2)
mp.figure(num='Hot', facecolor='lightgray')
mp.title('Hot', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.imshow(z, origin='low', cmap='jet')
mp.colorbar()
mp.show()
