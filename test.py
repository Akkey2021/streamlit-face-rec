import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2)
dx = 0.1  # xの微小な変化
e = np.e  # ネイピア数

y_e = e**x  # 元のべき乗の関数
y_de = (e**(x+dx) - e**x) / dx  # yの微小な変化/xの微小な変化

plt.plot(x, y_e, label="e^x")
plt.plot(x, y_de, label="de")
plt.legend()

plt.xlabel("x", size=14)
plt.ylabel("y", size=14)
plt.grid()
plt.show()
