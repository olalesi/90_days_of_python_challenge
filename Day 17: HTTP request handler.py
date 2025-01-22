import requests

# Function to fetch and save the content of a webpage to a file
def fetch_and_save_page_content(url):
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print(f"Successfully fetched the content of: {url}")
        
        # Save the raw HTML content of the webpage to a text file
        with open("webpage_content.txt", "w", encoding="utf-8") as file:
            file.write(response.text)  # Write the HTML content to the file
        
        print("The webpage content has been saved as 'webpage_content.txt'.")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Main function to run the program
def main():
    # Ask the user for the URL to fetch
    url = input("Enter the URL of the webpage to fetch: ")
    
    # Fetch and save the content of the webpage
    fetch_and_save_page_content(url)

if __name__ == "__main__":
    main()
