# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
closing_prices = np.loadtxt(
    '../../data/goog.csv', delimiter=',',
    usecols=(4), unpack=True, skiprows=1)
mp.figure(num='Price Distribution',
          facecolor='lightgray')
mp.title('Price Distribution', fontsize=20)
mp.xlabel('Price', fontsize=14)
mp.ylabel('Occurrence', fontsize=14)
mp.grid(axis='y', linestyle=':')
bins = mp.hist(closing_prices,
               int(np.sqrt(closing_prices.size)),
               edgecolor='indianred', facecolor='lightcoral',
               label='Price')[1]
# 设置水平坐标轴刻度
mp.xticks(bins, np.round(bins, 2), rotation=30)
mp.legend()
mp.show()
