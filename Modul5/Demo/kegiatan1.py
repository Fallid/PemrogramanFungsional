import matplotlib.pyplot as plt
from functools import reduce

# Data nilai-nilai ujian mahasiswa
nilai_mahasiswa = [75, 80, 90, 65, 70, 85, 95, 78, 88, 92]

# TODO 1: Menghitung rata-rata menggunakan fungsi reduce
rata_rata = reduce(lambda x, y: x + y, nilai_mahasiswa) / len(nilai_mahasiswa)

# TODO 2: Membuat label mahasiswa (sumbu x) dalam bentuk fungsional dinamis (list-map-lambda)
label_mahasiswa = list(map(lambda x: f'{x+1}', range(len(nilai_mahasiswa))))

# TODO 3: Visualisasi data dalam bentuk diagram batang
plt.bar(label_mahasiswa, nilai_mahasiswa, color='blue')
plt.xlabel('Mahasiswa')
plt.ylabel('Nilai Ujian')
plt.title('Diagram Batang Nilai Ujian Mahasiswa')
plt.axhline(rata_rata, color='red', linestyle='dashed', linewidth=2, label=f'Rata-rata: {rata_rata:.2f}')
plt.legend()
plt.show()
