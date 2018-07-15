import numpy as np
import matplotlib.pyplot as mp

# 生成随机序列
outcomes = np.random.hypergeometric(25, 1, 3, 100)
# print(outcomes)

scores = [100]

for outcome in outcomes:
    if outcome == 3:
        scores.append(scores[-1] + 1)
    else:
        scores.append(scores[-1] - 6)
scores = np.array(scores)

mp.figure('Hypergeometric Distribution', facecolor='lightgray')
mp.title('Hypergeometric Distribution', fontsize=20)
mp.xlabel('Round', fontsize=14)
mp.ylabel('Scores', fontsize=10)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
o,h,l,c = 0, scores.argmax(),scores.argmin(),scores.size-1
if scores[o] < scores[c]:
    color = 'orangered'
elif scores[c] < scores[o]:
    color = 'limegreen'
else:
    color = 'dodgerblue'
mp.plot(scores, c=color, label='Chip')
mp.axhline(y=scores[o], linestyle='--', color='deepskyblue', linewidth=1)
mp.axhline(y=scores[h], linestyle='--', color='black', linewidth=1)
mp.axhline(y=scores[l], linestyle='--', color='seagreen', linewidth=1)
mp.axhline(y=scores[c], linestyle='--', color='orange', linewidth=1)

mp.legend()
mp.show()