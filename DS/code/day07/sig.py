# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma
mp.figure(num='Signal', facecolor='lightgray')
mp.title('Signal', fontsize=20)
mp.xlabel('Time', fontsize=14)
mp.ylabel('Signal', fontsize=14)
ax = mp.gca()
ax.set_xlim(0, 10)
ax.set_ylim(-1.1, 1.1)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
line = mp.plot([], [], c='orangered')[0]
line.set_data([], [])


def update(data):
    t, v = data
    x, y = line.get_data()
    x.append(t)
    y.append(v)
    x_min, x_max = ax.get_xlim()
    if t >= x_max:
        ax.set_xlim(x_min, 2 * x_max)
        ax.figure.canvas.draw()
    line.set_data(x, y)
    return line


def genertor():
    t = 0
    for i in range(10000):
        v = np.sin(2 * np.pi * t) * np.exp(-t / 8)
        yield t, v
        t += 0.05


anim = ma.FuncAnimation(mp.gcf(), update, genertor,
                        interval=5, blit=False, repeat=False)
mp.show()
