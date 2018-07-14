# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import warnings
import datetime as dt
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md
warnings.filterwarnings('ignore',
                        category=np.RankWarning)


def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    date = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    ymd = date.strftime('%Y-%m-%d')
    return ymd


dates, bhp_closing_prices = np.loadtxt(
    '../../data/bhp.csv', delimiter=',',
    usecols=(1, 6), unpack=True,
    dtype=np.dtype('M8[D], f8'),
    converters={1: dmy2ymd})
_, vale_closing_prices = np.loadtxt(
    '../../data/vale.csv', delimiter=',',
    usecols=(1, 6), unpack=True,
    dtype=np.dtype('M8[D], f8'),
    converters={1: dmy2ymd})
diff_closing_prices = bhp_closing_prices - \
    vale_closing_prices
days = dates.astype(int)
p = np.polyfit(days, diff_closing_prices, 5)
poly_closing_prices = np.polyval(p, days)
q = np.polyder(p)
roots = np.roots(q)
reals = roots[np.isreal(roots)].real
peeks = []
for real in reals:
    if days[0] <= real and real <= days[-1]:
        peeks.append([real, np.polyval(p, real)])
peeks = np.array(peeks)
mp.figure(num='Polynomial Fitting',
          facecolor='lightgray')
mp.title('Polynomial Fitting', fontsize=20)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Difference Price', fontsize=14)
ax = mp.gca()
ax.xaxis.set_major_locator(
    md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_minor_locator(md.DayLocator())
ax.xaxis.set_major_formatter(
    md.DateFormatter('%d %b %Y'))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
dates = dates.astype(md.datetime.datetime)
mp.plot(dates, poly_closing_prices, 'o-', c='dodgerblue',
        linewidth=3, label='Polynomial Fitting')
mp.scatter(dates, diff_closing_prices, c='limegreen',
           alpha=0.5, s=80, label='Difference Price')
dates, prices = np.hsplit(peeks, 2)
dates = dates.astype(
    int).astype('M8[D]').astype(md.datetime.datetime)
mp.scatter(dates, prices, marker='x', c='red', s=100,
           label='Peek', zorder=4)
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
