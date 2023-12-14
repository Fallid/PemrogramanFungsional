_author_ = "Ahmad Naufal"
_copyright_ = "Copyright 2023, malang"

# TODO 0 : Import library lain yang dibutuhkan
from PIL import Image, ImageDraw, ImageFont


# TODO 1: Lakukan load image pada variabel berikut
# hint: kalian bisa gunakan fungsi open()
gambarku = Image.open("Images/labitUMM.jpg")


# TODO 2: Ubah gambar menjadi hitam-putih
# hint: kalian bisa gunakan fungsi convert()
gambarBW = gambarku.convert("L")


# TODO 3: Tambahkan text sesuai kriteria.
draw = ImageDraw.Draw(gambarBW)
font = ImageFont.truetype("arial.ttf", 24)
text = f"{_author_} 202110370311296"
text_width = draw.textlength(text, font)
text_x = (gambarku.width - text_width) // 2
text_y = gambarku.height / 2
draw.text((text_x, text_y), text, font=font, fill="black")


# TODO 4: Simpan gambar hasil edit menggunakan fungsi save()
gambarBW.save("Images/percobaan_satu.jpg")


# TODO 5: Tampilkan hasil akhir gambar
gambarBW.show()