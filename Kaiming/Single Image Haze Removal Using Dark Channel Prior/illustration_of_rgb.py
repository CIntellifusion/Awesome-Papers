import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 生成坐标点
x = np.linspace(0, 255, 10)
y = np.linspace(0, 255, 10)
z = np.linspace(0, 255, 10)
X, Y, Z = np.meshgrid(x, y, z)

# 将坐标点展平
X_flat = X.flatten()
Y_flat = Y.flatten()
Z_flat = Z.flatten()

# 将坐标点的值映射到 0 到 1 之间
X_norm = X_flat / 255.0
Y_norm = Y_flat / 255.0
Z_norm = Z_flat / 255.0

# 创建 RGB 颜色数组
colors = np.stack([X_norm, Y_norm, Z_norm], axis=-1)

# 绘制图像
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制散点图
ax.scatter(X_flat, Y_flat, Z_flat, c=colors)

ax.set_xlabel('Red')
ax.set_ylabel('Green')
ax.set_zlabel('Blue')

plt.show()
