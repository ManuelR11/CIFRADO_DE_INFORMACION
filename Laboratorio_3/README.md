
# Laboratorio 3 - Cifrados Simetricos

### Objetivos
- Implementar AES con modos ECB y CBC en un entorno real.

- Aplicar ChaCha20 como alternativa de cifrado de flujo.

- Analizar los riesgos de los modos ECB y CBC en imágenes.

- Implementar cifrados en un protocolo de comunicación con Wireshark.

- Explorar cómo se rompe un cifrado mal implementado.
---

## **Ejercicio 1: Rompiendo ECB en Imágenes**

### Descripción:
Se utilizó una imagen en escala de grises (tux.ppm) para demostrar las diferencias entre cifrar con **AES en modo ECB** y **AES en modo CBC**. Ambas imágenes cifradas fueron generadas para visualizar el comportamiento de los modos.

### Resultados:
- Imagen cifrada con ECB: `tux_ecb.bmp`
- Imagen cifrada con CBC: `tux_cbc.bmp`


**• ¿Por qué el cifrado ECB revela los patrones de la imagen?**  
Porque **ECB cifra cada bloque de datos de manera independiente**, por lo que los bloques idénticos de la imagen original generan bloques cifrados iguales. Esto hace que los patrones y contornos de la imagen original se mantengan visibles incluso después del cifrado.

**• ¿Cómo cambia la apariencia con CBC?**  
Con **CBC**, cada bloque es cifrado después de mezclarlo con el bloque cifrado anterior (y el IV en el primer caso). Esto destruye los patrones repetitivos, haciendo que la imagen cifrada se vea aleatoria y sin contornos visibles.

**• ¿Qué tan seguro es usar ECB para cifrar datos estructurados?**  
**Muy inseguro**. ECB no debe usarse para imágenes, bases de datos o cualquier dato estructurado porque mantiene patrones y puede ser vulnerable a análisis visuales o de bloques repetidos.

---
## **Ejercicio 2: Capturando Cifrado en Red con Wireshark**

### Descripción:
Se implementó un sistema cliente-servidor con **sockets TCP**, donde los mensajes se cifran con **AES-CBC** antes de enviarlos a través de la red. Luego, se capturó y analizó el tráfico con **Wireshark** para evaluar la seguridad de la transmisión.

---

### **Cliente:**
El cliente cifra mensajes con AES-CBC y los envía al servidor.

```python
def encrypt_message(message, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(pad(message.encode(), AES.block_size))
```

- **key** y **IV** se generan aleatoriamente.
- El cliente también envía la **clave e IV** al servidor (esto es solo para propósitos de demostración, no es seguro en la vida real).

