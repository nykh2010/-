# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md
dates, closing_prices = np.loadtxt(
    '../../data/goog.csv', delimiter=',',
    usecols=(0, 4), unpack=True,
    dtype=np.dtype('M8[D], f8'), skiprows=1)
mp.figure(num='Google', facecolor='lightgray')
mp.title('Google', fontsize=20)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)
ax = mp.gca()
ax.xaxis.set_major_locator(md.MonthLocator())
ax.xaxis.set_major_formatter(
    md.DateFormatter('%d %b %Y'))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
dates = dates.astype(md.datetime.datetime)
bottom = closing_prices.min() - 10
threshold = closing_prices[158]
mp.fill_between(dates, bottom, closing_prices,
                where=closing_prices <= threshold,
                facecolor='limegreen', alpha=0.5,
                label='Below Threshold')
mp.fill_between(dates, bottom, closing_prices,
                where=closing_prices >= threshold,
                facecolor='orangered', alpha=0.5,
                label='Above Threshold')
mp.plot(dates, closing_prices, c='red',
        label='Closing Price')
mp.axhline(y=threshold, linestyle='--',
           color='dodgerblue', linewidth=1,
           label='Threshold')
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
