from PIL import Image

# TODO 1 : Buka gambar latar belakang (background) dan gambar yang ingin disisipkan (overlay)
background_image = Image.open("Images/labitUMM.jpg")
overlay_image = Image.open("Images/freyapt3.jpg")

# TODO 2 : Konversi overlay image ke mode RGB (menghilangkan alpha channel)
overlay_image = overlay_image.convert("RGB")
overlay_image.load()

# TODO 3 : (optional) Perkecil ukuran gambar overlay menggunakan method resize()
width, height = overlay_image.size
new_width = 500
# Rumus untuk menghitung rasio height tanpa menghancurkan rasio asli dari gambar
new_height = int((new_width / width) * height)
overlay_image = overlay_image.resize((new_width, new_height), Image.LANCZOS)

overlay_mask = overlay_image.convert("L")

x_center = (background_image.width - overlay_image.width) // 2
y_center = (background_image.height - overlay_image.height) // 2

# TODO 4 : Sisipkan gambar overlay ke dalam gambar background menggunakan method paste()
background_image.paste(overlay_image, (x_center, y_center), mask=overlay_mask)

# TODO 5 : Simpan gambar hasil edit
background_image.save("Images/hasil_edit_gambar_noalpha.jpg")

# TODO 6 : Tampilkan
background_image.show()