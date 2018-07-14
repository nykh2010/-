from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md

path = r'C:\Users\xulingfeng\Desktop\python学习\数学分析\DS\data\aapl.csv'

def dmy2ymd(dmy):
	dmy = str(dmy, encoding='utf-8')	# utf-8转成UCS-4类型
	date = dt.datetime.strptime(dmy,'%d-%m-%Y').date()
	ymd = date.strftime('%Y-%m-%d')

dates,\
opening_prices,\
highest_prices,\
lowest_prices,\
closing_prices = np.loadtxt(path,delimiter=',',
	usecols = (1,3,4,5,6),
	unpack = True,
	dtype=np.dtype('M8[D],f8,f8,f8,f8'),
	converters={1:dmy2ymd})

mp.figure('K-Day', facecolor='lightgray')
mp.title('K-Day', fontsize=20)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)

ax = mp.gca()
ax.xaxis.set_major_locator(
	# 横轴主刻度定位器以星期为周期，且刻度画在星期一上
	md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_minor_locator(
	md.DayLocator())
ax.xaxis.set_major_formatter(md.DateFormatter('%d-%b-%Y'))	# 主刻度标签的日期格式化器

mp.tick_params(labelsize=10)
mp.grid(linestyle=':')

dates = dates.astype(md.datetime.datetime)  # 把numpy里的日期格式转成matplotlib里的datetime格式

rise = closing_prices - opening_prices >= 0.01
fall = opening_prices - closing_prices >= 0.01

fc = np.zeros(dates.size, dtype='3f4')
ec = np.zeros(dates.size, dtype='3f4')
fc[rise], fc[fall] = (1,1,1), (0,0.5,0)		# RGG的颜色格式
ec[rise], ec[fall] = (1,0,0), (0,0.5,0)

mp.bar(dates,highest_prices-lowest_prices,0,lowest_prices,color=fc,edgecolor=ec)		# 先画线，再画方块，可以达到空心效果
mp.bar(dates,closing_prices-opening_prices,0.8,opening_prices,color=fc,edgecolor=ec)

mp.gcf().autofmt_xdate()
mp.show()