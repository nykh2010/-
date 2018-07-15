import numpy as np
import matplotlib.pyplot as mp

# 生成随机序列
samples = np.random.normal(size=10000)


# print(outcomes)
mp.figure('Normal Distribution', facecolor='lightgray')
mp.title('Normal Distribution', fontsize=20)
mp.xlabel('Samples', fontsize=14)
mp.ylabel('Occurrence', fontsize=10)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
bins = mp.hist(samples, 100, normed=True, edgecolor='steelblue', facecolor='deepskyblue',label='normal')[1] # 生成条形图
probs = np.exp(-bins ** 2 / 2) / np.sqrt(2 * np.pi)
mp.plot(bins, probs, 'o-', c='orangered', label='Probability')
mp.legend()
mp.show()