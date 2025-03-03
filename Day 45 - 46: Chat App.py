import socket

# Create a socket object for TCP communication
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(('localhost', 12345))
print("Connected to the server.")

# Communicate with the server
while True:
    # Send a message to the server
    message = input("You (Client) > ")
    client_socket.send(message.encode())
    
    # Receive the response from the server
    response = client_socket.recv(1024).decode()
    print(f"Server says: {response}")
    
    if message.lower() == 'exit':
        print("Connection closed by client.")
        break

# Close the connection
client_socket.close()
