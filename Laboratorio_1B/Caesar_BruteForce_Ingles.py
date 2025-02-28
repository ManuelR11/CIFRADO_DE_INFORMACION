import re
import string
from collections import Counter
from Frecuencias_Texto import calculate_frequencies

def clean_text(text, for_analysis=False):
    text = text.upper()
    if for_analysis:
        text = re.sub(r'[^A-Z]', '', text)  # Solo letras A-Z para análisis
    else:
        text = re.sub(r'[^A-Z,{}]', '', text)  # Mantener caracteres especiales en la salida
    return text

def caesar_cipher_Decifrado(text, shift):
    alfa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    texto_decif = ''
    
    for x in text:
        if x in alfa:
            new_index = (alfa.index(x) - shift) % len(alfa)
            texto_decif += alfa[new_index]
        else:
            texto_decif += x  # Mantener caracteres especiales
    
    return texto_decif

def best_shift_(text, theoretical_frequencies):
    best_shift = 0
    best_match = float('inf')
    data_clean = clean_text(text, for_analysis=True)
    
    for shift in range(26):  
        decrypted_text = caesar_cipher_Decifrado(data_clean, shift)
        observed_frequencies = calculate_frequencies(decrypted_text)
        observed_frequencies = {k.upper(): v for k, v in observed_frequencies.items()}  # Asegurar mayúsculas
        
        
        difference = sum(abs(observed_frequencies.get(letter, 0) - theoretical_frequencies.get(letter, 0)) for letter in theoretical_frequencies)
        
        if difference < best_match:
            best_match = difference
            best_shift = shift
    
    return best_shift

def main():
    text = "SV OHU JVUZLNBPKV, OHU LUJVUAYHKV BUH MSHN WHYH LS ZPNBPLUAL KLZHMPV MSHN{JYFWAV_HUHSFZPZ}"
    
    theoretical_frequencies = {
        'A': 8.17, 'B': 1.49, 'C': 2.78, 'D': 4.25, 'E': 12.70, 'F': 2.23, 'G': 2.02, 'H': 6.09,
        'I': 6.97, 'J': 0.15, 'K': 0.77, 'L': 4.03, 'M': 2.41, 'N': 6.75, 'O': 7.51, 'P': 1.93,
        'Q': 0.10, 'R': 5.99, 'S': 6.33, 'T': 9.06, 'U': 2.76, 'V': 0.98, 'W': 2.36, 'X': 0.15,
        'Y': 1.97, 'Z': 0.07
    }
    
    best_corr = best_shift_(text, theoretical_frequencies)
    final_message = caesar_cipher_Decifrado(clean_text(text), best_corr) 
    
    print(f"El mejor desplazamiento encontrado es: {best_corr}")
    print("Texto descifrado:")
    print(final_message)
    
if __name__ == "__main__":
    main()