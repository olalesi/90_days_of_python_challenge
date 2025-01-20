import socket

# Function to create the server
def start_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the address and port
    host = "127.0.0.1"  # Localhost
    port = 65432         # Non-privileged port
    server_socket.bind((host, port))
    
    # Enable the server to listen for connections (max 1 connection at a time)
    server_socket.listen(1)
    print(f"Server started, waiting for connection on {host}:{port}...")
    
    while True:
        # Wait for a client connection
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")
        
        # Receive data from the client
        data = conn.recv(1024)
        if not data:
            break
        
        print(f"Received: {data.decode()}")
        
        # Send a response back to the client
        conn.sendall(b"Hello, Client!")
        
        # Close the connection
        conn.close()

# Start the server
if __name__ == "__main__":
    start_server()
