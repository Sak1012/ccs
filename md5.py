import hashlib

# Function to calculate MD5 hash
def calculate_md5(text):
    md5_hash = hashlib.md5()
    md5_hash.update(text.encode('utf-8'))
    return md5_hash.hexdigest()

# Example usage
text = "This is the text for which we want to calculate the MD5 hash."
md5_digest = calculate_md5(text)
print("MD5 Digest:", md5_digest)
