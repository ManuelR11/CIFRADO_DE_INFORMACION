'''
Manuel Rodas 21509

Universidad del Valle de Guatemala

CIFRADO DE INFORMACIÓN - SECCIÓN - 10 - 2025 - 1

'''

import random
import string

def ascii_to_binary(text):
    """
    Convierte un texto ASCII a su representación binaria.
    :param text: Texto en formato ASCII
    :return: Cadena de texto binaria
    """
    binary_result = ' '.join(format(ord(char), '08b') for char in text)
    return binary_result

def base64_to_binary(base64_text):
    """
    Convierte un texto codificado en Base64 a su representación binaria.
    :param base64_text: Texto en formato Base64
    :return: Cadena de texto binaria
    """
    base64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    padding = base64_text.count('=')
    base64_text = base64_text.rstrip('=')

    binary_result = ''
    for char in base64_text:
        index = base64_alphabet.index(char)
        binary_result += format(index, '06b')

    if padding:
        binary_result = binary_result[:-padding * 2]

    return ' '.join(binary_result[i:i+8] for i in range(0, len(binary_result), 8))

def binary_to_base64(binary_text):
    """
    Convierte un texto binario a su representación en Base64.
    :param binary_text: Cadena de texto binaria (separada por espacios o sin espacios)
    :return: Texto codificado en Base64
    """
    base64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    binary_text = binary_text.replace(' ', '')

    while len(binary_text) % 6 != 0:
        binary_text += '0'

    base64_result = ''
    for i in range(0, len(binary_text), 6):
        segment = binary_text[i:i+6]
        base64_result += base64_alphabet[int(segment, 2)]

    padding = (4 - len(base64_result) % 4) % 4
    base64_result += '=' * padding

    return base64_result

def binary_to_ascii(binary_text):
    """
    Convierte un texto binario a su representación ASCII.
    :param binary_text: Cadena de texto binaria (separada por espacios o sin espacios)
    :return: Texto en formato ASCII
    """
    binary_values = binary_text.split()
    ascii_result = ''.join(chr(int(b, 2)) for b in binary_values)
    return ascii_result

def base64_to_ascii(base64_text):
    """
    Convierte un texto Base64 a su representación ASCII pasando por binario.
    :param base64_text: Texto en formato Base64
    :return: Texto en formato ASCII
    """
    binary_text = base64_to_binary(base64_text)
    ascii_result = binary_to_ascii(binary_text)
    return ascii_result

def xor_binary(binary_text1, binary_text2):
    """
    Aplica la operación XOR entre dos cadenas binarias de igual longitud.
    :param binary_text1: Primera cadena binaria (separada por espacios)
    :param binary_text2: Segunda cadena binaria (separada por espacios)
    :return: Resultado de la operación XOR en formato binario
    """
    binary_values1 = binary_text1.split()
    binary_values2 = binary_text2.split()

    if len(binary_values1) != len(binary_values2):
        raise ValueError("Las cadenas binarias deben tener la misma longitud.")

    xor_result = [format(int(b1, 2) ^ int(b2, 2), '08b') for b1, b2 in zip(binary_values1, binary_values2)]
    return ' '.join(xor_result)


def generate_key(length):
    """
    Genera una llave de tamaño fijo compuesta de caracteres ASCII.
    :param length: Longitud de la llave a generar.
    :return: Cadena de texto ASCII representando la llave.
    """
    key = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
    return key

