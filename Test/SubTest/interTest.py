import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import matplotlib

# 设置图标字体
matplotlib.rcParams['font.family'] = "SimHei"
matplotlib.rcParams['font.size'] = 20

# 原始数据点
x = np.array([1, 3, 9, 20])
y = np.array([2, 4, 6, 1000])

# 创建三次插值函数
f = interp1d(x, y, kind='cubic')

# 生成均匀分布的 X 轴数据点
x_new = np.linspace(x.min(), x.max(), 1000)

# 使用插值函数计算对应的 Y 轴值
y_new = f(x_new)

# 绘制原始数据点和插值后的数据点
plt.plot(x, y, 'o', label='原始数据点')
plt.plot(x_new, y_new, 'o', label='插值后的数据点')
plt.legend()
plt.show()