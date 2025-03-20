import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

def encrypt_file(file_path, key, iv):
    with open(file_path, 'rb') as f:
        data = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(data, AES.block_size))
    with open(file_path, 'wb') as f:
        f.write(encrypted)
    print(f"Archivo cifrado: {file_path}")

def main():
    key = get_random_bytes(16)
    iv = get_random_bytes(16)

    base_folder = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(base_folder, 'key.bin'), 'wb') as f:
        f.write(key + iv)


    for filename in os.listdir(base_folder):
        if filename.endswith('.txt'):
            encrypt_file(os.path.join(base_folder, filename), key, iv)

    print("Todos los archivos de texto han sido cifrados en:", base_folder)

if __name__ == "__main__":
    main()
