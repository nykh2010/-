from __future__ import unicode_literals
import numpy as np
import datetime as dt
import matplotlib.pyplot as mp
import matplotlib.dates as md

def dmy2ymd(dmy):
	dmy = str(dmy, encoding='utf-8')
	date = dt.datetime.strptime(dmy,'%d-%m-%Y').date()
	ymd = date.strftime('%Y-%m-%d')
	return ymd

path = r'C:\Users\xulingfeng\Desktop\python学习\数学分析\DS\data\aapl.csv'

dates,closing_prices = np.loadtxt(path,delimiter=',',
	usecols = (1,6),
	unpack = True,
	dtype = np.dtype('M8[D], f8'),
	converters = {1:dmy2ymd})

sma5a = np.zeros(closing_prices.size - 4)
for i in range(sma5a.size):
	sma5a[i] = closing_prices[i:i+5].mean()

sma5b = np.convolve(closing_prices, np.ones(5)/5, 'valid')
# print(sma5a)
# print(sma5b)
sma10 = np.convolve(closing_prices, np.ones(10)/10, 'valid')

weights = np.exp(np.linspace(-1,0,5))
weights /= weights.sum()
ema5 = np.convolve(closing_prices, weights[::-1], 'valid')

mp.figure('Moving Average', facecolor='lightgray')
mp.title('Moving Average', fontsize=20)
mp.xlabel('Date', fontsize = 14)
mp.ylabel('Price', fontsize = 14)

ax = mp.gca()
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_minor_locator(md.DayLocator())
ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))		# %b为月份的缩写

mp.tick_params(labelsize=10)
mp.grid(linestyle=':')

dates = dates.astype(md.datetime.datetime)
mp.plot(dates, closing_prices, c='dodgerblue', label='closing_prices')
mp.plot(dates[4:], sma5a, c='orangered', label='sma5a')
mp.plot(dates[4:], sma5b, c='orangered', alpha = 0.25, linewidth = 6, label='sma5b', zorder = 1)
mp.plot(dates[9:], sma10, c='limegreen', label='sma10')
mp.plot(dates[4:], ema5, c='red', label='ema5')

mp.legend()
mp.gcf().autofmt_xdate()
mp.show()