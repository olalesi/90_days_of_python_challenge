# Import the math library
import math

# Ask the user to input a number
try:
    number = float(input("Enter a number to calculate its square root: "))

    # Check if the number is non-negative
    if number < 0:
        print("Error: Square root of a negative number is not defined for real numbers.")
    else:
        # Calculate the square root using math.sqrt()
        result = math.sqrt(number)
        print(f"The square root of {number} is {result}")

except ValueError:
    print("Error: Please enter a valid numeric value.")
