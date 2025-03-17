## pip install python-nmap

import nmap
import sys

def scan_target(target_ip):
    """Scans the target IP using Nmap and returns the results."""
    nm = nmap.PortScanner()
    print(f"[+] Scanning {target_ip} for open ports...")

    # Perform a basic scan for open ports
    nm.scan(target_ip, arguments="-sV -p 1-1000")  # Scan ports 1-1000 with service detection

    results = []
    for host in nm.all_hosts():
        results.append(f"\n[+] Host: {host} ({nm[host].hostname()})")
        results.append(f"    Status: {nm[host].state()}")

        for proto in nm[host].all_protocols():
            results.append(f"    Protocol: {proto}")
            ports = nm[host][proto].keys()
            for port in sorted(ports):
                state = nm[host][proto][port]["state"]
                service = nm[host][proto][port]["name"]
                results.append(f"    Port {port}: {state} ({service})")

    return "\n".join(results)

def save_results(results, filename="scan_results.txt"):
    """Saves scan results to a file."""
    with open(filename, "w") as file:
        file.write(results)
    print(f"[+] Scan results saved to {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python nmap_scanner.py <target-ip>")
        sys.exit(1)

    target = sys.argv[1]
    scan_data = scan_target(target)
    print(scan_data)
    save_results(scan_data)
