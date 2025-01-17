import json  # Import the JSON library

# Function to load JSON data from a file
def load_json(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)  # Parse the JSON file into a Python dictionary
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON.")
        return None

# Main function to interact with the user
def main():
    # Load JSON data from the file
    data = load_json("data.json")
    if not data:
        return  # Exit if the JSON file couldn't be loaded

    print("JSON Data Loaded!")
    print("You can search for a user's details by their name.")
    print("Type 'quit' to exit the program.")
    
    while True:
        # Get the user's input
        name = input("Enter a name: ")
        if name.lower() == "quit":
            print("Goodbye!")
            break

        # Search for the user in the JSON data
        found = False
        for user in data.get("users", []):
            if user["name"].lower() == name.lower():
                print(f"Name: {user['name']}, Age: {user['age']}, Email: {user['email']}")
                found = True
                break

        if not found:
            print(f"No user found with the name '{name}'.")

if __name__ == "__main__":
    main()
