from __future__ import unicode_literals
import warnings
import datetime as dt
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md

warnings.filterwarnings('ignore', category=np.RankWarning)

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

print(bhp_closing_prices)
print(vale_closing_prices)

diff_closing_prices = bhp_closing_prices - vale_closing_prices
days = dates.astype(int)

p = np.polyfit(days, diff_closing_prices, 5)
poly_closing_prices = np.polyval(p, days)

# q = np.polyder(p)
# roots = np.roots(q)
# reals = roots[np.isreal(roots)].real
# peeks = [[days[0], np.polyval(p, days[0])]]
# for real in reals:
#     if days[0] < real and real < days[-1]:
#         peeks.append([real, np.polyval(p, real)])
# peeks.append(days[-1], np.polyval(p, days[-1]))
# peeks.sort()
# peeks = np.array(peeks)

mp.figure('Polynomial Fitting', facecolor='lightgray')
mp.title('Polynomial Fitting', fontsize=20)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Difference Prices', fontsize=14)

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

mp.plot(dates, poly_closing_prices, c='dodgerblue', label='Polynomial Fitting', zorder='2')
mp.scatter(dates, diff_closing_prices, alpha=0.5, s=60, c='limegreen', label='VALE', zorder='2')
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()