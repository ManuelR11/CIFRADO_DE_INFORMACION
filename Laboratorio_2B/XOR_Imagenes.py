import base64
import numpy as np
from PIL import Image
from Script_Criptografia import ascii_to_binary, binary_to_ascii

def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

def base64_to_bytes(base64_str):
    return base64.b64decode(base64_str)

def xor_images(image_path1, image_path2, output_path):
    # Imagenes al mismo tamano
    img1 = Image.open(image_path1).convert('L')
    img2 = Image.open(image_path2).convert('L')
    img2 = img2.resize(img1.size)
    
    img1_array = np.array(img1)
    img2_array = np.array(img2)
    
    # XOR de bits
    xor_result_array = np.bitwise_xor(img1_array, img2_array)
    
    # Save
    xor_result_img = Image.fromarray(xor_result_array)
    xor_result_img.save(output_path)
    
    print("Imagen XOR generada y guardada como:", output_path)


image_path1 = r"Laboratorio_2B/Baseball_back.png" 
image_path2 = r"Laboratorio_2B/Baseball.png" 
output_path = r"Laboratorio_2B/imagen_xor.png"


xor_images(image_path1, image_path2, output_path)
