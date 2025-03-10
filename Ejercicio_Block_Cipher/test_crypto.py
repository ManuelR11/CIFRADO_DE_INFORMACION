import unittest
from DES.DES import des_encrypt_ecb, des_decrypt_ecb
from _3DES._3DES import triple_des_encrypt_cbc, triple_des_decrypt_cbc
from AES_CBC_ECB.AES import aes_encrypt_text, aes_decrypt_text, aes_encrypt_image, aes_decrypt_image


class TestCryptoMethods(unittest.TestCase):

    def test_des(self):
        plaintext = "Hola DES"
        key, encrypted = des_encrypt_ecb(plaintext)
        decrypted = des_decrypt_ecb(key, encrypted)
        self.assertEqual(decrypted, plaintext)

    def test_triple_des(self):
        plaintext = "Hola 3DES"
        key, iv, encrypted = triple_des_encrypt_cbc(plaintext)
        decrypted = triple_des_decrypt_cbc(key, iv, encrypted)
        self.assertEqual(decrypted, plaintext)

    def test_aes_text(self):
        plaintext = "Hola AES"
        key, iv, encrypted = aes_encrypt_text(plaintext)
        decrypted = aes_decrypt_text(key, iv, encrypted)
        self.assertEqual(decrypted, plaintext)

    def test_aes_image(self):
        key, iv, ciphertext_ecb, ciphertext_cbc = aes_encrypt_image("AES_CBC_ECB/pic.png")
        decrypted_ecb, decrypted_cbc = aes_decrypt_image(key, iv, ciphertext_ecb, ciphertext_cbc)

        with open("AES_CBC_ECB/pic.png", "rb") as f:
            original_data = f.read()

        self.assertEqual(decrypted_ecb, original_data)
        self.assertEqual(decrypted_cbc, original_data)

if __name__ == "__main__":
    unittest.main()
