_author_ = "Ahmad Naufal"
_copyright_ = "Copyright 2023, malang"

from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter

# Load images
background = Image.open("Images/bg.jpg")
overlay = Image.open("Images/logo.jpg")
font_path = "Typograph/arial.ttf" 

# Resize background
background = background.resize((1920, 1080))

# Convert background to grayscale, rotate by 30 degrees, and apply blur
bg_copy = background.convert("L")
rotated = bg_copy.rotate(30)
final_bg = rotated.filter(ImageFilter.BLUR)

# Enhance brightness and contrast of overlay
enhancer = ImageEnhance.Brightness(overlay.copy())
brightened = enhancer.enhance(1.89)

enhancer = ImageEnhance.Contrast(brightened)
contrasted = enhancer.enhance(1.89)
final = contrasted.resize((600, 600))

# Add text to the overlay
padding = 170
customFont = ImageFont.truetype(font_path, 24)
draw = ImageDraw.Draw(final)
text = "INFORMATIKA JOSSS!"
text_width = draw.textlength(text, font=customFont)
text_height = draw.textlength(text, font=customFont)
text_position = ((final.width - text_width) // 2, final.height - text_height + padding)
draw.text(text_position, text, font=customFont, fill="red")


# Paste the overlay onto the background
final_bg.paste(final, (600, 300))

# Show and save the final image
final_bg.show()
final_bg.save("Images/tugas_praktikum_enam.jpg")