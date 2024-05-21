# 生成区域中 M 个 权重为 W_i 的搜集点
import random as rd
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
from matplotlib import pyplot as plt
# plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

# 计算两点之间的距离
def distance(a, b):
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# 计算 W_i/S_ij, 给出排序后的列表
def sort_map(p_i,map):
    return sorted(map,key=lambda x: x[-1]/distance(p_i,x[0:2]),reverse=True)

#******************************************************
##################参数#################################
m, n = 3000, 2000 # 区域大小 单位：米
M = 700 # 搜集点数量 
N = 5  # 无人机数量
S = 10000 # 设置最远飞行距离 单位：米
max_W, min_W = 100, 10 # 设置权上下限 
#########################################################

points = [[rd.randint(0, m), rd.randint(0, n),rd.randint(min_W,max_W)] for _ in range(M)]
copy_points = deepcopy(points)

# 路径

paths = []

for _ in range(N):
    path = [[0,0]] # 第 i 个无人机的路径
    temp_map = deepcopy(points)
    S_i = 0
    p_i = [0,0] # 起始点都设置成(0,0)

    while S_i < S:

        # 得到权重排序的序列
        sorted_map = sort_map(p_i,temp_map)

        # 如果所有剩下的距离都大于 S-S_i,则退出
        if all(distance(p_i, p) > S-S_i for p in sorted_map):
            break
         
        # 优先选择权重大的
        for point in sorted_map:
            dis_pi_to_point = distance(p_i,point)
            if dis_pi_to_point < S - S_i:
                path.append(point)
                # 从 pi开始
                p_i = point
                S_i += dis_pi_to_point
                # 删掉这个点
                temp_map.remove(point)
                points.remove(point) # 下一个无人机不能经过这个点
                break
            else:
                continue
        
    
    paths.append(path)

# 将所有点的权重相加就是全部搜索完的总收益
total_gain_all = sum([point[2] for point in copy_points])
print("全部搜索完的总收益:", total_gain_all)

# 无人机实际访问到的所有点的权重之和就是搜索到的总收益
total_gain_found = sum([point[2] for path in paths for point in path if len(point) > 2])
print("搜索到的总收益:", total_gain_found)

print("===================================")
print("搜索完成,搜索结果：")
print("若全部搜完的总收益：", total_gain_all)
print("实际的总收益：", total_gain_found)
print(f"收益率：{total_gain_found / total_gain_all:.2%}")

# 假设 paths 是一个包含多个路径的列表，每个路径是一个点的列表，例如 [[(x1, y1), (x2, y2), ...], [(x1, y1), (x2, y2), ...], ...]  

# 绘制点
fig, ax = plt.subplots(figsize=[10, 6])  # 调整画布大小
color_list = ['b', 'g', 'r', 'c', 'm', 'y', 'k']  # 颜色列表，为了区分不同无人机的路径

for i, path in enumerate(paths):
    x_values = [point[0] for point in path]
    y_values = [point[1] for point in path]
    plt.plot(x_values, y_values, marker='o', linewidth=2, linestyle='-', color=color_list[i%7])  # 使用不同颜色

# 标记未访问点
for point in copy_points:
    x, y, weight = point
    plt.scatter(x, y, marker='x', color='k')  # 使用不同标记和颜色
    plt.annotate(f'{weight}', (x, y), textcoords="offset points", xytext=(0,10), ha='center')

# 添加标题和标签
plt.title('Drone Paths')
plt.xlabel('X')
plt.ylabel('Y')

# 添加理论收益，实际收益及收益率
total_gain_all = sum([point[2] for point in copy_points])
total_gain_found = sum([point[2] for path in paths for point in path if len(point) > 2])
revenue_rate = total_gain_found / total_gain_all
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

info_text = f'expected: {total_gain_all}   actual: {total_gain_found}   ratio: {revenue_rate:.2%}'
plt.text(0.12, 1.05, info_text, transform=ax.transAxes, fontsize=12, horizontalalignment='center', verticalalignment='top', bbox=props)

plt.show()