import numpy as np  
import matplotlib.pyplot as plt  
  
def f(x):  
    c = 1  # 可根据需要调整系数c  
    return c * x**2 * np.exp(-x)  
  
def metropolis_sampler(num_samples, delta):  
    samples = []  
    x = np.random.uniform(1, 10)  # 选择一个初始状态  
    for _ in range(num_samples):  
        x_candidate = np.random.uniform(x - delta, x + delta)  # 从邻域中采样候选状态  
        acceptance_prob = min(1, (f(x_candidate) / f(x)))  # 计算接受概率  
        if np.random.uniform(0, 1) < acceptance_prob:  # 根据接受概率决定是否接受新状态  
            x = x_candidate  
        samples.append(x)  
    return samples  
  
# 设置参数  
num_samples = 10000  # 采样数量  
delta = 0.5  # 邻域宽度  
  
# 进行采样  
samples = metropolis_sampler(num_samples, delta)  
  
# 绘制采样结果  
plt.hist(samples, bins=50, density=True, label='Samples')  
x = np.linspace(0, 10, 100)  
plt.plot(x, f(x), 'r', label='Target Distribution')  
plt.xlabel('x')  
plt.ylabel('Density')  
plt.legend()  
plt.show()  