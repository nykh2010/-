# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
dates, opening_prices, highest_prices, \
    lowest_prices, closing_prices = np.loadtxt(
    '../../data/aapl.csv', delimiter=',',
    usecols=(1,3,4,5,6), unpack=True,
    dtype=np.dtype('M8[D],f8,f8,f8,f8'),
    converters={1: dmy2ymd})
