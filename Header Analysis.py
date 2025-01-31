import requests

def check_security_headers(url):
    # List of security headers to check
    required_headers = [
        "Strict-Transport-Security", 
        "X-Content-Type-Options", 
        "X-XSS-Protection", 
        "Content-Security-Policy", 
        "X-Frame-Options", 
        "Referrer-Policy"
    ]
    
    try:
        # Send a GET request to fetch the headers
        response = requests.get(url)
        
        # Print all the headers returned by the server
        print(f"Headers for {url}:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")

        print("\nChecking for missing security headers:")
        # Check for missing headers
        for header in required_headers:
            if header not in response.headers:
                print(f"Missing header: {header}")
            else:
                print(f"Found {header}: {response.headers[header]}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching headers from {url}: {e}")

# Input the target URL
target_url = input("Enter the URL to analyze (e.g., http://example.com): ")

# Run the header analysis
check_security_headers(target_url)
