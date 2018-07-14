from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d
import matplotlib.animation as ma

n_samples = 100

data = np.zeros(n_samples, dtype=[
    ('position',float,2),
    ('size',float,1),
    ('growth',float,1),
    ('color',float,4)])
# dtype=[(字段名称,字段类型,字段维度)]

data['position'] = np.random.uniform(0,1,(n_samples,2))
data['size'] = np.random.uniform(50,750,n_samples)
data['growth'] = np.random.uniform(30,150,n_samples)
data['color'] = np.random.uniform(0,1,(n_samples,4))

mp.figure('Bubble',facecolor='lightgray')
mp.title('Bubble',fontsize=20)
mp.xlabel('x',fontsize=14)
mp.ylabel('y',fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
plot = mp.scatter(data['position'][:,0],data['position'][:,1],s=data['size'],c=data['color'])
# 用plot来接收函数的返回值，就是所有点的对象

def update(number):
    data['size'] += data['growth']
    index = number % n_samples
    data['position'][index] = np.random.uniform(0,1,2)
    data['size'][index] = 0
    data['growth'][index] = np.random.uniform(30,150)
    data['color'][index] = np.random.uniform(0,1,4)
    plot.set_offsets(data['position'])
    plot.set_sizes(data['size'])
    plot.set_facecolors(data['color'])

anim = ma.FuncAnimation(mp.gcf(), update, interval=10)
# 如果不用变量名去接收函数的返回，那么函数里的变量为临时变量，接收返回之后生命周期变长

mp.show()