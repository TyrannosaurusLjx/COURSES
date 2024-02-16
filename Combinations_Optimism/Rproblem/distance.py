import numpy as np

# F距离
def F(x, y):
    return np.sum(np.abs(x - y))

# rho距离
def R(x, y):
    return np.linalg.norm(x,y)

# 向量到集合集合的距离
def Dis(v, S, func):
    sum = 0
    for u in S:
        sum += func(u,v)
    return sum



