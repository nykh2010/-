from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

n = 1000

x,y = np.meshgrid(np.linspace(-3,3,n),np.linspace(-3,3))

z = (1-x/2+x**5+y**3)*np.exp(-x**2 - y**2)

ax = mp.gca(projetion = '3d')
mp.title('3D Wireframe', fontsize=20)
ax.set_xlabel('x',fontsize=14)
ax.set_ylabel('y',fontsize=14)
ax.set_zlabel('z',fontsize=14)

mp.tick_params(labelsize=10)

ax.plot_wireframe(x,y,z,rstride=10,cstride=10,color='blue')