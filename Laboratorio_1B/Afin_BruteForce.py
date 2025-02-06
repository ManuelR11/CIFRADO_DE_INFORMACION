import re
import string
from collections import Counter
from Frecuencias_Texto import calculate_frequencies
from math import gcd

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zñ]', '', text)
    return text

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_cipher_decifrado(text, a, b):
    alfa = "abcdefghijklmnñopqrstuvwxyz"
    m = len(alfa)
    a_inv = mod_inverse(a, m)
    if a_inv is None:
        return None
    
    texto_decif = ''
    for x in text:
        if x in alfa:
            new_index = (a_inv * (alfa.index(x) - b)) % m
            texto_decif += alfa[new_index]
        else:
            texto_decif += x
    
    return texto_decif

def best_key(text, theoretical_frequencies):
    best_a, best_b = 1, 1
    best_match = float('inf')
    clean_data = clean_text(text)
    m = 27  
    
    for a in range(1, 17):
        if gcd(a, m) != 1:
            continue
        
        for b in range(1, 17):
            decrypted_text = affine_cipher_decifrado(clean_data, a, b)
            if decrypted_text is None:
                continue
            
            observed_frequencies = calculate_frequencies(decrypted_text)
            
            # Comparar las frecuencias con la distribución teórica
            difference = sum(abs(observed_frequencies.get(letter, 0) - theoretical_frequencies.get(letter, 0)) for letter in theoretical_frequencies)
            
            if difference < best_match:
                best_match = difference
                best_a, best_b = a, b
    
    return best_a, best_b

def main():
    file_path = 'Laboratorio_1B/afines.txt'
    text = read_text_file(file_path)
    
    theoretical_frequencies = {
        'a': 12.53, 'b': 1.42, 'c': 4.68, 'd': 5.86, 'e': 13.68, 'f': 0.69, 'g': 1.01, 'h': 0.70,
        'i': 6.25, 'j': 0.44, 'k': 0.02, 'l': 4.97, 'm': 3.15, 'n': 6.71, 'ñ': 0.31, 'o': 8.68,
        'p': 2.51, 'q': 0.88, 'r': 6.87, 's': 7.98, 't': 4.63, 'u': 3.93, 'v': 0.90, 'w': 0.02,
        'x': 0.22, 'y': 0.90, 'z': 0.52
    }
    
    best_a, best_b = best_key(text, theoretical_frequencies)
    final_message = affine_cipher_decifrado(clean_text(text), best_a, best_b)
    
    print(f"Los mejores valores encontrados son: a = {best_a}, b = {best_b}")
    print("Texto descifrado:")
    print(final_message)
    
if __name__ == "__main__":
    main()
