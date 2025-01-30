import math

def encrypt_caesar(text: str, shift: int) -> str:
    shift = shift % 26
    encrypted = ""
    
    for char in text:
        if 'a' <= char <= 'z':
            encrypted += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            encrypted += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            encrypted += char
    
    return encrypted

def decrypt_caesar(text: str, shift: int) -> str:
    return encrypt_caesar(text, -shift)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("No existe inverso modular para el valor dado")

def position_in_alphabet(char: str) -> int:
    if 'a' <= char <= 'z':
        return ord(char) - ord('a')
    if char == 'ñ':
        return 14
    return -1

def letter_from_position(pos: int) -> str:
    if pos < 14:
        return chr(ord('a') + pos)
    if pos == 14:
        return 'ñ'
    return chr(ord('a') + pos - 1)

def encrypt_affine(text: str, a: int, b: int) -> str:
    m = 27  # Tamaño del alfabeto español (incluye la 'ñ')
    if gcd(a, m) != 1:
        raise ValueError("'a' debe ser coprimo con 27.")
    
    encrypted = ""
    for char in text:
        if 'a' <= char <= 'z' or char == 'ñ':
            x = position_in_alphabet(char)
            cipher = (a * x + b) % m
            encrypted += letter_from_position(cipher)
        else:
            encrypted += char
    
    return encrypted

def decrypt_affine(text: str, a: int, b: int) -> str:
    m = 27  # Tamaño del alfabeto español (incluye la 'ñ')
    inv_a = mod_inverse(a, m)
    
    decrypted = ""
    for char in text:
        if 'a' <= char <= 'z' or char == 'ñ':
            y = position_in_alphabet(char)
            plain = (inv_a * (y - b + m)) % m
            decrypted += letter_from_position(plain)
        else:
            decrypted += char
    
    return decrypted

def encrypt_vigenere(text: str, key: str) -> str:
    encrypted = ""
    key = key.lower()
    key_length = len(key)
    
    for i, char in enumerate(text):
        if 'a' <= char <= 'z':
            shift = ord(key[i % key_length]) - ord('a')
            encrypted += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            shift = ord(key[i % key_length]) - ord('a')
            encrypted += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            encrypted += char
    
    return encrypted

def decrypt_vigenere(text: str, key: str) -> str:
    decrypted = ""
    key = key.lower()
    key_length = len(key)
    
    for i, char in enumerate(text):
        if 'a' <= char <= 'z':
            shift = ord(key[i % key_length]) - ord('a')
            decrypted += chr(((ord(char) - ord('a') - shift + 26) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            shift = ord(key[i % key_length]) - ord('a')
            decrypted += chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))
        else:
            decrypted += char
    
    return decrypted

# Pruebas
print("Prueba César:")
c_text = encrypt_caesar("Hola Mundo", 3)
print("Cifrado:", c_text)
print("Descifrado:", decrypt_caesar(c_text, 3))

print("\nPrueba Afín:")
a_text = encrypt_affine("holañmundo", 5, 8)
print("Cifrado:", a_text)
print("Descifrado:", decrypt_affine(a_text, 5, 8))

print("\nPrueba Vigenère:")
v_text = encrypt_vigenere("WHATANICEDAYTODAY", "CRYPTO")
print("Cifrado:", v_text)
print("Descifrado:", decrypt_vigenere(v_text, "CRYPTO"))
