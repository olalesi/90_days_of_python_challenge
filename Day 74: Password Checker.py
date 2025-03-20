import re

# Common weak passwords (expand as needed)
WEAK_PASSWORDS = ["password", "123456", "qwerty", "abc123", "letmein", "welcome", "admin", "passw0rd"]

def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password is too short. Use at least 8 characters.")

    # Check uppercase and lowercase
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Add both uppercase and lowercase letters.")

    # Check numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number.")

    # Check special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one special character (e.g., @, #, $).")

    # Check against weak password list
    if password.lower() in WEAK_PASSWORDS:
        feedback.append("❌ This is a commonly used weak password!")

    # Determine strength level
    if score == 5:
        strength = "✅ Strong"
    elif score >= 3:
        strength = "⚠️ Medium"
    else:
        strength = "❌ Weak"

    return strength, feedback

if __name__ == "__main__":
    password = input("Enter a password to check: ")
    strength, feedback = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    for msg in feedback:
        print(msg)
