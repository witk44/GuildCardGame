import pygame
import sys
import socket
import threading
from GameCode import *
from utilities import *

# Define screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialize Pygame
pygame.init()

s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = find_open_port()
game_code = encrypt_game_code(str(ip),str(port))
print(game_code)
# Server configuration
SERVER_IP = ip  # Change this to your desired server IP address
SERVER_PORT = port  # Change this to your desired server port

# Initialize the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen()

clients = []  # List to store client connections


# Function to create the Pygame screen
def create_pygame_screen(game_code, num_of_players):
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Game Information")

    font = pygame.font.Font(None, 36)

    while True:
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill((255, 255, 255))

        # Render the game code and number of players on the screen
        game_code_text = font.render("Game Code: " + game_code, True, (0, 0, 0))
        num_of_players_text = font.render("Number of Players: " + str(num_of_players), True, (0, 0, 0))

        # Center the text on the screen
        game_code_rect = game_code_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        num_of_players_rect = num_of_players_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))

        # Blit the text on the screen
        screen.blit(game_code_text, game_code_rect)
        screen.blit(num_of_players_text, num_of_players_rect)

        pygame.display.flip()

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
game_code_thread = threading.Thread(target=create_pygame_screen, args=(game_code, len(clients)))
game_code_thread.start()
