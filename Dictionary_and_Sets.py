# Program  to store User Information and retrive it by name
# Empty dictionary to store user data
user_data = {}

# Add user info to the dictionary
name = input("Enter the name: ")
age = input("Enter the age: ")
user_data[name] = age

# Retrieve user info
search_name = input("Enter the name to retrieve their age: ")
if search_name in user_data:
  print(f"{search_name} is {user_data[search_name]} years old.")
else:
  print(f"No information found for {search_name}.")
