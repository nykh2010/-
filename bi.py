import numpy as np
import matplotlib.pyplot as mp

# 生成随机序列
outcomes = np.random.binomial(9, 0.5, 10000)
print(outcomes)

chips = [1000]

for outcome in outcomes:
    if outcome >= 5:
        chips.append(chips[-1] + 1)
    else:
        chips.append(chips[-1] - 1)
chips = np.array(chips)

mp.figure('Binomial Distribution', facecolor='lightgray')
mp.title('Binomial Distribution', fontsize=20)
mp.xlabel('Round', fontsize=14)
mp.ylabel('Chip', fontsize=10)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
o,h,l,c = 0, chips.argmax(),chips.argmin(),chips.size-1
if chips[o] < chips[c]:
    color = 'orangered'
elif chips[c] < chips[o]:
    color = 'limegreen'
else:
    color = 'dodgerblue'
mp.plot(chips, c=color, label='Chip')
mp.axhline(y=chips[o], linestyle='--', color='deepskyblue', linewidth=1)
mp.axhline(y=chips[h], linestyle='--', color='black', linewidth=1)
mp.axhline(y=chips[l], linestyle='--', color='seagreen', linewidth=1)
mp.axhline(y=chips[c], linestyle='--', color='orange', linewidth=1)

mp.legend()
mp.show()