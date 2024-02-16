import tensorflow as tf  
import numpy as np  
import matplotlib.pyplot as plt  
  
# 读取散点数据  
X = []  
Y = []  
Z = []  
  
with open("./ex1.dat") as file:  
    for line in file:  
        x, y, z = line.split(",")  
        X.append(float(x))  
        Y.append(float(y))  
        Z.append(float(z))  
  
X = np.array(X)  
Y = np.array(Y)  
Z = np.array(Z)  
  
# 构建神经网络模型  
model = tf.keras.Sequential([  
    tf.keras.layers.Dense(64, activation='relu', input_shape=(2,)),  
    tf.keras.layers.Dense(64, activation='relu'),  
    tf.keras.layers.Dense(1)  
])  
  
model.compile(optimizer='adam', loss='mean_squared_error')  
  
# 训练模型  
model.fit(x=np.column_stack((X, Y)), y=Z, epochs=100)  
  
# 可视化拟合结果  
fig = plt.figure()  
ax = fig.add_subplot(111, projection='3d')  
  
# 绘制散点图  
ax.scatter(X, Y, Z)  
  
# 生成拟合曲面  
x_surf = np.linspace(min(X), max(X), 100)  
y_surf = np.linspace(min(Y), max(Y), 100)  
x_surf, y_surf = np.meshgrid(x_surf, y_surf)  
z_surf = model.predict(np.column_stack((x_surf.ravel(), y_surf.ravel()))).reshape(x_surf.shape)  
  
# 绘制拟合曲面  
ax.plot_surface(x_surf, y_surf, z_surf, cmap='viridis', alpha=0.5)  
  
ax.set_xlabel('X Label')  
ax.set_ylabel('Y Label')  
ax.set_zlabel('Z Label')  
  
plt.show()  