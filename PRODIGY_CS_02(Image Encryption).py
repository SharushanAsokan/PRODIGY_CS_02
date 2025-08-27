#Import Pillow Image class for working with images
from PIL import Image

#Import os for working with file paths
import os

print("//////////////////////////////////////////////////////////")
print("         Pixel Manipulation for Image Encryption")
print("//////////////////////////////////////////////////////////")
print(" ")

#Image encryption function 
def encrypt_image(image_path, key, output_path):
# Open the image from the given file path    
    img = Image.open(image_path)
# Load the image pixels into a 2D pixel map     
    pixels = img.load()

# Loop over each pixel column
    for i in range(img.width):
# Loop over each pixel row        
        for j in range(img.height):
# Get the RGB values of the current pixel            
            r, g, b = pixels[i, j]
            
# Encrypt each color channel by adding the key and wrapping around 256            
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
 # Replace the old pixel with the new encrypted RGB value            
            pixels[i, j] = (r, g, b)

 # Save the modified encrypted image to the output path
    img.save(output_path)

# Print confirmation of saved encrypted image with absolute path    
    print(f"Encrypted image saved at: {os.path.abspath(output_path)}")

#Image decryption function 
def decrypt_image(image_path, key, output_path):
    
# Open the image from the given file path
    img = Image.open(image_path)
    
# Load the image pixels into a 2D pixel map
    pixels = img.load()

# Loop over each pixel column
    for i in range(img.width):
# Loop over each pixel row
        for j in range(img.height):
# Get the RGB values of the current pixel
            r, g, b = pixels[i, j]
            
# Decrypt each color channel by subtracting the key and wrapping around 256
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            
# Replace the old pixel with the new decrypted RGB value
            pixels[i, j] = (r, g, b)

# Save the modified (decrypted) image to the output path
    img.save(output_path)
    
# Print confirmation of saved decrypted image with absolute path
    print(f"Decrypted image saved at: {os.path.abspath(output_path)}")

# Ask the user whether they want to encrypt or decrypt
mode = input("Do you want to encrypt or decrypt? (e/d): ").lower()

# Ask the user for the path of the input image
file_path = input("Enter image path: ").strip()

# If the user included quotes around the path, remove them
if (file_path.startswith('"') and file_path.endswith('"')) or \
   (file_path.startswith("'") and file_path.endswith("'")):
    file_path = file_path[1:-1]

# Replace Windows backslashes with forward slashes to standardize paths
file_path = file_path.replace("\\", "/")

# Ask the user for an encryption/decryption key (must be between 0 and 255)
key = int(input("Enter numeric key (0-255): "))

# Ask the user for an encryption/decryption key (must be between 0 and 255)
output_name = input("Enter output file name: ").strip()

# If no extension is given, default to saving as a .png file
if "." not in output_name:
    output_name += ".png"

# Save the output in the same folder as the input image
folder_path = os.path.dirname(file_path)
output_file = os.path.join(folder_path, output_name)

# Perform encryption if user chose 'e'
if mode == 'e':
    encrypt_image(file_path, key, output_file)
    
# Perform decryption if user chose 'd'
elif mode == 'd':
    decrypt_image(file_path, key, output_file)
    
# If the user typed something else, print an error message    
else:
    print("Invalid option. Please enter 'e' or 'd'.")