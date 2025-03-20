from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes

def chacha20_encrypt(plaintext):
    key = get_random_bytes(32)  # ChaCha20 usa clave de 256 bits
    nonce = get_random_bytes(12)  # Nonce recomendado de 96 bits
    cipher = ChaCha20.new(key=key, nonce=nonce)
    ciphertext = cipher.encrypt(plaintext.encode())
    return key, nonce, ciphertext

def chacha20_decrypt(key, nonce, ciphertext):
    cipher = ChaCha20.new(key=key, nonce=nonce)
    decrypted = cipher.decrypt(ciphertext)
    return decrypted.decode()

# 🔄 PRUEBA directa de cifrado y descifrado
if __name__ == "__main__":
    mensaje = "Este es un mensaje secreto usando ChaCha20"
    
    # Cifrado
    key, nonce, ciphertext = chacha20_encrypt(mensaje)
    
    # Descifrado
    decrypted = chacha20_decrypt(key, nonce, ciphertext)
    
    # Resultados
    print("Mensaje original:", mensaje)
    print("Clave:", key.hex())
    print("Nonce:", nonce.hex())
    print("Cifrado (hex):", ciphertext.hex())
    print("Descifrado:", decrypted)
