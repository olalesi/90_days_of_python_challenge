import socket

HOST = "0.0.0.0"  # Listen on all interfaces
PORT = 4444  # Change to any available port

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"🚀 Listening on {HOST}:{PORT}...")

    conn, addr = server.accept()
    print(f"🔥 Connection received from {addr}")

    while True:
        command = input("Enter command: ")
        if command.lower() in ["exit", "quit"]:
            conn.sendall(b"exit")
            break

        conn.sendall(command.encode())
        response = conn.recv(4096).decode()
        print(f"📌 Response:\n{response}")

    conn.close()
    server.close()

if __name__ == "__main__":
    start_server()
