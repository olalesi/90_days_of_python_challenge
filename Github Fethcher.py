import requests  # Import the requests library

# Function to fetch GitHub user data
def fetch_github_user(username):
    # GitHub API endpoint for user data
    url = f"https://api.github.com/users/{username}"
    try:
        # Send a GET request to the GitHub API
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            user_data = response.json()
            # Display user information
            print(f"User: {user_data['login']}")
            print(f"Name: {user_data.get('name', 'N/A')}")
            print(f"Bio: {user_data.get('bio', 'N/A')}")
            print(f"Public Repositories: {user_data['public_repos']}")
            print(f"Followers: {user_data['followers']}")
            print(f"Following: {user_data['following']}")
            print(f"Profile URL: {user_data['html_url']}")
        else:
            # If the user is not found
            print(f"Error: User '{username}' not found (status code {response.status_code}).")
    except requests.exceptions.RequestException as e:
        # Handle network or other request errors
        print(f"An error occurred: {e}")

# Main program
def main():
    print("Welcome to the GitHub User Fetcher!")
    print("Type 'quit' to exit the program.")
    
    while True:
        # Get the GitHub username from the user
        username = input("Enter a GitHub username: ")
        if username.lower() == "quit":
            print("Goodbye!")
            break
        # Fetch and display the user's data
        fetch_github_user(username)

if __name__ == "__main__":
    main()
