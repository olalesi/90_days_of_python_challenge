# program to check eligibility for services based on age

# User's age as input
age = int(input("Enter youyr age: "))

# Using conditional statements to check eligibility status
if age < 18:
  print("You are too young to vote.")
elif age >= 18 and age < 21:
  print("You are eligible to vote but not for some restricted services (e.g., alcohol).")
else:
  print("You are eligible to vote and access all services.")

# Check eligibility for Senior Citizen Retirement Plan
if age >+ 60:
  print("You are eligible for Senior Citizen Retirement Plan.")
  
