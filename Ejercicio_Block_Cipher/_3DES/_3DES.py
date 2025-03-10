from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def triple_des_encrypt_cbc(plaintext):
    key = DES3.adjust_key_parity(get_random_bytes(24))  # Clave de 24 bytes
    iv = get_random_bytes(8)  # IV de 8 bytes
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    padded_text = pad(plaintext.encode(), DES3.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return key, iv, ciphertext

def triple_des_decrypt_cbc(key, iv, ciphertext):
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(ciphertext), DES3.block_size)
    return decrypted.decode()

# Prueba con texto plano
if __name__ == "__main__":
    plaintext = "Hola 3DES"  # Texto directo

    # with open("3des.txt", "r") as f:
    #     plaintext = f.read()

    key, iv, encrypted = triple_des_encrypt_cbc(plaintext)
    decrypted = triple_des_decrypt_cbc(key, iv, encrypted)

    print("Texto original:", plaintext)
    print("Texto cifrado:", encrypted.hex())
    print("Texto descifrado:", decrypted)
