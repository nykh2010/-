# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
outcomes = np.random.binomial(9, 0.5, 10000)
chips = [1000]
for outcome in outcomes:
    if outcome >= 5:
        chips.append(chips[-1] + 1)
    else:
        chips.append(chips[-1] - 1)
chips = np.array(chips)
mp.figure(num='Binomial Distribution',
          facecolor='lightgray')
mp.title('Binomial Distribution', fontsize=20)
mp.xlabel('Round', fontsize=14)
mp.ylabel('Chip', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
o, h, l, c = 0, chips.argmax(), chips.argmin(), \
    chips.size - 1
if chips[o] < chips[c]:
    color = 'orangered'
elif chips[c] < chips[o]:
    color = 'limegreen'
else:
    color = 'dodgerblue'
mp.plot(chips, c=color, label='Chip')
mp.axhline(y=chips[o], linestyle='--', linewidth=1)
mp.axhline(y=chips[h], linestyle='--', linewidth=1)
mp.axhline(y=chips[l], linestyle='--', linewidth=1)
mp.axhline(y=chips[c], linestyle='--', linewidth=1)
mp.legend()
mp.show()
