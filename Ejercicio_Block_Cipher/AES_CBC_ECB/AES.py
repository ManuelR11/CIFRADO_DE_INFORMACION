from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def aes_encrypt_text(plaintext):
    key = get_random_bytes(16)  # Clave de 16 bytes
    iv = get_random_bytes(16)  # IV de 16 bytes
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return key, iv, ciphertext

def aes_decrypt_text(key, iv, ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted.decode()

def aes_encrypt_image(file_path):
    key = get_random_bytes(16)  # Clave de 16 bytes
    iv = get_random_bytes(16)  # IV de 16 bytes

    with open(file_path, 'rb') as f:
        plaintext = f.read()

    cipher_ecb = AES.new(key, AES.MODE_ECB)
    ciphertext_ecb = cipher_ecb.encrypt(pad(plaintext, AES.block_size))

    cipher_cbc = AES.new(key, AES.MODE_CBC, iv)
    ciphertext_cbc = cipher_cbc.encrypt(pad(plaintext, AES.block_size))

    return key, iv, ciphertext_ecb, ciphertext_cbc

def aes_decrypt_image(key, iv, ciphertext_ecb, ciphertext_cbc):
    cipher_ecb = AES.new(key, AES.MODE_ECB)
    decrypted_ecb = unpad(cipher_ecb.decrypt(ciphertext_ecb), AES.block_size)

    cipher_cbc = AES.new(key, AES.MODE_CBC, iv)
    decrypted_cbc = unpad(cipher_cbc.decrypt(ciphertext_cbc), AES.block_size)

    return decrypted_ecb, decrypted_cbc

# Prueba con texto y una imagen
if __name__ == "__main__":
    # Prueba con texto
    plaintext = "Hola AES"
    
    key_text, iv_text, encrypted_text = aes_encrypt_text(plaintext)
    decrypted_text = aes_decrypt_text(key_text, iv_text, encrypted_text)

    print("Texto original:", plaintext)
    print("Texto cifrado (AES CBC):", encrypted_text.hex())
    print("Texto descifrado:", decrypted_text)

    # Prueba con imagen
    key_img, iv_img, ciphertext_ecb, ciphertext_cbc = aes_encrypt_image("Ejercicio_Block_Cipher/AES-CBC_ECB/pic.png")
    decrypted_ecb, decrypted_cbc = aes_decrypt_image(key_img, iv_img, ciphertext_ecb, ciphertext_cbc)

    # Guardar imágenes descifradas
    with open('pic_ecb_dec.png', 'wb') as f:
        f.write(decrypted_ecb)
    with open('pic_cbc_dec.png', 'wb') as f:
        f.write(decrypted_cbc)

    print("\n--- AES Imagen en ECB ---")
    print("Imagen cifrada (ECB):", ciphertext_ecb.hex()[:100], "...")  # Mostrando solo los primeros 100 caracteres
    print("Imagen descifrada (ECB):", decrypted_ecb[:10])  # Mostrando los primeros bytes descifrados

    print("\n--- AES Imagen en CBC ---")
    print("Imagen cifrada (CBC):", ciphertext_cbc.hex()[:100], "...")  # Mostrando solo los primeros 100 caracteres
    print("Imagen descifrada (CBC):", decrypted_cbc[:10])  # Mostrando los primeros bytes descifrados

    print("Imagen cifrada en ECB y CBC, descifrada correctamente.")
