import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
y3 = np.array([5, 10, 5, 7, 9])

# Membuat plot untuk garis y1 dan y2
plt.plot(y1, label='Garis 1', linestyle='-.', color="red")
plt.plot(y2, label='Garis 2', linestyle='--', color="green")
plt.plot(y3, label='Garis 3', linestyle=':', color="blue")

# Menambahkan judul dan label sumbu
plt.title('Plot Dua Garis')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')

# Menambahkan keterangan (legend)
plt.legend()
plt.show()