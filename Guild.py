import pygame
import random
from resources.PyCode.config import *
from resources.PyCode.utilities import *
from resources.main_menu import MainMenu
import subprocess
Tile_Size = 64

# Initialize Pygame
pygame.init()

# Set up the display
screen_info = pygame.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Guild Card Game")







# Function to start the server in a separate thread
def start_server():
    global server_process
    server_process = subprocess.Popen(['python', app_path('resources/PyCode/server.py')])
    server_on = True

# Function to start the client in a separate thread
def start_client():
    global client_process
    client_process = subprocess.Popen(['python', app_path('resources/PyCode/client.py')])
    client_on = True

def kill_client():
    client_process.kill()

def kill_server():
    server_process.kill()
def launch():
   
 
    mainMenu = MainMenu(screen,screen_width,screen_height)
    process = mainMenu.main_menu()
    if(process):
        start_client()
        while(client_process.poll() is None):
            continue
        launch()
    else:
        start_server()
        start_client()
        while(server_process.poll() is None):
            continue
        launch()
    
    # Game.start_game()
    # Game.roll_dice()



    pass





launch()


    