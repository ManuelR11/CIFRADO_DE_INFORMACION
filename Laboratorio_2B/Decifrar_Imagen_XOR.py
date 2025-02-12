import base64
from Script_Criptografia import ascii_to_binary, binary_to_ascii, xor_binary, extend_key

def decode_xor_image(image_path, key):
    # Leer la imagen y convertirla a Base64
    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()
        image_base64 = base64.b64encode(image_bytes).decode('utf-8')
    
    # Convertir la base64 a binario
    binary_image = ' '.join(format(byte, '08b') for byte in base64.b64decode(image_base64))
    
    # Extender la llave al tamaño del binario de la imagen
    extended_key = extend_key(key, len(image_bytes))
    binary_key = ' '.join(format(ord(char), '08b') for char in extended_key)
    
    # Aplicar XOR entre la imagen en binario y la llave
    decrypted_binary = xor_binary(binary_image, binary_key)
    
    # Convertir el binario resultante de vuelta a bytes
    decrypted_bytes = bytes(int(b, 2) for b in decrypted_binary.split())
    
    # Guardar la imagen descifrada
    with open("imagen_descifrada.png", "wb") as output_file:
        output_file.write(decrypted_bytes)
    
    print("Imagen descifrada y guardada como 'imagen_descifrada.png'")

# Parámetros
image_path = "Laboratorio_2B\imagen_xor.png"  # Ruta de la imagen cifrada
key = "cifrados_2025"  # Llave para el XOR

decode_xor_image(image_path, key)
