import numpy as np
import sklearn.preprocessing as sp      # 机器学习的预处理包

raw_samples = np.array([
    [3, -1.5, 2, -5.4],
    [0, 4, -0.3, 2.1],
    [1, 3.3, -1.9, -4.3]
])
mms_samples = raw_samples.copy()

# 手动生成
for col in mms_samples.T:
    col_min = col.min()
    col_max = col.max()
    # kx + b = y
    # k col_min + b = 0
    # k col_max + b = 1
    # / col_min  1 \  X  / k \ = / 0 \
    # \ col_max  1 /     \ b /   \ 1 /
    a = np.array([
        [col_min, 1],
        [col_max, 1]
    ])
    b = np.array([0,1])
    x = np.linalg.solve(a,b)
    col *= x[0]
    col += x[1]
print(mms_samples)

print('-' * 40)

mms = sp.MinMaxScaler(feature_range=(0,1))      # 构建最小值最大值缩放器
mms_samples = mms.fit_transform(raw_samples)
print(mms_samples)