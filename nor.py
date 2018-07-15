import numpy as np
import sklearn.preprocessing as sp      # 机器学习的预处理包

raw_samples = np.array([
    [3, -1.5, 2, -5.4],
    [0, 4, -0.3, 2.1],
    [1, 3.3, -1.9, -4.3]
])
nor_samples = raw_samples.copy()

for row in nor_samples:
    row_abssum = abs(row).sum()
    row /= row_abssum
print(nor_samples)
print(abs(nor_samples).sum(axis=1))
nor_samples = sp.normalize(raw_samples, norm='l1')      # l1:绝对值和
                                                        # l2:平方和
print(nor_samples)                                                    