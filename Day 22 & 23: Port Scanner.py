import socket

def scan_ports(target, start_port, end_port):
    print(f"Starting scan on target: {target}")
    print(f"Scanning ports {start_port} to {end_port}...\n")
    
    for port in range(start_port, end_port + 1):
        try:
            # Create a socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)  # Set timeout for the connection attempt
            
            # Try connecting to the port
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port}: OPEN")
            s.close()
        except KeyboardInterrupt:
            print("\nScan interrupted by user.")
            break
        except Exception as e:
            print(f"Error scanning port {port}: {e}")
            continue

    print("\nScan complete.")

# Ask user for the target and port range
target_ip = input("Enter the target IP or hostname: ")
start = int(input("Enter the starting port: "))
end = int(input("Enter the ending port: "))

# Perform the port scan
scan_ports(target_ip, start, end)
