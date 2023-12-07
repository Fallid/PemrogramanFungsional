import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [3, 7, 2, 8, 5]
N = 5
area = (40 * np.random.rand(N))**2
colors = np.random.rand(N)
plt.scatter(x, y, c=colors, s=area,marker="X")
plt.show()