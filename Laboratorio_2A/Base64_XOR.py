from Script_Criptografia import (
    ascii_to_binary, binary_to_ascii,
    binary_to_base64, base64_to_binary,
    base64_to_ascii, xor_binary,
    extend_key, ascii_to_binary
)

def main():
    # Ejercicio 1: Convertir cadena de caracteres a bits
    print("Ejercicio 1: Convertir cadena de caracteres a bits")
    print("--------------------------------------------------")
    texto1 = "¡Hola, mundo!"
    texto2 = "1234@#$%"
    binario1 = ascii_to_binary(texto1)
    binario2 = ascii_to_binary(texto2)
    print(f"Texto: {texto1} -> Binario: {binario1}")
    print(f"Texto: {texto2} -> Binario: {binario2}")
    print()

    # Ejercicio 2: Convertir una cadena de bytes a caracteres
    print("Ejercicio 2: Convertir una cadena de bytes a caracteres")
    print("-------------------------------------------------------")
    ascii1 = binary_to_ascii(binario1)
    ascii2 = binary_to_ascii(binario2)
    print(f"Binario: {binario1} -> Texto: {ascii1}")
    print(f"Binario: {binario2} -> Texto: {ascii2}")
    print()

    # Ejercicio 3: Convertir cadena de caracteres a Base64 manualmente
    print("Ejercicio 3: Convertir cadena de caracteres a Base64 manualmente")
    print("-----------------------------------------------------------------")
    base64_1 = binary_to_base64(binario1)
    base64_2 = binary_to_base64(binario2)
    print(f"Texto: {texto1} -> Base64: {base64_1}")
    print(f"Texto: {texto2} -> Base64: {base64_2}")
    print()

    # Ejercicio 4: Convertir una cadena de Base64 a su texto correspondiente manualmente
    print("Ejercicio 4: Convertir una cadena de Base64 a su texto correspondiente manualmente")
    print("------------------------------------------------------------------------------------")
    binario_desde_b64_1 = base64_to_binary(base64_1)
    binario_desde_b64_2 = base64_to_binary(base64_2)
    texto_desde_b64_1 = binary_to_ascii(binario_desde_b64_1)
    texto_desde_b64_2 = binary_to_ascii(binario_desde_b64_2)
    print(f"Base64: {base64_1} -> Texto: {texto_desde_b64_1}")
    print(f"Base64: {base64_2} -> Texto: {texto_desde_b64_2}")
    print()

    # Ejercicio 5: Operación XOR entre dos cadenas de texto
    print("Ejercicio 5: Operación XOR entre dos cadenas de texto")
    print("-----------------------------------------------------")
    texto_xor1 = "clave123!"
    texto_xor2 = "seguraXYZ"
    
    print("\n--- Proceso XOR Paso a Paso ---")
    print(f"Texto 1: {texto_xor1}")
    print(f"Texto 2: {texto_xor2}")
    
    binario_xor1 = ascii_to_binary(texto_xor1)
    binario_xor2 = ascii_to_binary(extend_key(texto_xor2, len(texto_xor1)))
    
    print(f"Texto 1 en Binario: {binario_xor1}")
    print(f"Texto 2 en Binario (extendido si es necesario): {binario_xor2}")
    
    resultado_xor = xor_binary(binario_xor1, binario_xor2)
    print(f"Resultado XOR en Binario: {resultado_xor}")
    
    resultado_ascii = binary_to_ascii(resultado_xor)
    print(f"Resultado XOR en ASCII: {resultado_ascii}")
    print()

if __name__ == "__main__":
    main()
