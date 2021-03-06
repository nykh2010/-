import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array([
    [1,3,9],
    [7,5,2],
    [1,8,4],
    [7,3,6]
])
print(raw_samples)

code_tables = []

for col in raw_samples.T:
    code_table = {}
    for val in col:
        code_table[val] = None
    code_tables.append(code_table)

for code_table in code_tables:
    size = len(code_table)
    for one, key in enumerate(sorted(code_table.keys())):
        code_table[key] = np.zeros(shape=size,  dtype=int)
        code_table[key][one] = 1

ohe_samples = []
for raw_sample in raw_samples:
    ohe_sample = np.array([], dtype=int)
    for i,key in enumerate(raw_sample):
        ohe_sample = np.hstack((ohe_sample, code_tables[i][key]))
    ohe_samples.append(ohe_sample)
ohe_samples = np.array(ohe_samples)
print(ohe_samples)

ohe = sp.OneHotEncoder(sparse=False, dtype=int)        # 稀疏矩阵，只记1的行列号
ohe_samples = ohe.fit_transform(raw_samples)
print(ohe_samples)