**Imagen de la consola del cliente:**  
![Cliente](https://github.com/ManuelR11/CIFRADO_DE_INFORMACION/blob/f9a1e240206cfa659b5066167299bd9680d6c132/Laboratorio_3/Wireshark/Cliente.png)

---

### **Servidor:**
El servidor recibe los datos cifrados, y usa la clave y IV previamente recibidos para descifrar.

```python
def decrypt_message(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext), AES.block_size).decode()
```

**Imagen de la consola del servidor:**  
![Servidor](https://github.com/ManuelR11/CIFRADO_DE_INFORMACION/blob/f9a1e240206cfa659b5066167299bd9680d6c132/Laboratorio_3/Wireshark/Server.png)

---

### **Imagen Wireshark**

Se capturó la comunicación y se observó que los mensajes viajan **encriptados**.

**Paquete con mensaje cifrado en Wireshark:**  
![Mensaje Cifrado](https://github.com/ManuelR11/CIFRADO_DE_INFORMACION/blob/f9a1e240206cfa659b5066167299bd9680d6c132/Laboratorio_3/Wireshark/Mensaje_Cifrado.png)

Se puede ver claramente cómo **el contenido del mensaje es ilegible** y aparece como bloques en hexadecimal (datos cifrados con AES).

---

### **Respuestas:**

**• ¿Se puede identificar que los mensajes están cifrados con AES-CBC?**  
No directamente. Wireshark solo muestra que los datos están cifrados (no hay texto plano legible), pero **no puede determinar que sea AES-CBC** sin información adicional. Solo verás datos binarios en crudo.  
Sin embargo, un atacante que analice la longitud fija de los bloques y patrones en las comunicaciones podría sospechar que es un cifrado por bloques como AES.

---

**• ¿Cómo podríamos proteger más esta comunicación?**  
- **Intercambiar la clave de forma segura**, por ejemplo, usando **Diffie-Hellman** o un protocolo como **TLS** para evitar enviar la clave e IV en claro.  
- Utilizar **certificados y autenticación mutua** para asegurar la identidad de cliente y servidor.  
- Agregar un **HMAC** o autenticación adicional para verificar la integridad y evitar ataques de manipulación de mensajes (como ataques de padding oracle).  
- **Evitar reusar IVs** en múltiples mensajes con la misma clave.

---

## **Ejercicio 3: Implementando un Cifrado de Flujo con ChaCha20**

### Descripción:
Se implementó **ChaCha20**, un algoritmo de cifrado de flujo moderno, y se comparó su rendimiento contra **AES-CBC**.

### Resultados de ejecución:

```
Mensaje original: Este es un mensaje secreto usando ChaCha20
Clave: 2cdbc83340cedf00594f2fe31efccc62415cd445e9b9ab51e5ff38b4b538b43b
Nonce: 69d4ee4bb75778e76a9a49b3
Cifrado (hex): 755f4e7fc63c73d643f04d0b95d9cc749d384c27dcc8ff6cbab4571e7dc2e68f0d642a536614860c61f7
Descifrado: Este es un mensaje secreto usando ChaCha20
```

### Benchmark:

```
Benchmark ChaCha20:
Tiempo: 0.001566 s | Memoria: 143.52 KB

Benchmark AES-CBC:
Tiempo: 0.000556 s | Memoria: 138.89 KB
```


**• ¿Analizar qué cifrado es más rápido ChaCha20 o AES?**  
En esta prueba, **AES-CBC fue ligeramente más rápido** que ChaCha20 en tiempo, aunque esto puede variar según la implementación o la arquitectura. Sin embargo, **ChaCha20 suele ser más rápido que AES en dispositivos sin aceleración de hardware** (como microcontroladores o entornos embebidos).

**• ¿En qué casos debería usarse en vez de AES?**  
ChaCha20 es ideal cuando:  
- Se trabaja en **software puro** (sin soporte de AES por hardware).  
- En **aplicaciones móviles** o sistemas embebidos.  
- Cuando se necesita **un cifrado de flujo moderno y seguro** como alternativa a RC4.

---

## **Ejercicio 4: Implementación de un Ransomware Simulado**

### Descripción:
Se creó un ransomware simulado que cifra archivos de texto dentro de una carpeta utilizando **AES-CBC** y genera una clave almacenada localmente en `key.bin`. Luego se implementó un script de desencriptado que recupera los archivos originales.

### Resultado (archivo cifrado):
```
archivo1.txt = ���|�u~*p��Z��ӕF�7�����0�m�Ob1��gwK{X�������J~A��<�^����:�����9��ޛ�>�%Jo���D���[  
```

### Resultado (archivo descifrado):
```
archivo1.txt = Este es el archivo 1 para la prueba de ransomware, con el fin de ver que pasa jajajajaja
```


**• ¿Cómo podríamos evitar ataques de ransomware?**  
- Manteniendo **backups regulares** fuera de línea.  
- Utilizando **antivirus y EDRs** que detecten comportamientos sospechosos.  
- No descargar archivos ni abrir enlaces de fuentes no confiables.  
- Tener una buena **higiene de seguridad** (segmentación de red, privilegios mínimos, etc.).

**• ¿Qué tan importante es almacenar claves de manera segura?**  
Es **crítico**. En este ejercicio la clave se guarda localmente (algo que un ransomware real no haría). En un ataque real, **la clave se envía al atacante** para que el usuario no pueda recuperar sus archivos sin pagar. **Nunca debes almacenar claves en el mismo lugar donde están los datos cifrados.**

