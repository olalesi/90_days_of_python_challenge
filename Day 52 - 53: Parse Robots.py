import requests

def fetch_robots_txt(url):
    if not url.startswith("http"):
        url = "http://" + url  # Ensure URL has HTTP/HTTPS

    robots_url = url.rstrip("/") + "/robots.txt"
    
    try:
        response = requests.get(robots_url, timeout=5)
        if response.status_code == 200:
            print(f"✅ Successfully retrieved robots.txt from {url}\n")
            return response.text
        else:
            print(f"⚠️ Could not retrieve robots.txt (Status Code: {response.status_code})")
            return None
    except requests.RequestException as e:
        print(f"❌ Error fetching robots.txt: {e}")
        return None

def parse_robots(robots_txt):
    disallowed_paths = []
    for line in robots_txt.split("\n"):
        if line.lower().startswith("disallow:"):
            path = line.split(":", 1)[1].strip()
            disallowed_paths.append(path)
    
    return disallowed_paths

def save_to_file(url, disallowed_paths):
    filename = "robots_results.txt"
    with open(filename, "w") as file:
        file.write(f"Website: {url}\n")
        file.write("Disallowed Paths:\n")
        for path in disallowed_paths:
            file.write(f"- {path}\n")
    
    print(f"\n✅ Results saved to {filename}")

if __name__ == "__main__":
    target_url = input("🔗 Enter website URL (e.g., example.com): ").strip()
    
    robots_txt = fetch_robots_txt(target_url)
    if robots_txt:
        disallowed_paths = parse_robots(robots_txt)
        if disallowed_paths:
            print("\n🚨 Potential Sensitive Paths Found:")
            for path in disallowed_paths:
                print(f"  - {path}")
            save_to_file(target_url, disallowed_paths)
        else:
            print("✅ No sensitive paths found.")
