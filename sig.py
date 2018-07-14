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

mp.figure('Signal',facecolor='lightgray')
mp.title('Signal',fontsize=20)
mp.xlabel('Time',fontsize=14)
mp.ylabel('Signal',fontsize=14)
ax = mp.gca()
ax.set_ylim(-1.1,1.1)
ax.set_xlim(0,10)
mp.tick_params(lable_size=10)
mp.grid(linestyle=':')

plot = mp.plot([],[],c='orangered')
# 用plot来接收函数的返回值，就是所有点的对象
plot.set_data([],[])

def update(data):   # 绘制函数 
    t,v = data
    x,y = plot.get_data()
    x.append(t)
    y.appent(v)

    x_min,x_max = ax.get_xlim()
    if t >= x_max:
        ax.set_xlim(x_min,x_max*2)
        ax.figure.canvas.draw()
    
    plot.set_data(x,y)

def generator():
    t = 0
    for i in range(10000):
        v = np.sin(2 * np.pi) * np.exp(-t/8)
        yield t,v
        t += 0.05

anim = ma.FuncAnimation(mp.gcf(), update, generator, interval=10)
# 如果不用变量名去接收函数的返回，那么函数里的变量为临时变量，接收返回之后生命周期变长

mp.show()