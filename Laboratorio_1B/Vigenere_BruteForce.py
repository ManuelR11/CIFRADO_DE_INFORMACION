import re
import string
from collections import Counter
from itertools import product
from Frecuencias_Texto import calculate_frequencies

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zñ]', '', text)
    return text

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def vigenere_cipher_decifrado(text, key):
    alfa = "abcdefghijklmnñopqrstuvwxyz"
    m = len(alfa)
    key = key.lower()
    key_repeated = (key * ((len(text) // len(key)) + 1))[:len(text)]
    
    decrypted_text = ''
    for x, k in zip(text, key_repeated):
        if x in alfa and k in alfa:
            new_index = (alfa.index(x) - alfa.index(k)) % m
            decrypted_text += alfa[new_index]
        else:
            decrypted_text += x
    
    return decrypted_text

def generate_key_variations(base, length, alphabet):
    if length <= len(base):
        return [base[:length]]
    
    extra_length = length - len(base)
    suffixes = product(alphabet, repeat=extra_length)
    return [base + ''.join(suffix) for suffix in suffixes]

def find_best_vigenere_key(text, theoretical_frequencies):
    alfa = "abcdefghijklmnñopqrstuvwxyz"
    clean_data = clean_text(text)
    best_key = "pa"
    best_match = float('inf')
    
    for key_length in range(1, 7): 
        key_variations = generate_key_variations("pa", key_length, alfa)
        
        for test_key in key_variations:
            decrypted_text = vigenere_cipher_decifrado(clean_data, test_key)
            observed_frequencies = calculate_frequencies(decrypted_text)
            

            difference = sum(abs(observed_frequencies.get(letter, 0) - theoretical_frequencies.get(letter, 0)) for letter in theoretical_frequencies)
            
            print(f"Clave probada: {test_key}, Diferencia - frecuencia: {difference:.2f}")
            
            if difference < best_match:
                best_match = difference
                best_key = test_key
    
    return best_key

def main():
    file_path = 'Laboratorio_1B/vigenere.txt'
    text = read_text_file(file_path)
    
    theoretical_frequencies = {
        'a': 12.53, 'b': 1.42, 'c': 4.68, 'd': 5.86, 'e': 13.68, 'f': 0.69, 'g': 1.01, 'h': 0.70,
        'i': 6.25, 'j': 0.44, 'k': 0.02, 'l': 4.97, 'm': 3.15, 'n': 6.71, 'ñ': 0.31, 'o': 8.68,
        'p': 2.51, 'q': 0.88, 'r': 6.87, 's': 7.98, 't': 4.63, 'u': 3.93, 'v': 0.90, 'w': 0.02,
        'x': 0.22, 'y': 0.90, 'z': 0.52
    }
    
    best_key = find_best_vigenere_key(text, theoretical_frequencies)
    final_message = vigenere_cipher_decifrado(clean_text(text), best_key)
    
    print(f"\nLa mejor clave que se encontro es: {best_key}")
    print("Texto descifrado:")
    print(final_message)
    
if __name__ == "__main__":
    main()
