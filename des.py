from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

# Generate a random 8-byte key (64 bits)
key = get_random_bytes(8)

def des_encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_plaintext = _pad(plaintext)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def des_decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = cipher.decrypt(ciphertext)
    return _unpad(decrypted_text).decode('utf-8')

def _pad(text):
    pad_length = 8 - len(text) % 8
    return text + bytes([pad_length] * pad_length)

def _unpad(text):
    pad_length = text[-1]
    return text[:-pad_length]

# Example usage:
plaintext = "Hello, DES!"
print("Original Text:", plaintext)

encrypted_text = des_encrypt(plaintext.encode('utf-8'), key)
print("Encrypted Text:", encrypted_text)

decrypted_text = des_decrypt(encrypted_text, key)
print("Decrypted Text:", decrypted_text)

