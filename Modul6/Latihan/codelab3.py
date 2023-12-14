from PIL import Image, ImageEnhance

# TODO 1: Buka gambar menggunakan Pillow
image_path = "Images/hasil_edit_gambar_noalpha.jpg"
original_image = Image.open(image_path)

# TODO 2: Buat nilai contrast dan brightness baru yang berbeda
brightness_factor = 1.5  
contrast_factor = 1.2  

enhancer = ImageEnhance.Brightness(original_image)
brightened_image = enhancer.enhance(brightness_factor)

enhancer = ImageEnhance.Contrast(brightened_image)
final_image = enhancer.enhance(contrast_factor)

# TODO 3: Simpan gambar hasil edit dengan nama "brightness_contrast_image.jpg"
result_image_path = "Images/brightness_contrast_image.jpg"
final_image.save(result_image_path)

# TODO 4: Tampilkan hasilnya
final_image.show()