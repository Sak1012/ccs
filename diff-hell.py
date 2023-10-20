# Parameters
q = 11  # A prime number
g = 2   # A primitive root modulo q

# User A's private key
XA = 2

# User B's private key
XB = 3

# Calculate User A's public key (YA)
YA = (g ** XA) % q

# Calculate User B's public key (YB)
YB = (g ** XB) % q

# Calculate the shared secret key (k) for User A and B
k_A = (YB ** XA) % q  # User A calculates k using User B's public key and their private key
k_B = (YA ** XB) % q  # User B calculates k using User A's public key and their private key

print("User A's Public Key (YA):", YA)
print("User B's Public Key (YB):", YB)
print("Shared Secret Key (k) for User A:", k_A)
print("Shared Secret Key (k) for User B:", k_B)

