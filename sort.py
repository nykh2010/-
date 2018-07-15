import numpy as np

names = np.array(['张飞','赵云','关羽','黄忠','马超'])
scores = np.array([80, 90, 70, 80, 60])
ages = np.array([19, 22, 28, 25, 20])

result = names[np.lexsort((ages, scores))][::-1]         # 排成绩，参考年龄，返回的是排序下标
print(result)

# 复数序列排序，以实部作为主序列，参考虚部
a = np.array([0+8j, 5+3j, 0+1j, 1+8j, 2+7j, 1+1j])
b = np.sort_complex(a)
print(b)

c = np.array([1,9,3,np.nan,7,5])        # nan作为无效值，numpy默认为无穷大和无穷小，全部最大和最小都返回nan
print(c.max(), np.max(c))
print(c.min(), np.min(c))
print(c[np.argmax(c)])
print(c[np.argmin(c)])

print(np.nanmax(c))             # 忽略nan
print(np.nanmin(c))
print(c[np.nanargmax(c)])
print(c[np.nanargmin(c)])

d = np.array([1,2,4,5,6,8,9])
e = np.array([7,3])
f = np.searchsorted(d,e)        # 将 e 插入 d 中，首先保证d为有序
print(f)            # 返回的是插入的下标号
g = np.insert(d, f, e)          # 将 e 按 f 所标示的位置插入d中，返回插入结果
print(g)