# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
# 从-pi到pi平均分割成200份，取201个点
t = np.linspace(-np.pi, np.pi, 201)
#A, a, B, b = 10, 1, 5, 1
#A, a, B, b = 10, 1, 5, 2
A, a, B, b = 10, 9, 5, 8
x = A * np.sin(a * t + np.pi / 2)
y = B * np.sin(b * t)
mp.figure(num='Lissajous', facecolor='lightgray')
mp.title('Lissajous', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(x, y, c='orangered', label='Lissajous')
mp.legend()
mp.show()