import numpy as np

A = np.mat('1 2 3; 8 9 4; 7 6 5')
print(A)

B = np.linalg.inv(A)       # 仅限于方阵
print(B)

C = A * B
print(C)
print(A.I)