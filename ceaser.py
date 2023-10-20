def caesar_cipher(text, shift, mode):
    result = ''
    shift %= 26  # Ensure the shift is within the range of the alphabet (26 letters)

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()

            if mode == 'encrypt':
                char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            elif mode == 'decrypt':
                char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))

            if is_upper:
                char = char.upper()

        result += char

    return result

# Example usage:
plaintext = "Hello, World!"
shift = 3
encrypted_text = caesar_cipher(plaintext, shift, mode='encrypt')
print("Encrypted:", encrypted_text)

decrypted_text = caesar_cipher(encrypted_text, shift, mode='decrypt')
print("Decrypted:", decrypted_text)

