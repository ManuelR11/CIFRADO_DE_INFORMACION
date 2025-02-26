import os
import random
import unittest

# ----------- generar un keystream pseudoaleatorio ------------ 
def generate_keystream(length, seed):
    random.seed(seed)
    return bytes([random.randint(0, 255) for _ in range(length)])

# ------------ Cifrado XOR - keystream ------------------------
def xor_encrypt(plaintext, keystream):
    plaintext_bytes = plaintext.encode()
    return bytes([b ^ k for b, k in zip(plaintext_bytes, keystream)])

# ------------ Decifrado XOR - keystream ------------------------
def xor_decrypt(ciphertext, keystream):
    return bytes([c ^ k for c, k in zip(ciphertext, keystream)]).decode()

message = "Hola, esto es un mensaje de prueba"
seed = 42
keystream = generate_keystream(len(message), seed)
ciphertext = xor_encrypt(message, keystream)
decrypted_message = xor_decrypt(ciphertext, keystream)

print("Texto plano:", message)
print("Keystream:", keystream)
print("Texto cifrado:", ciphertext)
print("Texto descifrado:", decrypted_message)

# --------- Pruebas unitarias ------------------
class TestXORCipher(unittest.TestCase):
    def test_encryption_decryption(self):
        message = "Mensaje de prueba"
        seed = 1234
        keystream = generate_keystream(len(message), seed)
        ciphertext = xor_encrypt(message, keystream)
        decrypted_message = xor_decrypt(ciphertext, keystream)
        self.assertEqual(decrypted_message, message)
    
    def test_different_keys(self):
        message = "Mensaje secreto"
        seed1 = 42
        seed2 = 43
        keystream1 = generate_keystream(len(message), seed1)
        keystream2 = generate_keystream(len(message), seed2)
        ciphertext1 = xor_encrypt(message, keystream1)
        ciphertext2 = xor_encrypt(message, keystream2)
        self.assertNotEqual(ciphertext1, ciphertext2)  
    
    def test_keystream_reuse_risk(self):
        message1 = "Hola mundo"
        message2 = "Secreto X"
        seed = 99
        keystream = generate_keystream(max(len(message1), len(message2)), seed)
        ciphertext1 = xor_encrypt(message1, keystream)
        ciphertext2 = xor_encrypt(message2, keystream)
        recovered_xor = bytes([c1 ^ c2 for c1, c2 in zip(ciphertext1, ciphertext2)])
        self.assertNotEqual(recovered_xor, keystream) 

if __name__ == "__main__":
    unittest.main()
