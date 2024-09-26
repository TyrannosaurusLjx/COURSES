## SGA 实现
import numpy as np
import matplotlib.pyplot as plt
import math
M = 6
pc = 0.6
pm = 0.01 
T = 3
l = 10 # 染色体长度


def target(x, y):
    if x == 0 and y == 0:
        return 0
    else:
        return 1 - np.sqrt(8 - x**2 - y**2)
# 编码函数
def encode(x, y):
    chromesome = ""
    length = int(l/2)
    chromesome += bin(int(x))[2:].zfill(length)
    chromesome += bin(int(y))[2:].zfill(length)
    return chromesome

# 解码函数
def decode(chromesome):
    length = int(l/2)
    x = int(chromesome[:length], 2)
    y = int(chromesome[length:], 2)
    return x, y

# 适应度函数
def fit(chromesome):
    return target(*decode(chromesome))


polulation = [encode(np.random.uniform(0,2), np.random.uniform(0,2)) for _ in range(M)]

fitness = [fit(chromesome) for chromesome in polulation]

for t in range(T):
    new_polution = []
    fit_sum = np.sum(fitness)

    for i in range(int(M/2)):
        new_polution.append( np.random.choice(polulation, p = np.array(fitness)/fit_sum))

    for i in range(i, M, 2):
        cross_1, cross_2 = polulation[i], polulation[i-1]
        if np.random.uniform(0,1) < pc:
            cross_point = np.random.randint(0, l)
            new_polution.append(cross_1[:cross_point] + cross_2[cross_point:])
            new_polution.append(cross_2[:cross_point] + cross_1[cross_point:])
        else:
            new_polution.append(cross_1)
            new_polution.append(cross_2)

    for j in range(M):
        if np.random.uniform(0,1) < pm:
            mutation_point = np.random.randint(0, l)
            mutation_value = "1" if new_polution[j][mutation_point] == "0" else "0"
            # new_polution[j][mutation_point] = mutation_value
# 将字符串转换为列表
            polution_list = list(new_polution[j])

# 修改 mutation_point 位置的元素
            polution_list[mutation_point] = mutation_value

# 将列表重新转为字符串并赋值回 new_polution[j]
            new_polution[j] = ''.join(polution_list)



# 输出最优解
fitness = [fit(chromesome) for chromesome in polulation]

print("最优解为：", decode(polulation[np.argmax(fitness)]))

        


















