from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import numpy as np
from PIL import Image
import os

def load_image(image_path):
    img = Image.open(image_path).convert("L") 
    img_data = np.array(img) 
    return img, img_data.tobytes()

def save_encrypted_image(encrypted_bytes, original_size, output_path):
    encrypted_array = np.frombuffer(encrypted_bytes, dtype=np.uint8).reshape(original_size)
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save(output_path)
    print(f"Imagen guardada: {output_path}")

def encrypt_aes_ecb(image_bytes, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_image = pad(image_bytes, AES.block_size)
    encrypted_bytes = cipher.encrypt(padded_image)
    return encrypted_bytes

def encrypt_aes_cbc(image_bytes, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_image = pad(image_bytes, AES.block_size)
    encrypted_bytes = cipher.encrypt(padded_image)
    return encrypted_bytes

def main():
    image_path = "Laboratorio_3/tux.ppm" 
    key = get_random_bytes(16)  
    iv = get_random_bytes(16) 

    img, img_bytes = load_image(image_path)
    original_size = img.size[::-1] 


    encrypted_ecb = encrypt_aes_ecb(img_bytes, key)
    save_encrypted_image(encrypted_ecb[:len(img_bytes)], original_size, "Laboratorio_3/tux_ecb.bmp")

    encrypted_cbc = encrypt_aes_cbc(img_bytes, key, iv)
    save_encrypted_image(encrypted_cbc[:len(img_bytes)], original_size, "Laboratorio_3/tux_cbc.bmp")


    img.show(title="Imagen Original")
    Image.open("tux_ecb.bmp").show(title="AES-ECB")
    Image.open("tux_cbc.bmp").show(title="AES-CBC")

if __name__ == "__main__":
    main()
