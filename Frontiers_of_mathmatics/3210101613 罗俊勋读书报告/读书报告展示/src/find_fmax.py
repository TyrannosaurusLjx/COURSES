# $\sin(\frac{\pi}{3}x)\sin(\frac{\pi}{3}y) + \cos(\frac{\pi}{4}x)\cos(\frac{\pi}{4}y)$

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize, differential_evolution, dual_annealing

# 找最大值


def f(xy):
    x, y = xy
    result = np.sin(np.pi*x / 3)*np.sin(np.pi*y / 3) + \
        np.cos(np.pi*x / 4)*np.cos(np.pi*y / 4)
    return 10 - result


# 定义范围
bounds = [(-0.1, 0.1), (-0.1, 0.1)]


def global_optimization_diff_evolution():
    result = differential_evolution(f, bounds)
    return result.x, result.fun


def global_optimization_dual_annealing():
    result = dual_annealing(f, bounds)
    return result.x, result.fun


global_solution_diff, global_value_diff = global_optimization_diff_evolution()
global_solution_anneal, global_value_anneal = global_optimization_dual_annealing()


# 输出结果
print("\n差分进化全局最优化结果：")
print("最优解：", global_solution_diff)
print("目标函数值：", global_value_diff)
print("\n模拟退火全局最优化结果：")
print("最优解：", global_solution_anneal)
print("目标函数值：", global_value_anneal)

# 绘制函数图像以验证结果
x = np.linspace(-20, 20, 400)
y = np.linspace(-20, 20, 400)
X, Y = np.meshgrid(x, y)
Z = f([X, Y])


fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7)
ax.scatter(*global_solution_diff, global_value_diff,
           color='g', label="Global Minima (DE)", s=50)
ax.scatter(*global_solution_anneal, global_value_anneal,
           color='b', label="Global Minima (SA)", s=50)
ax.legend()
plt.title("Function Visualization and Optimization Results")
plt.show()
