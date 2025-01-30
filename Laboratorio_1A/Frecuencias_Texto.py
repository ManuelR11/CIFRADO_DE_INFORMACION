import matplotlib.pyplot as plt
from collections import Counter

def calculate_frequencies(text):
    text = text.lower()
    total_chars = len(text)
    letter_counts = Counter(c for c in text if c.isalpha() or c == 'ñ')
    
    frequencies = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
    frequencies['ñ'] = 0
    for letter, count in letter_counts.items():
        frequencies[letter] = (count / total_chars) * 100
    
    return frequencies

def plot_frequencies(frequencies, theoretical_frequencies):
    letters = sorted(frequencies.keys())
    observed = [frequencies[l] for l in letters]
    theoretical = [theoretical_frequencies[l] for l in letters]
    
    plt.figure(figsize=(12, 6))
    plt.bar(letters, observed, alpha=0.6, label='Frecuencia Observada')
    plt.plot(letters, theoretical, color='red', marker='o', linestyle='dashed', label='Frecuencia Teórica')
    plt.xlabel("Letra")
    plt.ylabel("Frecuencia relativa (%)")
    plt.title("Comparación de frecuencias de letras en español")
    plt.legend()
    plt.show()

def compare_frequencies(frequencies, theoretical_frequencies):
    sorted_observed = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    sorted_theoretical = sorted(theoretical_frequencies.items(), key=lambda x: x[1], reverse=True)
    
    print("Orden de letras según frecuencia observada:")
    for letter, freq in sorted_observed:
        print(f"{letter}: {freq:.2f}%")
    
    print("\nOrden de letras según frecuencia teórica:")
    for letter, freq in sorted_theoretical:
        print(f"{letter}: {freq:.2f}%")
    
    mismatches = [letter for (letter, _), (t_letter, _) in zip(sorted_observed, sorted_theoretical) if letter != t_letter]
    print("\nLetras que no coinciden en el orden esperado:")
    print(mismatches if mismatches else "Todas las letras coinciden en el orden esperado.")

def main():
    theoretical_frequencies = {
        'a': 12.53, 'b': 1.42, 'c': 4.68, 'd': 5.86, 'e': 13.68, 'f': 0.69, 'g': 1.01, 'h': 0.70,
        'i': 6.25, 'j': 0.44, 'k': 0.02, 'l': 4.97, 'm': 3.15, 'n': 6.71, 'ñ': 0.31, 'o': 8.68,
        'p': 2.51, 'q': 0.88, 'r': 6.87, 's': 7.98, 't': 4.63, 'u': 3.93, 'v': 0.90, 'w': 0.02,
        'x': 0.22, 'y': 0.90, 'z': 0.52
    }
    
    text = "este es un texto de prueba para analizar la frecuencia de letras en el cifrado"
    frequencies = calculate_frequencies(text)
    plot_frequencies(frequencies, theoretical_frequencies)
    compare_frequencies(frequencies, theoretical_frequencies)

if __name__ == "__main__":
    main()
