#pip install pycipher

from pycipher import Caesar

text = "Hello, World!"
shift = 3

# Encrypt
cipher = Caesar(key=shift)
encrypted_text = cipher.encipher(text)
print("Encrypted:", encrypted_text)

# Decrypt
decrypted_text = cipher.decipher(encrypted_text)
print("Decrypted:", decrypted_text)
