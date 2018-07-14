# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
highest_prices, lowest_prices = np.loadtxt(
    '../../data/aapl.csv', delimiter=',',
    usecols=(4, 5), unpack=True)
# 最高价的最大和最小值
max_highest_price, min_highest_price = \
    highest_prices[0], highest_prices[0]
# 最低价的最大和最小值
max_lowest_price, min_lowest_price = \
    lowest_prices[0], lowest_prices[0]
for highest_price, lowest_price in zip(
        highest_prices, lowest_prices):
    # 如果该最高价高于最高的最高价
    if highest_price > max_highest_price:
        # 更新最高的最高价为该最高价
        max_highest_price = highest_price
    # 如果该最高价低于最低的最高价
    if highest_price < min_highest_price:
        # 更新最低的最高价为该最高价
        min_highest_price = highest_price
    # 如果该最低价高于最高的最低价
    if lowest_price > max_lowest_price:
        # 更新最高的最低价为该最低价
        max_lowest_price = lowest_price
    # 如果该最低价低于最低的最低价
    if lowest_price < min_lowest_price:
        # 更新最低的最低价为该最低价
        min_lowest_price = lowest_price
high_spread = max_highest_price - min_highest_price
low_spread = max_lowest_price - min_lowest_price
print(high_spread, low_spread)
# 最高价数组的极差
high_spread = np.ptp(highest_prices)
# 最低价数组的极差
low_spread = np.ptp(lowest_prices)
print(high_spread, low_spread)
