import numpy as np

M = np.mat('4 11 14; 8 7 -2')
print(M)

U, S, V = np.linalg.svd(M, full_matrices=False)     # 不能为满置
print(U)
print(np.diag(S))       # S返回的是主对角线元素，使用diag生成矩阵
print(V)
print(U * U.T)
print(V * V.T)
print(U*S*V)