from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes

# Generate DSA key pair
private_key = dsa.generate_private_key(key_size=1024)
public_key = private_key.public_key()

# Sign a message
message = b"This is a message to be signed."
signature = private_key.sign(message, hashes.SHA256())

# Verify the signature
try:
    public_key.verify(signature, message, hashes.SHA256())
    print("Signature is valid.")
except:
    print("Signature is invalid.")

