# pip install colorama

import socket
import datetime
from colorama import Fore, Style

def honeypot(host="0.0.0.0", port=8080):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)

    print(f"{Fore.GREEN}[+] Honeypot Running on {host}:{port}{Style.RESET_ALL}")

    while True:
        conn, addr = sock.accept()
        print(f"{Fore.YELLOW}[!] Connection Attempt from {addr[0]}:{addr[1]}{Style.RESET_ALL}")

        # Log the connection attempt
        with open("honeypot_logs.txt", "a") as log_file:
            log_file.write(f"{datetime.datetime.now()} - Connection from {addr[0]}:{addr[1]}\n")

        # Fake banner to trick attackers
        conn.sendall(b"Fake SSH Server v2.0\nUsername: ")
        conn.close()

if __name__ == "__main__":
    honeypot()
