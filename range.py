from __future__ import unicode_literals
import numpy as np

path = r'C:\Users\xulingfeng\Desktop\python学习\数学分析\DS\data\aapl.csv'

highest_prices,\
lowest_prices = np.loadtxt(path,delimiter=',',
	usecols = (4,5),
	unpack = True)

max_highest_price, min_highest_price = \
highest_prices[0],highest_prices[0]

max_lowest_price, min_lowest_price =\
lowest_prices[0], lowest_prices[0]

for highest_price, lowest_price in zip(highest_prices,lowest_prices):
	if highest_price > max_highest_price:
		max_highest_price = highest_price
	if highest_price < min_highest_price:
		min_highest_price = highest_price
	if lowest_price > max_lowest_price:
		max_lowest_price = lowest_price
	if lowest_price < min_lowest_price:
		min_lowest_price = lowest_price

price_range = max_highest_price - min_lowest_price
print(price_range)

# 用 numpy 里的函数
max_highest_price = highest_prices.max()
min_lowest_price = lowest_prices.min()

# 原始方法求价格幅度
high_spread = max_highest_price - min_highest_price
low_spread = max_lowest_price - min_lowest_price

# 用 numpy 里的函数
high_spread = np.ptp(highest_prices)
low_spread = np.ptp(lowest_prices)

print(high_spread)
print(low_spread)