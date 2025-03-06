import socket
import logging

# Configure logging
logging.basicConfig(filename="firewall.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Blocked IPs (Modify this list)
BLOCKED_IPS = ["192.168.1.100", "203.0.113.45"]  # Example IPs

# Firewall settings
HOST = "0.0.0.0"  # Listen on all interfaces
PORT = 8080        # Port to monitor

def firewall():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)

    print(f"🚀 Firewall is running on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server.accept()
        ip, port = client_address

        # Log the connection attempt
        logging.info(f"Incoming connection from {ip}:{port}")

        if ip in BLOCKED_IPS:
            print(f"❌ Blocked connection from {ip}")
            client_socket.close()
        else:
            print(f"✅ Allowed connection from {ip}")
            client_socket.send(b"Connection accepted\n")
            client_socket.close()

if __name__ == "__main__":
    firewall()
