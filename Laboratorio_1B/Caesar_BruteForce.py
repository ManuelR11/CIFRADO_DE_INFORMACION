import re
import string
from collections import Counter
from Frecuencias_Texto import calculate_frequencies

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zñ]', '', text)
    return text

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def caesar_cipher_Decifrado(text, shift):
    alfa = "abcdefghijklmnñopqrstuvwxyz"
    texto_decif = ''
    
    for x in text:
        if x in alfa:
            new_index = (alfa.index(x) - shift) % len(alfa)
            texto_decif += alfa[new_index]
        else:
            texto_decif += x
    
    return texto_decif

def best_shift_(text, theoretical_frequencies):
    best_shift = 0
    best_match = float('inf')
    data_clean = clean_text(text)
    
    for shift in range(27):  
        decrypted_text = caesar_cipher_Decifrado(data_clean, shift)
        observed_frequencies = calculate_frequencies(decrypted_text)
        
        difference = sum(abs(observed_frequencies.get(letter, 0) - theoretical_frequencies.get(letter, 0)) for letter in theoretical_frequencies)
        
        if difference < best_match:
            best_match = difference
            best_shift = shift
    
    return best_shift

def main():
    file_path = 'Laboratorio_1B/ceasar.txt'  
    text = read_text_file(file_path)
    
    theoretical_frequencies = {
        'a': 12.53, 'b': 1.42, 'c': 4.68, 'd': 5.86, 'e': 13.68, 'f': 0.69, 'g': 1.01, 'h': 0.70,
        'i': 6.25, 'j': 0.44, 'k': 0.02, 'l': 4.97, 'm': 3.15, 'n': 6.71, 'ñ': 0.31, 'o': 8.68,
        'p': 2.51, 'q': 0.88, 'r': 6.87, 's': 7.98, 't': 4.63, 'u': 3.93, 'v': 0.90, 'w': 0.02,
        'x': 0.22, 'y': 0.90, 'z': 0.52
    }
    
    best_corr = best_shift_(text, theoretical_frequencies)
    final_message = caesar_cipher_Decifrado(clean_text(text), best_corr) 
    
    print(f"El mejor desplazamiento encontrado es: {best_corr}")
    print("Texto descifrado:")
    print(final_message)
    
if __name__ == "__main__":
    main()
