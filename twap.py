from __future__ import unicode_literals
import numpy as np
import datetime as dt
import matplotlib.pyplot as mp

path = r'C:\Users\xulingfeng\Desktop\python学习\数学分析\DS\data\aapl.csv'

def dmy2days(dmy):
	dmy = str(dmy,encoding='utf-8')
	date = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
	days = (date - dt.date.min).days    # dt.date.min 最小日期，算出时间差，用天数显示
	return days

days, closing_prices = np.loadtxt(
	path,
	delimiter = ',',
	usecols = (1,6),
	unpack = True,
	converters = {1:dmy2days})

twap, sw = 0, 0
for closing_price, day in zip(closing_prices, days):
	twap += closing_price * day
	sw += day
twap /= sw
print(twap)


twap = closing_prices.dot(days) / days.sum()
print(twap)

twap = np.average(closing_prices, weights=days)
print(twap)