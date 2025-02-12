from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def encrypt_data(key, data):
    # Generate random IV (Initialization Vector)
    iv = os.urandom(16)
    
    # Create AES cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Pad data to be multiple of block size (AES block size = 16 bytes)
    padding = 16 - len(data) % 16
    padded_data = data + bytes([padding] * padding)
    
    # Encrypt the data
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    
    return iv + encrypted_data  # Return IV and encrypted data

# Example usage:
key = b'secretkey1234567'  # Weak 16-byte key (for demonstration purposes)
data = b"Hello, this is a secret message!"
encrypted_data = encrypt_data(key, data)
print("Encrypted Data:", encrypted_data)
