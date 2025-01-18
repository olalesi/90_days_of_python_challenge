import requests  # Import the requests library

# Function to fetch weather data from wttr.in
def get_weather(city):
    # API endpoint for wttr.in with the city name
    url = f"http://wttr.in/{city}?format=%C+%t"
    try:
        # Send a GET request to wttr.in
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            # Print the weather information
            print(f"Weather in {city.capitalize()}: {response.text}")
        else:
            print(f"Error: Unable to fetch weather for '{city}'.")
    except requests.exceptions.RequestException as e:
        # Handle network or other request errors
        print(f"An error occurred: {e}")

# Main program
def main():
    print("Welcome to the Weather Checker!")
    print("Type 'quit' to exit the program.")
    
    while True:
        # Ask the user for a city name
        city = input("Enter the name of a city: ")
        if city.lower() == "quit":
            print("Goodbye!")
            break
        # Fetch and display the weather for the entered city
        get_weather(city)

if __name__ == "__main__":
    main()
