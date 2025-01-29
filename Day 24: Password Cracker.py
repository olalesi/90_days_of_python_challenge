import hashlib
import itertools

def brute_force_crack(hash_to_crack, wordlist):
    print("Starting brute force attack...\n")
    
    # Read the wordlist (list of possible passwords)
    with open(wordlist, 'r') as file:
        words = file.readlines()

    # Clean up any newline characters from the wordlist
    words = [word.strip() for word in words]
    
    # Try each word from the wordlist and hash it
    for word in words:
        # Hash the current word using SHA-256 (you can change the algorithm if needed)
        hashed_word = hashlib.sha256(word.encode()).hexdigest()

        # Compare the hash to the target hash
        if hashed_word == hash_to_crack:
            print(f"Password found: {word}")
            return word

    print("Password not found in the wordlist.")
    return None

# Input: the hash to crack and the wordlist file
target_hash = input("Enter the hash to crack (SHA-256): ")
wordlist_file = input("Enter the path to the wordlist file (e.g., big.txt): ")

# Run the brute-force attack
cracked_password = brute_force_crack(target_hash, wordlist_file)

if cracked_password:
    print(f"Password is: {cracked_password}")
else:
    print("No matching password found.")
