from __future__ import unicode_literals
import numpy as np
import datetime as dt

path = r'C:\Users\xulingfeng\Desktop\python学习\数学分析\DS\data\aapl.csv'

def dmy2wday(dmy):
	dmy = str(dmy, encoding='utf-8')
	date = dt.datetime.strptime(dmy,'%d-%m-%Y').date()
	wday = date.weekday()	# 用 0 到 6 表示周一到周日
	return wday

wdays,\
opening_prices,\
highest_prices,\
lowest_prices,\
closing_prices = np.loadtxt(path,delimiter=',',
	usecols = (1,3,4,5,6),
	unpack = True,
	converters={1:dmy2wday})

wdays = wdays[:19]
opening_prices = opening_prices[:19]
highest_prices = highest_prices[:19]
lowest_prices = lowest_prices[:19]
closing_prices = closing_prices[:19]

first_monday = np.where(wdays == 0)[0][0]
last_friday = np.where(wdays == 4)[0][-1]
indices = np.arange(first_monday,last_friday+1)
indices = np.split(indices,3)

def week_summary(indices):
	opening_price = opening_prices[indices[0]]
	highest_price = np.max(np.take(highest_prices, indices))
	lowest_price = np.min(np.take(lowest_prices, indices))
	closing_price = closing_prices[indices[-1]]
	return opening_price,highest_price,lowest_price,closing_price

summeries = np.apply_along_axis(week_summary, 1, indices)
print(summeries)

np.savetxt(r'C:\Users\xulingfeng\Desktop\python学习\数学分析\DS\data\sum2.csv',
	summeries,delimiter=',',fmt='%g')