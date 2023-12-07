import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Data tinggi badan individu dalam sentimeter
tinggi_badan = [165, 170, 155, 172, 180, 160, 175, 165, 185, 175, 170, 160]
interval_size = 10  # Misalnya interval ukuran per 10 sentimeter

# Fungsi untuk mengelompokkan tinggi badan ke dalam interval tertentu
def group_into_intervals(data, interval_size):
    grouped_data = {}
    for value in data:
        interval_lower = (value // interval_size) * interval_size
        interval_upper = interval_lower + interval_size
        interval = (interval_lower, interval_upper)
        if interval not in grouped_data:
            grouped_data[interval] = 0
        grouped_data[interval] += 1
    return grouped_data

# Menghitung frekuensi tinggi badan dalam interval
frekuensi_tinggi_badan = group_into_intervals(tinggi_badan, interval_size)

# Visualisasi data dalam bentuk histogram dan kurva PDF
intervals = list(frekuensi_tinggi_badan.keys())
frekuensi = list(frekuensi_tinggi_badan.values())

# Menghitung kurva PDF
mu, std = np.mean(tinggi_badan), np.std(tinggi_badan)
xmin, xmax = min(tinggi_badan), max(tinggi_badan)
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)

# Normalisasi kurva PDF
scaling_factor = 0.5 / max(p)  # Sesuaikan faktor skala agar frekuensi mencapai 6
p_scaled = p * scaling_factor

# Flatten the list of tuples into a 1-dimensional array
flat_intervals = np.array(intervals).ravel()

# Sort the intervals to ensure they are in increasing order
sorted_intervals = sorted(flat_intervals)

# Menampilkan histogram dengan kurva PDF tumpang tindih
plt.hist(tinggi_badan, bins=sorted_intervals, color='blue', alpha=0.7, label='Histogram')
plt.plot(x, p_scaled * len(tinggi_badan), 'k', linewidth=1, label='PDF', color='red')
plt.xlabel('Tinggi Badan (cm)')
plt.ylabel('Frekuensi')
plt.title('Histogram dan Kurva PDF Tinggi Badan')
plt.legend()
plt.show()
