import socket

# Create a socket object for TCP communication
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server to a specific IP and port
server_socket.bind(('localhost', 12345))

# Listen for incoming connections
server_socket.listen(5)
print("Server is waiting for a connection...")

# Accept a client connection
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

# Communicate with the client
while True:
    # Receive the message from the client
    message = client_socket.recv(1024).decode()
    if message.lower() == 'exit':
        print("Connection closed by client.")
        break
    print(f"Client says: {message}")
    
    # Send a response to the client
    response = input("You (Server) > ")
    client_socket.send(response.encode())

# Close the connection
client_socket.close()
server_socket.close()
