import requests
from bs4 import BeautifulSoup

# Ask user for the target URL
url = input("Enter the website URL (include http/https): ")

# Send a GET request to fetch the webpage content
try:
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors

    # Extract headers from response
    headers = response.headers

    print("\n🔍 Security Headers Found:")
    for header in ["Server", "X-Powered-By", "Strict-Transport-Security", "Content-Security-Policy"]:
        print(f"{header}: {headers.get(header, 'Not Found')}")

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract and display meta tags
    print("\n🔍 Extracted Meta Tags:")
    for meta in soup.find_all("meta"):
        print(meta)

    # Extract and display all links
    print("\n🔍 Extracted Links:")
    for link in soup.find_all("a", href=True):
        print(link["href"])

except requests.exceptions.RequestException as e:
    print(f"❌ Error: {e}")
