import socket

# Function to create the client
def start_client():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect the client to the server's IP address and port
    host = "127.0.0.1"  # Localhost (same machine)
    port = 65432         # Port number (must match server port)
    
    client_socket.connect((host, port))
    
    # Send data to the server
    message = "Hello, Server!"
    client_socket.sendall(message.encode())
    
    # Receive the response from the server
    data = client_socket.recv(1024)
    print(f"Received from server: {data.decode()}")
    
    # Close the connection
    client_socket.close()

# Start the client
if __name__ == "__main__":
    start_client()
