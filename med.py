from __future__ import unicode_literals
import numpy as np

path = r'C:\Users\xulingfeng\Desktop\python学习\数学分析\DS\data\aapl.csv'

closing_prices = np.loadtxt(path,delimiter=',',
	usecols = (6),
	unpack = True)

# 应用 numpy 的快速排序算法对给定数组中的元素做升序排列
sorted_prices = np.msort(closing_prices)
print(sorted_prices)

a = sorted_prices[::-1]		# 切片方式做降序排列

# 公式计算
l = sorted_prices.size
median = (sorted_prices[int((l-1)/2)] + sorted_prices[int(l/2)]) / 2
print(median)

# 函数计算
median = np.median(closing_prices)
print(median)
