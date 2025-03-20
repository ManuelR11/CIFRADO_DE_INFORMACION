import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_file(file_path, key, iv):
    with open(file_path, 'rb') as f:
        data = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(data), AES.block_size)
    with open(file_path, 'wb') as f:
        f.write(decrypted)
    print(f"Archivo descifrado: {file_path}")

def main():
    base_folder = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(base_folder, 'key.bin'), 'rb') as f:
        content = f.read()
        key = content[:16]
        iv = content[16:]

    for filename in os.listdir(base_folder):
        if filename.endswith('.txt'):
            decrypt_file(os.path.join(base_folder, filename), key, iv)

    print("Archivos descifrados correctamente en:", base_folder)

if __name__ == "__main__":
    main()
