# README - Cifrado con Keystream y XOR

## Descripción

### 1. Generación de Keystream
Escriban una función en el lenguaje de programación que prefieran para generar un keystream pseudoaleatorio basado en:

- Un generador de números pseudoaleatorios (PRNG) básico.
- Una clave (seed/nonce) para inicializar el PRNG.
- Asegúrate de que el keystream tenga al menos la misma longitud que el mensaje a cifrar.

### 2. Cifrado
Implementa una función que tome un mensaje en texto plano y lo cifre utilizando la operación XOR con el keystream generado.

### 3. Descifrado
Implementa una función que tome el mensaje cifrado y lo descifre utilizando la misma operación XOR con el keystream. Asegúrate de que el descifrado reproduzca exactamente el mensaje original.

## Archivos
- `Stream_Cipher.py`: Contiene la implementación del keystream, cifrado y descifrado.
- `tests.py`: Archivo de pruebas unitarias para validar la funcionalidad.

## Cómo ejecutar el código
1. Asegúrate de tener Python 3 instalado en tu sistema.
2. Clona este repositorio o descarga los archivos.
3. Abre una terminal y navega hasta la carpeta del proyecto.
4. Ejecuta el script con el siguiente comando:

   ```bash
   python3 Stream_Cipher.py
   ```

## Ejemplo de salida del código
```
manuelrodasgordillo@MacBook-Pro-de-Manuel CIFRADO_DE_INFORMACION % /usr/bin/python3 /Users/manuelrodasgordillo
/Documents/CODE11/Cifrado_Informacion/CIFRADO_DE_INFORMACION/Ejercicio_Stream_Cipher/Stream_Cipher.py
Texto plano: Hola, esto es un mensaje de prueba
Keystream: b'9\x0c\x8c}rG4,\xd8\x10\x0f/ow\re\xd6p\xe5\x8e\x03Q\xd8\xae\x8eOn\xac4/\xc21\xb7\xb0'
Texto cifrado: b'qc\xe0\x1c^gQ_\xac\x7f/J\x1cWx\x0b\xf6\x1d\x80\xe0p0\xb2\xcb\xae+\x0b\x8cD]\xb7T\xd5\xd1'
Texto descifrado: Hola, esto es un mensaje de prueba
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

## Preguntas y respuestas
### ¿Qué sucede cuando cambias la clave utilizada para generar el keystream?
Cuando cambias la clave (original) que se utiliza para generar el keystream, se obtiene una secuencia de bytes completamente diferente. Por lo que esto significa que el mensaje cifrado será diferente incluso si el texto original es el mismo.

### ¿Qué riesgos de seguridad existen si reutilizas el mismo keystream para cifrar dos mensajes diferentes?
Si el mismo keystream se reutiliza para cifrar dos mensajes distintos,cualquier persona puede calcular la XOR de los dos ciphertexts y poder asi revelar información parcial sobre los textos originales. Este problema de seguridad es conocido en cifrados de flujo débiles.

### ¿Cómo afecta la longitud del keystream a la seguridad del cifrado?
Si el keystream es más corto que el mensaje, se repetirá, lo que puede introducir patrones predecibles y hace más fácil romper el cifrado. En un sistema seguro, el keystream debe ser al menos tan largo como el mensaje.

### ¿Qué consideraciones debes tener al generar un keystream en un entorno real?
- Usar un generador criptográficamente seguro en lugar de `random.seed()`, como `secrets.token_bytes()`.
- No reutilizar el mismo keystream para múltiples mensajes.
- Asegurar que la semilla utilizada sea verdaderamente aleatoria y única para cada cifrado.
- En aplicaciones críticas, considerar el uso de cifrados autenticados como AES-GCM en lugar de simples XOR con keystreams pseudoaleatorios.

Manuel Rodas 21509

