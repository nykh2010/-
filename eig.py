import numpy as np

A = np.mat('3 -2; 1 0')
eigvals, eigvecs = np.linalg.eig(A)
print(eigvals)
print(eigvecs)
# 验算
print(A * eigvecs[:,0])
print(eigvals[0] * eigvecs[:,0])
print(A * eigvecs[:,0])
print(eigvals[0] * eigvecs[:,0])
