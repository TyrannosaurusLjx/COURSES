import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

def fitness_function(x):
    return np.sin(x) + np.cos(5 * x) + 1 / (1 + 0.4 * x**2) + 3

# 设置初始猜测值
initial_guess = 0.0  # 可以选择一个初始猜测值

# 调用 minimize 函数进行优化
result = minimize(lambda x: - fitness_function(x), initial_guess, bounds=[(-5, 5)])  # 设定优化的区间

# 输出优化结果
print(f"Optimal solution: {result.x}")
print(f"Minimum value: {-result.fun}")

# plot and save
x = np.linspace(-10, 10, 1000)
y = fitness_function(x)
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Fitness Function")
plt.savefig("../assets/img/fitness_function.png")
plt.show()