
# Ejercicio Block Cipher

Este proyecto implementa **cifrado y descifrado** usando los algoritmos de bloque:
- **DES (ECB)**
- **3DES (CBC)**
- **AES (CBC y ECB, aplicados a texto e imágenes)**

Cada algoritmo tiene su propio archivo de código y pruebas unitarias para verificar su funcionamiento.

---

## **Estructura del Proyecto**
```
Ejercicio_Block_Cipher/
│── 3DES/
│   ├── _3DES.py     <- Implementación de cifrado y descifrado 3DES (modo CBC)
│   ├── 3des.txt     <- Archivo de prueba opcional para cifrado de texto
│
│── AES_CBC_ECB/
│   ├── AES.py       <- Implementación de cifrado y descifrado AES en CBC y ECB
│   ├── pic.png      <- Imagen de prueba para cifrado con AES
│
│── DES/
│   ├── DES.py       <- Implementación de cifrado y descifrado DES (modo ECB)
│   ├── des.txt      <- Archivo de prueba opcional para cifrado de texto
│
│── test_crypto.py   <- Pruebas unitarias para verificar que los cifrados y descifrados funcionan correctamente
│── README.md        
```

---

## **Descripción de Archivos**
| Archivo | Descripción |
|---------|------------|
| `DES.py` | Implementa cifrado y descifrado DES en modo ECB. |
| `_3DES.py` | Implementa cifrado y descifrado 3DES en modo CBC. |
| `AES.py` | Implementa cifrado y descifrado AES en modo CBC y ECB para texto e imágenes. |
| `des.txt` y `3des.txt` | Archivos de prueba opcionales para cifrar texto en DES y 3DES. |
| `pic.png` | Imagen de prueba que se cifra y descifra con AES. |
| `test_crypto.py` | Contiene pruebas unitarias para validar que el cifrado y descifrado funcionan correctamente. |

---

## **Requisitos**
Este proyecto utiliza **Python 3** y la librería `pycryptodome`. Instálala con:

```bash
pip install pycryptodome
```

---

## **Cómo Usar**
### **1. Ejecutar los cifrados y descifrados manualmente**
Ejecuta los archivos para probar el cifrado y descifrado:

#### **DES**
```bash
python3 DES/DES.py
```

#### **3DES**
```bash
python3 _3DES/_3DES.py
```

#### **AES (Texto e Imagen)**
```bash
python3 AES_CBC_ECB/AES.py
```

---

### **2. Ejecutar pruebas unitarias**
Para verificar que todo funciona correctamente, usa:

```bash
python3 -m unittest test_crypto.py
```

Esto ejecutará las pruebas de:
✅ **DES (ECB)**  
✅ **3DES (CBC)**  
✅ **AES (CBC y ECB, en texto e imágenes)**  

Si todo está bien, verás:

```
....
----------------------------------------------------------------------
Ran 4 tests in 0.XXXs

OK
```

---


✅ **Las claves y IVs se generan aleatoriamente en cada ejecución**, por lo que los resultados cifrados varían cada vez.

---

## **Explicación de los Algoritmos**
### **DES (Data Encryption Standard)**
- Algoritmo de cifrado simétrico de 56 bits.
- Se usa en modo **ECB** (Electronic Codebook).
- Cada bloque de texto es cifrado de manera independiente.

### **3DES (Triple DES)**
- Variación más segura de DES.
- Usa **tres claves de 56 bits** y opera en modo **CBC** (Cipher Block Chaining).
- Requiere un **Vector de Inicialización (IV)**.

### **AES (Advanced Encryption Standard)**
- Algoritmo más seguro con claves de **128, 192 o 256 bits**.
- Implementado en **modo ECB (Electronic Codebook) y CBC (Cipher Block Chaining)**.
- **ECB** cifra cada bloque de manera independiente (menos seguro).
- **CBC** encadena los bloques usando un **IV aleatorio** (más seguro).

---
