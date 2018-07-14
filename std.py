from __future__ import unicode_literals
import numpy as np

path = r'C:\Users\xulingfeng\Desktop\python学习\数学分析\DS\data\aapl.csv'

closing_prices = np.loadtxt(path,delimiter=',',
	usecols = (6),
	unpack = True)

# 算术平均值
mean = closing_prices.mean()

# 离差
devs = closing_prices - mean

# 离差方
sqrs = devs ** 2

# 方差
svar = sqrs.mean() 		# 总体方差
pvar = sqrs.sum() / (sqrs.size - 1) 	# 样本方差

# 标准差
sstd = np.sqrt(svar)	# 总体标准差
print(sstd)
pstd = np.sqrt(pvar)	# 样本标准差
print(pstd)

# 用内置函数
sstd = np.std(closing_prices)
print(sstd)
pstd = np.std(closing_prices, ddof=1)
print(pstd)