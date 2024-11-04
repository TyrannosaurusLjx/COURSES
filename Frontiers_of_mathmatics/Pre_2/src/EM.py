import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 人数比例
boys_nums = 300
girls_nums = 700
total_nums = boys_nums + girls_nums

# 参数预设定
b_mu = 170
b_sigma = 9
g_mu = 160
g_sigma = 2

# 生成数据
boys = np.random.normal(b_mu, b_sigma, boys_nums)
girls = np.random.normal(g_mu, g_sigma, girls_nums)
mixs = np.concatenate([boys, girls])
indexs = np.zeros(total_nums, dtype=int)
indexs[:boys_nums] = 1
shuffle_indexs = np.random.permutation(total_nums)
mixs = mixs[shuffle_indexs]
indexs = indexs[shuffle_indexs]

# 初始化Z，Theta
Z = np.zeros(total_nums, dtype=int)
b_mu_pred = 180  # 选择更接近真实值的初始均值
g_mu_pred = 160
b_sigma_pred = 3  # 合理的初始值
g_sigma_pred = 2

# EM算法参数
T = 3000  # 初期减少迭代次数
M = 100
epsilon = 0.00001

def loss(old, new, epsilon):
    return np.abs(new - old) < epsilon

# 存储迭代情况
data = np.zeros((T, 5))

for t in range(T):
    # E-step: 计算每个样本属于男孩和女孩的概率密度
    boys_density = norm.pdf(mixs, b_mu_pred, b_sigma_pred)
    girls_density = norm.pdf(mixs, g_mu_pred, g_sigma_pred)

    # 更新Z，使用最大概率判断
    Z = np.where(boys_density > girls_density, 1, 0)

    # M-step: 更新参数
    b_mu_pred = np.sum(Z * mixs) / np.sum(Z) if np.sum(Z) > 0 else 0
    g_mu_pred = np.sum((1 - Z) * mixs) / np.sum(1 - Z) if np.sum(1 - Z) > 0 else 0
    b_sigma_pred = np.sqrt(np.sum(Z * (mixs - b_mu_pred) ** 2) / np.sum(Z)) if np.sum(Z) > 0 else 0
    g_sigma_pred = np.sqrt(np.sum((1 - Z) * (mixs - g_mu_pred) ** 2) / np.sum(1 - Z)) if np.sum(1 - Z) > 0 else 0
    data[t] = [b_mu_pred, g_mu_pred, b_sigma_pred, g_sigma_pred, np.sum(Z == indexs)/total_nums]
    b_mu_gap = np.abs(data[t, 0] - data[t-1, 0]) if t > 0 else M
    g_mu_gap = np.abs(data[t, 1] - data[t-1, 1]) if t > 0 else M
    b_sigma_gap = np.abs(data[t, 2] - data[t-1, 2]) if t > 0 else M
    g_sigma_gap = np.abs(data[t, 3] - data[t-1, 3]) if t > 0 else M
    if t > 15 and loss(b_mu_gap, 0, epsilon) and loss(g_mu_gap, 0, epsilon) and loss(b_sigma_gap, 0, epsilon) and loss(g_sigma_gap, 0, epsilon):
        data = data[:t]
        break
    else:
        print('第{}次迭代'.format(t))
        print(b_mu_gap, g_mu_gap, b_sigma_gap, g_sigma_gap)

# 输出最终的参数和准确率
print('b_mu_pred:', b_mu_pred)
print('g_mu_pred:', g_mu_pred)
print('b_sigma_pred:', b_sigma_pred)
print('g_sigma_pred:', g_sigma_pred)
print("Z准确率: {}".format(np.sum(Z == indexs) / total_nums))

# 绘制参数变化图
data_mu = data[:, :2]
data_sigma = data[:, 2:-1]
data_Z = data[:,-1]
plt.figure(figsize=(12, 6))
plt.subplot(131)
plt.plot(data_mu)
plt.title('mu')
plt.legend(['b_mu', 'g_mu'])
plt.subplot(132)
plt.plot(data_sigma)
plt.title('sigma')
plt.legend(['b_sigma', 'g_sigma'])
plt.subplot(133)
plt.plot(data_Z)
plt.title('The accuracy of parameter Z')
plt.legend(['Z'])
plt.show()
