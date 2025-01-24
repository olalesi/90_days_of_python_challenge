from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

# Function to encrypt the message
def encrypt_message(key, plaintext):
    # Generate a random 128-bit (16-byte) IV (Initialization Vector)
    iv = os.urandom(16)

    # Create the cipher object using AES algorithm in CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    # Pad the plaintext to make it a multiple of block size (128 bits = 16 bytes)
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()

    # Create an encryptor and encrypt the padded plaintext
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    return iv, ciphertext

# Function to decrypt the message
def decrypt_message(key, iv, ciphertext):
    # Create the cipher object using AES algorithm in CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    # Create a decryptor and decrypt the ciphertext
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Unpad the decrypted data
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    return plaintext.decode()

# Main function to demonstrate encryption and decryption
def main():
    # Key must be 16, 24, or 32 bytes long (AES-128, AES-192, or AES-256)
    key = os.urandom(32)  # 256-bit key for AES-256

    # Get the message from the user
    message = input("Enter the message to encrypt: ")

    # Encrypt the message
    iv, encrypted_message = encrypt_message(key, message)
    print("\nEncrypted message:", encrypted_message.hex())

    # Decrypt the message
    decrypted_message = decrypt_message(key, iv, encrypted_message)
    print("\nDecrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
