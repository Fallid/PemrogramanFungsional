import matplotlib.pyplot as plt
import numpy as np

data_transaksi = [
    ("Produk A", 50, 10),
    ("Produk B", 30, 25),
    ("Produk C", 20, 30),
    ("Produk D", 60, 8),
    ("Produk E", 40, 15),
    ("Produk F", 70, 5),
]

# Ekstrak harga produk dan jumlah produk terjual
harga_produk = [item[1] for item in data_transaksi]
jumlah_terjual = [item[2] for item in data_transaksi]

# Menghitung total pendapatan untuk setiap produk
total_pendapatan = [item[1] * item[2] for item in data_transaksi]

# Membuat label produk
produk_labels = [item[0] for item in data_transaksi]

# Membuat subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

# Scatter plot (diagram titik)
ax1.scatter(harga_produk, jumlah_terjual, color='blue')
ax1.set_xlabel('Harga Produk')
ax1.set_ylabel('Jumlah Produk Terjual')
ax1.set_title('Scatter Plot Hubungan Harga dan Jumlah Terjual')

# Bar chart (diagram balok)
ax2.bar(produk_labels, total_pendapatan, color='cyan')
ax2.set_xlabel('Produk')
ax2.set_ylabel('Total Pendapatan')
ax2.set_title('Diagram Balok Total Pendapatan Produk')

plt.tight_layout()
plt.show()
