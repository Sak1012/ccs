import hashlib

# Function to calculate SHA-1 hash
def calculate_sha1(text):
    sha1_hash = hashlib.sha1()
    sha1_hash.update(text.encode('utf-8'))
    return sha1_hash.hexdigest()

# Example usage
text = "This is the text for which we want to calculate the SHA-1 hash."
sha1_digest = calculate_sha1(text)
print("SHA-1 Digest:", sha1_digest)
