import random
import numpy as np
from matplotlib import pyplot as plt

mu = 0.5
sigma = 0.1
skip = 700 # 收敛步数
num = 10000 # 采样点数

def Gaussian(x):
    return 1/(sigma*np.sqrt(2*np.pi)) * np.exp(-(x-mu)**2 /(2*sigma**2))
def M_H():
    x_0 = 0
    samples = []
    j = 1
    while len(samples) <= num:
        while True:
            x_1 = random.random()
            p_j = Gaussian(x_1)
            p_i = Gaussian(x_0)
            alpha = min(p_j / p_i, 1.0)
            r = random.random()
            if r <= alpha:
                x_0 = x_1
                if j >= skip:
                    samples.append(x_1)
                j += 1
                break
    return samples
norm_samples = M_H()
x = np.linspace(0, 1, len(norm_samples))
plt.plot(x, Gaussian(x), label='normal distribution')
plt.hist(norm_samples, 100, density=True, color='red', label='samples distribution')
plt.title('Metropolis-Hastings',fontsize=19)
plt.ylabel('pdf', fontsize=19)
plt.xlabel('sample', fontsize=19)
plt.legend()
plt.show()