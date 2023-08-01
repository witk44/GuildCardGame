import pygame
import socket
import threading
import sys
from utilities import *
from GameCode import *
s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
def enter_game_code():
    global game_code
    pygame.init()

    # Set up the display
    screen_width, screen_height = 500, 300
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Enter Game Code")
    
    # Load the background image
    background_image = pygame.image.load(app_path("resources/images/Guild_Logo.jpg"))  
    # Resize the background image to fit the screen
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
    # Set up colors
    black = (0, 0, 0)
    white = (255, 255, 255)

    # Set up fonts
    font = pygame.font.Font(None, 32)

    # Initialize variables
    game_code = ""

    # Create a submit button
    class SubmitButton(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.Surface((60, 30))
            self.image.fill(black)
            self.rect = self.image.get_rect(center=(screen_width // 2, 180))

        def update(self):
            pass

    submit_button = SubmitButton()
    all_sprites = pygame.sprite.Group(submit_button)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                # Check if the key pressed is alphanumeric or space
                if event.unicode.isalnum():
                    game_code += event.unicode
                # If Backspace is pressed, remove the last character from user_input
                elif event.key == pygame.K_BACKSPACE:
                    game_code = game_code[:-1]

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the submit button is clicked
                if submit_button.rect.collidepoint(event.pos):
                    run = False
        if run:
            # Clear the screen
            screen.fill(white)

            # Render the game code and user input text on the screen
            game_code_text = font.render("Game Code: " + game_code, True, black)
            screen.blit(background_image,(0,0))
            screen.blit(game_code_text, (10, 10))

            # Draw the submit button
            all_sprites.update()
            all_sprites.draw(screen)

            pygame.display.update()


enter_game_code()
server_ip,server_port=decrypt_game_code(game_code)
# Server configuration
SERVER_IP = server_ip
SERVER_PORT = server_port

# Client configuration
CLIENT_IP = ip  
CLIENT_PORT = find_open_port()  
# Initialize the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, int(SERVER_PORT)))


global player_x
global player_y

player_x = 400
player_y = 300



# Function to handle receiving data from the server
def receive_data():
    run = True
    while run:
        try:
            # Receive data from the server
            data = client_socket.recv(1024).decode('utf-8')
            # Process the received data
            data = data.split(" ")
            player_x = data[1]
            player_y  = data[2]
            # TODO: Update game state based on the received data
        except Exception as e:
            print(f"Error: {e}")
            client_socket.close()
        

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
receive_thread.daemon = True
receive_thread.start()
# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


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
