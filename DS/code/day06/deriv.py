# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
x = np.linspace(-10, 10, 201)
# y = x^3 + 2x^2 + 3x + 4
# y = x ** 3 + 2 * x ** 2 + 3 * x + 4
f = np.poly1d([1., 2., 3., 4.])
y = f(x)
# m: 微分阶数
df = f.deriv(m=1)
dy = df(x)
mp.figure(num='Polynomial & Derivative',
          facecolor='lightgray')
mp.title('Polynomial & Derivative', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel("y/y'", fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# 绘制曲线
mp.plot(x, y, c='dodgerblue',
        label=r'$y=x^3+2x^2+3x+4$')
mp.plot(x, dy, c='limegreen',
        label=r"$y'=\frac{d(x^3+2x^2+3x+4)}{dx}$")
mp.legend()
mp.show()
