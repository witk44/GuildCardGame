import pygame
import socket
import threading

s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)

# Server configuration
SERVER_IP = ip  # Change this to the server IP address
SERVER_PORT = 5000  # Change this to the server port

# Client configuration
CLIENT_IP = '127.0.0.1'  # Change this to the client IP address
CLIENT_PORT = 5001  # Change this to the client port

# Initialize the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))

# Function to handle receiving data from the server
def receive_data():
    while True:
        try:
            # Receive data from the server
            data = client_socket.recv(1024).decode('utf-8')
            # Process the received data
            
            # TODO: Update game state based on the received data
            
        except Exception as e:
            print(f"Error: {e}")
            client_socket.close()
            break

# Function to send data to the server
def send_data(data):
    try:
        # Send data to the server
        client_socket.send(data.encode('utf-8'))
    except Exception as e:
        print(f"Error: {e}")
        client_socket.close()

# Start receiving data from the server
receive_thread = threading.Thread(target=receive_data)
receive_thread.start()

# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

player_x = 400
player_y = 300

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= 5
                send_data(f"POS {player_x} {player_y}")  # Send player position to the server
            elif event.key == pygame.K_RIGHT:
                player_x += 5
                send_data(f"POS {player_x} {player_y}")  # Send player position to the server
            elif event.key == pygame.K_UP:
                player_y -= 5
                send_data(f"POS {player_x} {player_y}")  # Send player position to the server
            elif event.key == pygame.K_DOWN:
                player_y += 5
                send_data(f"POS {player_x} {player_y}")  # Send player position to the server

    # TODO: Update game state based on the server updates

    # Update the game display
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 255), (player_x, player_y, 50, 50))
    pygame.display.flip()
    clock.tick(60)
