# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
t = np.linspace(0, 4 * np.pi, 501)
r = 2 * t
#mp.figure(num='Polar', facecolor='lightgray')
ax = mp.gca(projection='polar')
mp.title('Polar', fontsize=20)
mp.plot(t, r, c='orangered', linewidth=3)
mp.show()
