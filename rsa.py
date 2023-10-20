# Function to calculate the greatest common divisor (GCD)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to calculate the modular inverse of a number
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Given values
p = 7
q = 11
e = 17
n = p * q  # Calculate n (modulus)
phi = (p - 1) * (q - 1)  # Calculate Euler's totient function

# Calculate d (private key)
d = mod_inverse(e, phi)

# Message to be encrypted
M = 8

# Encryption (Ciphertext = M^e mod n)
C = (M ** e) % n

# Decryption (Decrypted message = C^d mod n)
decrypted_message = (C ** d) % n

print("Original Message (M):", M)
print("Encrypted Message (C):", C)
print("Decrypted Message:", decrypted_message)

