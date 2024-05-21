import numpy as np
np.set_printoptions(threshold=np.inf)
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
from matplotlib import path, animation
import itertools

#*********************************************************************************
##########################参数###############################################
n = 1000    # 定义矩阵大小（根据实际情况，n=max {[L_x/d], [L_y/d]}）
plane_nums = 5  #无人机数量
MaxTime = 1500  #最大时间
totaltime = 0   #初始化当前用时
speed  = 30   #无人机速度 (d*m/s)
frequence =500  #图像采样频率
points = np.array([[100,300],[600, 0], [900, 0], [200, 800]])  # 指定区域边界
output = "output.gif" #输出文件名

#***********************************************************************************
# 对这些点创建凸包
hull = ConvexHull(points)

# 创建网格点
x = np.arange(n)
y = np.arange(n)
xv, yv = np.meshgrid(x, y)

# 检查网格中的每个点是否在凸包内
path_points = path.Path(points[hull.vertices])
mask = path_points.contains_points(np.vstack([xv.flatten(), yv.flatten()]).T)
mask.shape = xv.shape

# 根据 mask 创建一个全零矩阵，并在 mask 为 True 的地方置为 1
matrix = np.zeros((n, n))
matrix[mask] = 1

# 删除全零行和全零列
matrix = matrix[~np.all(matrix == 0, axis=1)]
matrix = matrix[:, ~np.all(matrix == 0, axis=0)]

matrix = np.pad(matrix, pad_width=1, mode='constant', constant_values=0)


# 创建一个用于记录搜索轨迹的矩阵
#matrix_trace = matrix.copy()
all_matrix = []

#分割
#计算每个区域的点数
every_drone_point = len(np.argwhere(matrix == 1)) / plane_nums
last_line = 0

for index in range(plane_nums):
    if index == plane_nums - 1:
        last = np.argwhere(matrix == 1)
        matrix[last[:, 0], last[:, 1]] = 10*(index + 1)
        break

    drone_points = 0
    for line in range(last_line, 9999999):
        for i, j in itertools.product(range(matrix.shape[0]), range(min(line, matrix.shape[1]))):
            if matrix[i, j] == 1:
                drone_points += 1
                matrix[i, j] = 10*(index + 1)

        if drone_points >= every_drone_point:
            last_line = line
            break


#搜索

number_list = [ 10*(index+1) for index in range(plane_nums)]
number_list.append(0)
number_list.append(2)

print(number_list)
while np.any((matrix != 0) & (matrix != 2)):
    #print(111)
    bounds = []
    counter = 0 #计数采样频率

    #对每架无人机赵边界
    for index in range(plane_nums):
        bound = []
        number_list.remove(10*(index+1))
        #每个的边界搜索
        for i in range(0, matrix.shape[0] - 1):
            for j in range(0, matrix.shape[1] - 1):
                #if matrix[i][j] == 1:
                if \
                    (matrix[i][j] == 10*(index + 1)) and \
                    (matrix[i - 1][j] in number_list or matrix[i + 1][j] in number_list or matrix[i][j - 1] in number_list or matrix[i][j + 1] in number_list) :
                    bound.append([i, j])
                    matrix[i,j] = 3
        number_list.append(10*(index+1))

        bound = np.array(bound)
        if bound.size != 0:
            bound = bound[np.argsort(np.arctan2(bound[:,1] - np.mean(bound[:,1]), bound[:,0] - np.mean(bound[:,0])))]
        else:
            bound = np.array(bound).reshape(-1, 2)
        bounds.append(bound)
    
    #若所有边界都为空，则跳出循环
    condition = 0
    for index in range(plane_nums):
        if bounds[index].size != 0:
            condition = 1
    
    if condition == 0:
        break

    #开始遍历
    while(True):

        if max(len(i) for i in bounds) <= counter:
            break

        for bound in bounds:
            #该边界已遍历完
            if len(bound) <= counter:
                pass
            else:
                i, j =bound[counter]
                matrix[i,j] = 2
        
        if counter % frequence == 0:
            all_matrix.append(matrix.copy())

        counter += 1
        #print(matrix)
        totaltime += 1.0 / speed

        if totaltime > MaxTime: #超时
            break

    if totaltime > MaxTime: #超时
            break


print("===================================================================")
print("无人机速度：{:.2f}".format(speed))
print("总用时：{:.2f}".format(totaltime))
print("仿真完成，正在生成动态图像，过程可能较长，请稍等")
# 使用自定义颜色映射来改变颜色，0为黑色，1为白色，表示待搜索区域，2为绿色（表示已搜索区域）
cmap = plt.cm.colors.ListedColormap(['black', 'white', 'green', 'blue', "yellow", "purple", "grey", "pink", "lightblue", "c", "teal"])
bounds=[-2, 0.5, 1.5, 2.5, 3.5, 11, 21, 31, 41, 51, 61, 71]
norm = plt.cm.colors.BoundaryNorm(bounds, cmap.N)


def animate(frame):
    ax.clear()
    im = ax.imshow(all_matrix[frame], cmap=cmap, norm=norm, origin='lower')
    return [im]

# 创建动画
fig, ax = plt.subplots(figsize=(8, 8))
ani = animation.FuncAnimation(fig, animate, frames=len(all_matrix), interval=5, blit=True)

# 保存动画
ani.save(output, writer='pillow')

# 显示动画
plt.show()
