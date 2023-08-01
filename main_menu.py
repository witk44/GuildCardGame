import pygame
import sys
import socket
import threading
from resources.PyCode.utilities import *
import subprocess

# Initialize Pygame
pygame.init()

# Set up the display
screen_info = pygame.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Guild Card Game")

# Load the background image
background_image = pygame.image.load(app_path("resources/images/Guild_Logo.jpg"))  
# Resize the background image to fit the screen
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))


# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up fonts
font_title = pygame.font.Font(None, 72)
font_options = pygame.font.Font(None, 48)

# Set up text
title_text = font_title.render("Guild Main Menu", True, WHITE)
join_text = font_options.render("Join Game", True, WHITE)
host_text = font_options.render("Host Game", True, WHITE)

# Set up text positions
title_text_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 4))
join_text_rect = join_text.get_rect(center=(screen_width // 2, screen_height // 2))
host_text_rect = host_text.get_rect(center=(screen_width // 2, screen_height // 2 + 50))

# Function to start the server in a separate thread
def start_server():
    global server_process
    server_process = subprocess.Popen(['python', app_path('resources/PyCode/server.py')])
    

# Function to start the client in a separate thread
def start_client():
    global client_process  
    client_process = subprocess.Popen(['python', app_path('resources/PyCode/client.py')])

def kill_client():
    client_process.kill()

def kill_server():
    server_process.kill()

# Main menu loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            kill_client()
            kill_server()
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if join_text_rect.collidepoint(mouse_pos):
                client_thread = threading.Thread(target=start_client)
                client_thread.daemon = True
                client_thread.start()
                print("Joining a game...")
                # Add your code for joining a game here
            elif host_text_rect.collidepoint(mouse_pos):
                server_thread = threading.Thread(target=start_server)
                server_thread.daemon = True
                server_thread.start()
                print("Hosting a game...")
                # Add your code for hosting a game here

    # Draw the background
    screen.fill(BLACK)
     # Draw the background image
    screen.blit(background_image, (0, 0))

    # Draw the text
    screen.blit(title_text, title_text_rect)
    screen.blit(join_text, join_text_rect)
    screen.blit(host_text, host_text_rect)

    # Update the display
    pygame.display.flip()