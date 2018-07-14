# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime as dt
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md


def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    date = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    ymd = date.strftime('%Y-%m-%d')
    return ymd


dates, closing_prices = np.loadtxt(
    '../../data/aapl.csv', delimiter=',',
    usecols=(1, 6), unpack=True,
    dtype=np.dtype('M8[D], f8'),
    converters={1: dmy2ymd})
sma5a = np.zeros(closing_prices.size - 4)
for i in range(sma5a.size):
    sma5a[i] = closing_prices[i:i+5].mean()
sma5b = np.convolve(closing_prices,
                    np.ones(5) / 5, 'valid')
weights = np.exp(np.linspace(-1, 0, 5))
weights /= weights.sum()
ema5 = np.convolve(closing_prices, weights[::-1],
                   'valid')
mp.figure('Simple Moving Average',
          facecolor='lightgray')
mp.title('Simple Moving Average', fontsize=20)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)
ax = mp.gca()
ax.xaxis.set_major_locator(
    md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_minor_locator(md.DayLocator())
ax.xaxis.set_major_formatter(
    md.DateFormatter('%d %b %Y'))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
dates = dates.astype(md.datetime.datetime)
mp.plot(dates, closing_prices, 'o-', c='gray',
        label='Closing Price')
mp.plot(dates[4:], sma5a, c='orangered',
        linewidth=3, label='SMA-5A')
mp.plot(dates[4:], sma5b, c='dodgerblue',
        linewidth=6, alpha=0.5, label='SMA-5B')
mp.plot(dates[4:], ema5, c='limegreen',
        linewidth=6, alpha=0.5, label='EMA-5')
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()







