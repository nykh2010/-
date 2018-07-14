from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(-np.pi, np.pi, 200)
cos_y = np.cos(x) / 2
sin_y = np.sin(x) / 2

#用直线连接曲线上的各点
mp.plot(x, cos_y)
mp.plot(x, sin_y)

mp.show()
