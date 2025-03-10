from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def des_encrypt_ecb(plaintext):
    key = get_random_bytes(8)  # Clave de 8 bytes
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext.encode(), DES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return key, ciphertext

def des_decrypt_ecb(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted = unpad(cipher.decrypt(ciphertext), DES.block_size)
    return decrypted.decode()

# Prueba con texto plano
if __name__ == "__main__":
    plaintext = "Hola DES"  # Texto directo

    # with open("des.txt", "r") as f:
    #     plaintext = f.read()

    key, encrypted = des_encrypt_ecb(plaintext)
    decrypted = des_decrypt_ecb(key, encrypted)

    print("Texto original:", plaintext)
    print("Texto cifrado:", encrypted.hex())
    print("Texto descifrado:", decrypted)
