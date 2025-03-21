import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_message(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext), AES.block_size).decode()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(1)
    print("Servidor escuchando en puerto 9999...")

    conn, addr = server.accept()
    print(f"Conexión establecida con {addr}")

    data = conn.recv(32)
    key = data[:16]
    iv = data[16:]

    while True:
        encrypted_data = conn.recv(1024)
        if not encrypted_data:
            break
        decrypted_message = decrypt_message(encrypted_data, key, iv)
        print("Mensaje descifrado:", decrypted_message)

    conn.close()
    print("Conexión cerrada.")

if __name__ == "__main__":
    main()
