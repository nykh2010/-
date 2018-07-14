from __future__ import unicode_literals
import numpy as np
import datetime as dt

path = r'C:\Users\xulingfeng\Desktop\python学习\数学分析\DS\data\aapl.csv'

def dmy2wday(dmy):
	dmy = str(dmy, encoding='utf-8')
	date = dt.datetime.strptime(dmy,'%d-%m-%Y').date()
	wday = date.weekday()	# 用 0 到 6 表示周一到周日
	return wday

wdays,closing_prices = np.loadtxt(path,delimiter=',',
	usecols = (1,6),
	unpack = True,
	converters = {1:dmy2wday})

ave_closing_prices = np.zeros(5)
for wday in range(ave_closing_prices.size):
	# 第一种方法：
	# ave_closing_prices[wday] = \
	# closing_prices[wdays==wday].mean()
	# 第二种方法：
	# ave_closing_prices[wday] = \
	# closing_prices[np.where(wdays==wday)].mean()
	# 第三种方法：
	ave_closing_prices[wday] = np.take(closing_prices, np.where(wdays==wday)).mean()

print(np.round(ave_closing_prices,2))		# 保留两位小数