# Program that takes user input for their name and age, then prints a greeting and calculates the birth year

# Taking input from the user
name = input("Enter your name: ")   # string input
age = int(input("Enter your age : ")) # converts to integer

# Calculating the year of birth
current_year = 2025
birth_year = current_year - age

# Printing a greeting and the year the user was born
print(f"Hello, {name}! You were born in the year {birth_year}.")
