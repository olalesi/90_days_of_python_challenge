import re  # Import the regular expressions library

# Function to validate email addresses
def validate_email(email):
    # Define a simple email validation pattern
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$'
    
    # Check if the email matches the pattern
    if re.match(email_pattern, email):
        return True
    else:
        return False

# Main program
print("Welcome to the Email Validator!")
print("Type 'quit' to exit the program.")

while True:
    # Ask the user to input an email address
    email = input("Enter an email address: ")
    
    # Exit the loop if the user types 'quit'
    if email.lower() == 'quit':
        print("Goodbye!")
        break
    
    # Validate the email and print the result
    if validate_email(email):
        print(f"'{email}' is a valid email address!")
    else:
        print(f"'{email}' is NOT a valid email address.")
