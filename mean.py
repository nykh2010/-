from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp

path = r'C:\Users\xulingfeng\Desktop\python学习\数学分析\DS\data\aapl.csv'

closing_prices = np.loadtxt(
	path,
	delimiter = ',',
	usecols = (6),
	unpack = True)
# print(type(closing_prices))

mean = 0
for closing_price in closing_prices:
	mean += closing_price
mean /= closing_prices.size
print(mean)

mean = closing_prices.sum() / closing_prices.size
print(mean)

mean = np.mean(closing_prices)
print(mean)