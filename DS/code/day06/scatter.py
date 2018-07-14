# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d
closing_prices, volumes = np.loadtxt(
    '../../data/goog.csv', delimiter=',',
    usecols=(4, 6), unpack=True, skiprows=1)
closing_price_rates = np.diff(closing_prices) / \
    closing_prices[:-1]
volume_rates = np.diff(volumes) / volumes[:-1]
ax = mp.gca(projection='3d')
mp.title('Price-Volume', fontsize=20)
ax.set_xlabel('Price', fontsize=14)
ax.set_ylabel('Volume', fontsize=14)
ax.set_zlabel('Price Rate', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
ax.scatter(closing_prices[:-1], volumes[:-1],
           closing_price_rates, s=80,
           c=volume_rates, cmap='prism',
           label='Price-Volume')
mp.legend()
mp.show()
