# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
closing_prices = np.loadtxt(
    '../../data/aapl.csv', delimiter=',',
    usecols=(6), unpack=True)
# 计算相邻元素之差
diff_closing_prices = np.diff(closing_prices)
simple_returns = diff_closing_prices / \
    closing_prices[:-1]
m_simple_returns = simple_returns.mean()
print(m_simple_returns)
d_simple_returns = simple_returns - m_simple_returns
q_simple_returns = d_simple_returns ** 2
v_simple_returns = q_simple_returns.mean()
print(v_simple_returns)
v_simple_returns = np.var(simple_returns)
print(v_simple_returns)
s_simple_returns = np.sqrt(v_simple_returns)
print(s_simple_returns)
s_simple_returns = np.std(simple_returns)
print(s_simple_returns)