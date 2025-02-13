# Corrupción de Imagen al Aplicar XOR


## Causas del Problema
1. **Modificación de Metadatos**: 
   - Las imágenes contienen estructuras binarias específicas (cabecera, datos comprimidos). XOR puede alterar estos datos críticos y hacer que la imagen sea ilegible.

2. **Conversión Base64**:
   - Codificar en Base64 antes de aplicar XOR puede introducir caracteres de relleno que, si se modifican, impiden la reconstrucción correcta.

3. **Tamaño de la Llave**:
   - Si la llave no es de la misma longitud que los datos, se repite, generando patrones en la imagen cifrada y posibles corrupciones.

4. **Efecto en Datos Binarios**:
   - XOR en bytes de imagen no sigue las mismas reglas que en texto ASCII. Si se aplica incorrectamente, los valores pueden quedar fuera del rango válido.

## Soluciones
- Aplicar XOR directamente sobre los bytes de la imagen sin convertir a Base64.
- Usar una llave del mismo tamaño que la imagen.
- Verificar que la cabecera de la imagen no se altere.
- Considerar cifrados más adecuados como AES en lugar de XOR.

## Imagen Final de XOR
![Imagen Final](https://github.com/ManuelR11/CIFRADO_DE_INFORMACION/blob/6019b978211252fdcb33dabddcac0bbb409d53ec/Laboratorio_2B/imagen_xor.png "Imagen Final")

## Bibliografía
- Schneier, B. (1996). Applied Cryptography. Wiley.
- Ferguson, N., & Schneier, B. (2003). Practical Cryptography. Wiley.
- Menezes, A., van Oorschot, P., & Vanstone, S. (1996). Handbook of Applied Cryptography. CRC Press.

