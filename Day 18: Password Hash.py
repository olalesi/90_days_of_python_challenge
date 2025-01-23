import hashlib

# Function to hash the password using SHA256
def hash_password(password):
    # Create a SHA256 hash object
    sha256_hash = hashlib.sha256()
    
    # Update the hash object with the bytes of the password
    sha256_hash.update(password.encode('utf-8'))
    
    # Return the hexadecimal representation of the hash
    return sha256_hash.hexdigest()

# Known hash (replace with an actual hash to compare against)
known_hash = "5e884898da28047151d0e56f8dc6292773603d0d28f6c424e9889754f7f93d20"  # SHA256 of "password"

# Accept user input for password
user_input = input("Enter your password: ")

# Hash the entered password
hashed_input = hash_password(user_input)

# Compare the entered password hash with the known hash
if hashed_input == known_hash:
    print("Password is correct!")
else:
    print("Password is incorrect.")
