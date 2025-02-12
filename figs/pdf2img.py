from pdf2image import convert_from_path
import os

# Input PDF file path
pdf_path = "/home/tianyizhou/FourierNumber.github.io/figs/teaser.pdf"
output_folder = "/home/tianyizhou/FourierNumber.github.io/figs/slides"

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Convert PDF to images
images = convert_from_path(pdf_path, dpi=300)  # Adjust DPI for quality

# Save each page as an image
for i, image in enumerate(images):
    image_path = os.path.join(output_folder, f"slide{i+1}.png")
    image.save(image_path, "PNG")
    print(f"Saved {image_path}")

print("PDF conversion completed!")
