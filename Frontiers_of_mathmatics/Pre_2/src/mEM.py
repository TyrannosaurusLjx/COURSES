import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 返回下标序列
def getIndex(K, M):
    return np.random.choice(np.arange(K), size=M)

# 获得混合高斯分布
def getY(Z, mu, sigma, K, M):
    if np.size(mu) != K or np.size(sigma) != K:
        raise SystemError
    else:
        Y = np.zeros(M)
        for i in range(K):
            Y[ Z == i ] = np.random.normal(mu[i], sigma[i], size=np.sum(Z==i))
        return Y

# 检查是否收敛
def check(old, new, epsilon):
    return np.all(np.abs(old - new) < epsilon)

# EM算法
def gaussEM(K, M, T, Y, epsilon, Theta0):
    loop = 5
    data = np.zeros((T, K, 2))
    # 初始化参数
    mu, sigma = Theta0
    Z = np.zeros(M)
    t = 0
    for t in range(T):
        # E-step: 计算每个点属于每个高斯分布的概率
        densities = np.zeros((M, K))
        for k in range(K):
            densities[:, k] = norm.pdf(Y, loc=mu[k], scale=sigma[k])
        
        # 根据最大概率分配每个数据点到对应的簇
        Z = np.argmax(densities, axis=1)

        # M-step: 更新参数
        new_mu = np.zeros(K)
        new_sigma = np.zeros(K)

        for k in range(K):
            # 计算每个簇的均值和标准差
            cluster_data = Y[Z == k]
            if len(cluster_data) > 0:
                new_mu[k] = np.mean(cluster_data)
                new_sigma[k] = np.std(cluster_data, ddof=0) if len(cluster_data) > 1 else 0
            else:
                # 空的话就不变, 弄成0差别太大
                new_mu[k] = mu[k]
                new_sigma[k] = sigma[k]
        
        # 检查是否收敛
        if check(mu, new_mu, epsilon) and check(sigma, new_sigma, epsilon):
            if loop == 0:
                print(f"Converged at iteration {t}")
                break
            else:
                loop -= 1
        
        # 更新参数
        mu, sigma = new_mu, new_sigma
        data[t] = np.stack([mu, sigma], axis=1)

    return (mu, sigma, Z, data[:t])

# 参数配置
K = 5  # 高斯分布个数
M = 10000  # 数据个数
mu = np.array([150., 180, 100, 140, 210])
sigma = np.array([3, 4, 1, 3, 9])
# print(f"mu: {mu}, sigma: {sigma}")

T = 500
Theta0 = np.array([mu + np.random.choice(np.arange(-15,15), K) ,sigma + np.random.choice(np.arange(-2,2), K)])
# Theta0 = np.array([[147,164, 168, 179,195],[2,3,2,5,6]])

# 生成数据
Z = getIndex(K, M)
Y = getY(Z, mu, sigma, K, M)
# gaussEM
mu_pred, sigma_pred, Z_pred, data = gaussEM(K, M, T, Y, 0.001, Theta0)

accuracy = np.sum(Z == Z_pred) / M
print("Clustering accuracy: ", accuracy)
print(f"mu:{mu_pred}, sigma:{sigma_pred}")

# # 绘制 mu, sigma , Z准确率的变化
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(data[:, :, 0])
plt.title('mu')
plt.legend([f"mu_{i}" for i in range(K)])

plt.subplot(1, 2, 2)
plt.plot(data[:, :, 1])
plt.title('sigma')
plt.legend([f"sigma_{i}" for i in range(K)])

plt.show()




