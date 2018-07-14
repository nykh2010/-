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
ddf = f.deriv(m=2)
ddy = ddf(x)
mp.figure(num='Polynomial & Derivative',
          facecolor='lightgray')
# 创建子坐标图
mp.subplot(311)
mp.title('Polynomial Function', fontsize=16)
mp.ylabel('y', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(x, y, c='dodgerblue',
        label=r'$y=x^3+2x^2+3x+4$')
mp.legend()
# 创建子坐标图
mp.subplot(312)
mp.title('First Order Derivative', fontsize=16)
mp.ylabel("y'", fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(x, dy, c='limegreen',
        label=r"$y'=\frac{d(x^3+2x^2+3x+4)}{dx}$")
mp.legend()
# 创建子坐标图
mp.subplot(313)
mp.title('Second Order Derivative', fontsize=16)
mp.xlabel('x', fontsize=12)
mp.ylabel('y"', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(x, ddy, c='orangered',
        label=r"$y'=\frac{d^2(x^3+2x^2+3x+4)}{(dx)^2}$")
mp.legend()
# 紧凑布局，防止叠压
mp.tight_layout()
mp.show()
