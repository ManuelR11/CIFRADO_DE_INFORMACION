import base64
import numpy as np
from PIL import Image
from Script_Criptografia import ascii_to_binary, binary_to_ascii

def image_to_base64(image_path):
    """Convierte una imagen a Base64"""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

def base64_to_bytes(base64_str):
    """Convierte Base64 a bytes"""
    return base64.b64decode(base64_str)

def xor_images(image_path1, image_path2, output_path):
    """Aplica XOR entre dos imágenes a color y guarda el resultado"""
    # Cargar imágenes y redimensionarlas al mismo tamaño
    img1 = Image.open(image_path1).convert('RGB')
    img2 = Image.open(image_path2).convert('RGB')
    img2 = img2.resize(img1.size)
    
    # Convertir imágenes a arrays NumPy
    img1_array = np.array(img1)
    img2_array = np.array(img2)
    
    # Aplicar XOR en cada canal de color (R, G, B)
    xor_result_array = np.bitwise_xor(img1_array, img2_array)
    
    # Convertir a imagen y guardar
    xor_result_img = Image.fromarray(xor_result_array)
    xor_result_img.save(output_path)
    
    print("Imagen XOR generada y guardada como:", output_path)

# Parámetros
image_path1 = r"Laboratorio_2B/Baseball_back.png"  # Ruta de la primera imagen
image_path2 = r"Laboratorio_2B/Baseball.png"  # Ruta de la segunda imagen
output_path = r"Laboratorio_2B/imagen_xor.png"

# Ejecutar XOR de imágenes
xor_images(image_path1, image_path2, output_path)
