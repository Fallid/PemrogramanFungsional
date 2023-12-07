import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([1, 8, 10])
ypoints = np.array([3, 10, 5])



plt.figure(figsize=(5,5))
plt.plot(xpoints, ypoints,color='red',marker='o')
plt.xlabel('Perubahan Tiap Bulan')
plt.ylabel('Jumlah Populasi')
plt.title('Populasi Hewan')
plt.xlim([0,12])
plt.ylim([0,20])
plt.grid(True)
plt.show()