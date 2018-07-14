# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md
dates, volumes = np.loadtxt(
    '../../data/goog.csv', delimiter=',',
    usecols=(0, 6), unpack=True,
    dtype=np.dtype('M8[D], f8'), skiprows=1)
mp.figure(num='Volume', facecolor='lightgray')
ax = mp.subplot(211)
mp.title('Ordinary', fontsize=20)
mp.ylabel('Volume', fontsize=14)
ax.xaxis.set_major_locator(md.MonthLocator())
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
dates = dates.astype(md.datetime.datetime)
mp.plot(dates, volumes, c='dodgerblue',
        label='Volume')
mp.legend()
ax = mp.subplot(212)
mp.title('Logarithmic', fontsize=20)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Volume', fontsize=14)
ax.xaxis.set_major_locator(md.MonthLocator())
ax.xaxis.set_major_formatter(
    md.DateFormatter('%d %b %Y'))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.semilogy(dates, volumes, c='orangered',
            label='Volume')
mp.legend()
mp.gcf().autofmt_xdate()
mp.tight_layout()
mp.show()
