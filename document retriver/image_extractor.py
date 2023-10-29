from pdf2image import convert_from_path
import os

# Define input and output directories
pdf_folder = r"C:\Users\RAMKUMAR K\Desktop\kivy search gui\local_drive_2"
output_folder = "extracted_images"

# Create the output directory if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate through PDF files in the input folder
for filename in os.listdir(pdf_folder):
    if filename.endswith(".pdf"):
        pdf_file = os.path.join(pdf_folder, filename)

        # Convert the PDF to a list of images
        images = convert_from_path(pdf_file)

        # Save the images to the output folder
        for img_index, image in enumerate(images):
            output_file = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_page{img_index+1}.jpg")
            image.save(output_file, "JPEG")

print("Images extracted and saved to the 'extracted_images' folder.")
