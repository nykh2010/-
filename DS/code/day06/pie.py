# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import matplotlib.pyplot as mp
values = [26, 17, 21, 29, 11]
spaces = [0.05, 0.01, 0.01, 0.01, 0.01]
labels = ['Python', 'JavaScript', 'C++', 'C', 'PHP']
colors = ['dodgerblue', 'orangered', 'limegreen',
          'violet', 'gold']
mp.figure(num='Pie', facecolor='lightgray')
mp.title('Pie', fontsize=20)
mp.pie(values, spaces, labels, colors, '%d%%',
       shadow=True, startangle=90)
mp.axis('equal')
mp.show()
