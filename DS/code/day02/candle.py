# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime as dt
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md


# 将原始数据文件中"日-月-年"格式的日期字符串转换为
# Numpy可以处理的"年-月-日"格式
def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    date = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    ymd = date.strftime('%Y-%m-%d')
    return ymd


# 从原始数据文件中读取交易日期和每个交易日的开盘价、
# 最高价、最低价和收盘价(ohlc)
dates, opening_prices, highest_prices, \
    lowest_prices, closing_prices = np.loadtxt(
        '../../data/aapl.csv', delimiter=',',
        usecols=(1, 3, 4, 5, 6), unpack=True,
        dtype=np.dtype('M8[D],f8,f8,f8,f8'),
        converters={1: dmy2ymd})


# 创建图形窗口
mp.figure('Candlestick', facecolor='lightgray')
# 设置标题
mp.title('Candlestick', fontsize=20)
# 设置水平和垂直坐标轴上标签的文本和字号
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)
# 获取坐标轴对象
ax = mp.gca()
# 设置水平坐标轴主、次刻度定位器
ax.xaxis.set_major_locator(
    md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_minor_locator(md.DayLocator())
# 设置水平坐标轴主刻度标签格式化器
ax.xaxis.set_major_formatter(
    md.DateFormatter('%d %b %Y'))
# 设置坐标轴刻度标签字号
mp.tick_params(labelsize=10)
# 设置网格线线型
mp.grid(linestyle=':')
# 将日期由Numpy类型转换为matplotlib类型
dates = dates.astype(md.datetime.datetime)
# 获取上涨和下跌的掩码数组
rise = closing_prices - opening_prices >= 0.01
fall = opening_prices - closing_prices >= 0.01
# 设置每个交易日K线的填充色和边缘色
# 颜色用一个元组表示(红, 绿，蓝)，其中每个元素分别
# 表达一个颜色通道的亮度等级([0, 1])
fc = np.zeros(dates.size, dtype='3f4')
ec = np.zeros(dates.size, dtype='3f4')
fc[rise], fc[fall] = (1, 1, 1), (0, 0.5, 0)
ec[rise], ec[fall] = (1, 0, 0), (0, 0.5, 0)
# 绘制影线
mp.bar(dates, highest_prices - lowest_prices, 0,
       lowest_prices, color=fc, edgecolor=ec)
# 绘制实体
mp.bar(dates, closing_prices - opening_prices, 0.8,
       opening_prices, color=fc, edgecolor=ec)
# 调整水平坐标轴上的日期标签格式，避免重叠
mp.gcf().autofmt_xdate()
# 显示绘图结果，提供交互
mp.show()
