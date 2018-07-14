# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d
x = np.linspace(-2.5, 2.5, 501)
y = np.linspace(-2.5, 2.5, 501)
z = np.sinc(np.outer(x, y))
ax = mp.gca(projection='3d')
mp.title('3D Wireframe', fontsize=20)
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_zlabel('z', fontsize=14)
mp.tick_params(labelsize=10)
x, y = np.meshgrid(x, y)
ax.plot_wireframe(x, y, z, rstride=30, cstride=30,
                  color='orangered')
mp.show()