def extend_key(key, text_length):
    """
    Extiende una llave fija repitiéndola hasta alcanzar la longitud del texto.
    :param key: Llave fija en formato ASCII.
    :param text_length: Longitud del texto a cifrar.
    :return: Llave extendida al tamaño del texto.
    """
    return (key * (text_length // len(key)) + key[:text_length % len(key)])

def cypher_fixed(text, key):
    """
    Genera un cifrado en ASCII utilizando una llave fija que se repite hasta alcanzar el tamaño del texto.
    :param text: Texto original en formato ASCII.
    :param key: Llave fija en formato ASCII.
    :return: Texto cifrado en formato ASCII.
    """
    extended_key = extend_key(key, len(text))

    binary_text = ascii_to_binary(text)
    binary_key = ascii_to_binary(extended_key)


    binary_cypher = xor_binary(binary_text, binary_key)


    ascii_cypher = binary_to_ascii(binary_cypher)

    return ascii_cypher

def decrypt_cypher_fixed(cypher_text, key):
    """
    Descifra un texto cifrado en ASCII utilizando una llave mediante la operación XOR.
    :param cypher_text: Texto cifrado en formato ASCII.
    :param key: Llave fija en formato ASCII.
    :return: Texto descifrado en formato ASCII.
    """

    extended_key = extend_key(key, len(cypher_text))


    binary_cypher = ascii_to_binary(cypher_text)
    binary_key = ascii_to_binary(extended_key)


    binary_text = xor_binary(binary_cypher, binary_key)


    original_text = binary_to_ascii(binary_text)

    return original_text



def dynamic_cypher(text, key):
    """
    Genera un cifrado en ASCII utilizando una llave mediante la operación XOR.
    Si la llave no es del mismo tamaño que el texto en binario, se rellena con ceros a la izquierda.
    :param text: Texto original en formato ASCII.
    :param key: Llave en formato ASCII (puede ser de tamaño distinto al texto).
    :return: Texto cifrado en formato ASCII.
    """

    binary_text = ascii_to_binary(text).replace(" ", "")
    binary_key = ascii_to_binary(key).replace(" ", "")


    if len(binary_key) < len(binary_text):
        binary_key = binary_key.zfill(len(binary_text))
    elif len(binary_key) > len(binary_text):
        binary_text = binary_text.zfill(len(binary_key))


    binary_text_segments = [binary_text[i:i+8] for i in range(0, len(binary_text), 8)]
    binary_key_segments = [binary_key[i:i+8] for i in range(0, len(binary_key), 8)]


    binary_cypher = xor_binary(" ".join(binary_text_segments), " ".join(binary_key_segments))


    ascii_cypher = binary_to_ascii(binary_cypher)

    return ascii_cypher

def dynamic_decrypt_cypher(cypher_text, key):
    """
    Descifra un texto cifrado en ASCII utilizando una llave mediante la operación XOR.
    Si la llave no es del mismo tamaño que el texto cifrado en binario, se rellena con ceros a la izquierda.
    :param cypher_text: Texto cifrado en formato ASCII.
    :param key: Llave en formato ASCII (puede ser de tamaño distinto al texto cifrado).
    :return: Texto descifrado en formato ASCII.
    """

    binary_cypher = ascii_to_binary(cypher_text).replace(" ", "")
    binary_key = ascii_to_binary(key).replace(" ", "")


    if len(binary_key) < len(binary_cypher):
        binary_key = binary_key.zfill(len(binary_cypher))
    elif len(binary_key) > len(binary_cypher):
        binary_cypher = binary_cypher.zfill(len(binary_key))


    binary_cypher_segments = [binary_cypher[i:i+8] for i in range(0, len(binary_cypher), 8)]
    binary_key_segments = [binary_key[i:i+8] for i in range(0, len(binary_key), 8)]


    binary_text = xor_binary(" ".join(binary_cypher_segments), " ".join(binary_key_segments))


    original_text = binary_to_ascii(binary_text)

    return original_text




if __name__ == "__main__":
    # --------- ASCII a BINARIO ------------
    ascii_text = "Hola"
    binary_from_ascii = ascii_to_binary(ascii_text)
    print(f"ASCII a Binario: {binary_from_ascii}")

    # --------- BASE64 a BINARIO ------------
    base64_text = "SG9sYQ=="
    binary_from_base64 = base64_to_binary(base64_text)
    print(f"Base64 a Binario: {binary_from_base64}")

    # --------- BINARIO a BASE64 ------------
    binary_text = "01001000 01101111 01101100 01100001"
    base64_from_binary = binary_to_base64(binary_text)
    print(f"Binario a Base64: {base64_from_binary}")

    # --------- BINARIO a ASCII ------------
    binary_text = "01001000 01101111 01101100 01100001"
    ascii_from_binary = binary_to_ascii(binary_text)
    print(f"Binario a ASCII: {ascii_from_binary}")

    # ---------- BASE64 a ASCII ------------
    ascii_from_base64 = base64_to_ascii(base64_text)
    print(f"Base64 a ASCII: {ascii_from_base64}")

    #  ---------- XOR entre dos cadenas binarias ------------
    binary1 = "01001000 01101111 01101100 01100001"
    binary2 = "00001111 00001111 00001111 00001111"
    xor_result = xor_binary(binary1, binary2)
    print(f"XOR de binarios: {xor_result}")

    # ----------- Generar llave dinámica ------------
    key_length = 16
    dynamic_key = generate_key(key_length)
    print(f"Llave dinámica generada: {dynamic_key}")

    original_text = "Hola mundo"
    


    cypher = dynamic_cypher(original_text, dynamic_key)


    decrypted_text = dynamic_decrypt_cypher(cypher, dynamic_key)

    print(f"Texto original: {original_text}")
    print(f"Llave: {dynamic_key}")
    print(f"Texto cifrado (cypher): {cypher}")
    print(f"Texto descifrado: {decrypted_text}")



    fixed_key = "perro"


    cypher_fixed_key = cypher_fixed(original_text, fixed_key)


    decrypted_text_fixed_key = decrypt_cypher_fixed(cypher_fixed_key, fixed_key)

    print(f"Texto original: {original_text}")
    print(f"Llave fija: {fixed_key}")
    print(f"Texto cifrado (cypher): {cypher_fixed_key}")
    print(f"Texto descifrado: {decrypted_text_fixed_key}")