# Ask the user to enter a number
try:
    user_input = input("Enter a number: ")
    
    # Convert the input to an integer
    number = int(user_input)
    
    # Print the number if input is valid
    print(f"Great! You entered the number: {number}")

# Handle invalid input (e.g., if the user enters a non-numeric value)
except ValueError:
    print("Error: That's not a valid number. Please enter a numeric value.")

# Add a finally block to execute code regardless of the result
finally:
    print("Thank you for using the program!")
