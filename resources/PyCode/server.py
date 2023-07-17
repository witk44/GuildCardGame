import socket
import threading
s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)

# Server configuration
SERVER_IP = ip  # Change this to your desired server IP address
SERVER_PORT = 5000  # Change this to your desired server port

# Initialize the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen()

clients = []  # List to store client connections

# Function to handle client connections
def handle_client(client_socket, client_address):
    while True:
        try:
            # Receive data from the client
            data = client_socket.recv(1024).decode('utf-8')
            # Process the received data

            # Broadcast the processed data to other clients
            for client in clients:
                if client != client_socket:
                    client.send(data.encode('utf-8'))
        except Exception as e:
            print(f"Error: {e}")
            clients.remove(client_socket)
            client_socket.close()
            break

# Function to accept incoming connections
def accept_connections():
    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        print(f"New connection from {client_address[0]}:{client_address[1]}")

        # Start a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

# Start accepting incoming connections
print("Server started. Waiting for connections...")
accept_thread = threading.Thread(target=accept_connections)
accept_thread.start()
