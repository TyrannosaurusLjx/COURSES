import numpy as np
from scipy.optimize import minimize

def target_function(X: np.array) -> float:
    x, y = X
    r = np.sqrt(np.abs(x**2 + y**2 + (x-y)**2*x))
    return 100 / (1 + np.exp(-r))

# 要最大化的函数的负值（因为 minimize 是最小化函数）
def neg_target_function(X: np.array) -> float:
    return -target_function(X)

# 初始猜测的 x 和 y 值
initial_guess = np.array([0, 0])

# 使用 minimize 找到负目标函数的最小值，也就是原函数的最大值
result = minimize(neg_target_function, initial_guess)

# 最大值的位置和对应的函数值
max_point = result.x
max_value = -result.fun  # 恢复原函数值

print("最大值发生在: ", max_point)
print("最大值: ", max_value)