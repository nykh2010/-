from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp

path = r'C:\Users\xulingfeng\Desktop\python学习\数学分析\DS\data\aapl.csv'

closing_prices, volumes = np.loadtxt(
	path,
	delimiter=',',
	usecols=(6,7),
	unpack=True)

vwap, sw = 0, 0
for closing_price, volume in zip(closing_prices, volumes):
	vwap += closing_price * volume
	sw += volume
vwap /= sw
print(vwap)

vwap = closing_prices.dot(volumes) / volumes.sum()
print(vwap)

vwap = np.average(closing_prices, weights=volumes)
print(vwap)