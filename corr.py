from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md

path1 = r'C:\Users\xulingfeng\Desktop\python学习\数学分析\DS\data\vale.csv'
path2 = r'C:\Users\xulingfeng\Desktop\python学习\数学分析\DS\data\bhp.csv'

def dmy2ymd(dmy):
	dmy = str(dmy, encoding='utf-8')	# utf-8转成UCS-4类型
	date = dt.datetime.strptime(dmy,'%d-%m-%Y').date()
	ymd = date.strftime('%Y-%m-%d')

dates,bhp_closing_prices = np.loadtxt(path2,delimiter=',',
	usecols = (1,6),
	unpack = True,
	dtype=np.dtype('M8[D],f8'),
	converters={1:dmy2ymd})


dates,vale_closing_prices = np.loadtxt(path1,delimiter=',',
	usecols = (1,6),
	unpack = True,
	dtype=np.dtype('M8[D],f8'),
	converters={1:dmy2ymd})

bhp_returns = np.diff(bhp_closing_prices)		# 计算相邻元素之前的差
bhp_returns = bhp_returns / bhp_closing_prices[:-1]		# 排除最后一天的数
# print(bhp_returns)

vale_returns = np.diff(vale_closing_prices)		# 计算相邻元素之前的差
vale_returns = vale_returns / vale_closing_prices[:-1]		# 排除最后一天的数
# print(vale_returns)

ave_a = np.mean(bhp_returns)
dev_a = bhp_returns - ave_a
var_a = np.mean(dev_a * dev_a)
std_a = np.sqrt(var_a)

ave_b = np.mean(vale_returns)
dev_b = vale_returns - ave_b
var_b = np.mean(dev_b * dev_b)
std_b = np.sqrt(var_b)

cov_aa = var_a
cov_ab = np.mean(dev_a * dev_b)
cov_ba = np.mean(dev_b * dev_a)
cov_bb = var_b

covs = np.array([[cov_aa, cov_ab],[cov_ba, cov_bb]])
stds = np.array([[std_a * std_a, std_a * std_b],[std_b * std_a, std_b * std_b]])
corr = covs / stds
print(corr)

corr = np.corrcoef(bhp_returns, vale_returns)
print(corr)

mp.figure('Correlation Of Returns', facecolor='lightgray')
mp.title('Correlation Of Returns', fontsize=20)
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

mp.plot(dates[:-1], bhp_returns, 'o-', c='orangered', label='BHP')
mp.plot(dates[:-1], vale_returns, 'o-', c='dodgerblue', label='VALE')

mp.legend()
mp.gcf().autofmt_xdate()
mp.show()