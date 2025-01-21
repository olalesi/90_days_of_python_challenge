import requests
from bs4 import BeautifulSoup

# Function to fetch and parse the webpage
def scrape_website(url):
    # Send an HTTP request to the user-provided URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find all the headline elements (for this example, we're looking for <h3> tags)
        headlines = soup.find_all("h3")
        
        print("\nLatest Headlines from the Website:")
        
        # Extract and display the text of each headline
        for index, headline in enumerate(headlines[:10], 1):  # Limiting to top 10 headlines
            print(f"{index}. {headline.get_text()}")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Main function to run the program
def main():
    # Ask the user for the URL
    url = input("Enter the URL of the website to scrape: ")
    
    # Scrape the website with the provided URL
    scrape_website(url)

if __name__ == "__main__":
    main()
