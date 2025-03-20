from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import time
import tracemalloc
from ChaCha20 import chacha20_encrypt

def aes_encrypt(plaintext):
    key = get_random_bytes(16)
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_text = plaintext.encode() + b' ' * (16 - len(plaintext) % 16)
    ciphertext = cipher.encrypt(padded_text)
    return key, iv, ciphertext

def benchmark(func, *args):
    tracemalloc.start()
    start_time = time.perf_counter()
    result = func(*args)
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return (result, end_time - start_time, peak / 1024)

if __name__ == "__main__":
    plaintext = "Probamos un mensaje un poco largo para ver tiempos y memoria " * 1000

    print("\nBenchmark ChaCha20:")
    _, chacha_time, chacha_mem = benchmark(chacha20_encrypt, plaintext)
    print(f"Tiempo: {chacha_time:.6f} s | Memoria: {chacha_mem:.2f} KB")

    print("\nBenchmark AES-CBC:")
    _, aes_time, aes_mem = benchmark(aes_encrypt, plaintext)
    print(f"Tiempo: {aes_time:.6f} s | Memoria: {aes_mem:.2f} KB")
