import pygame
import os,sys
import socket
guild_primary = (131,120,180)
guild_secondary = (248,186,139)
guild_background = (216,159,152)
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128,128,128)
def app_path(path):
    frozen = 'not'
    if getattr(sys, 'frozen', False):
            # we are running in executable mode
            frozen = 'ever so'
            app_dir = sys._MEIPASS
            return os.path.join(app_dir, path)
    else:
            # we are running in a normal Python environment
            return path
    
def find_open_port():
    with socket.socket() as s:
        s.bind(('', 0))            # Bind to a free port provided by the host.
        return s.getsockname()[1]  # Return the port number assigned.
 # Create a submit button
class SubmitButton(pygame.sprite.Sprite):
    def __init__(self,screen_width,screen_height):
        
       super().__init__()
       width = 90
       height = 45
       
       self.image = pygame.Surface((width, height))
       self.image.fill(guild_primary)
       self.rect = self.image.get_rect(center=(int((screen_width // 2)), int(screen_height-(height//2))))

       # Set the "Submit" text on the button in black
       font = pygame.font.Font(None, 18)
       text_surface = font.render("Submit", True, guild_secondary)
       text_rect = text_surface.get_rect(center=self.image.get_rect().center)
       self.image.blit(text_surface, text_rect)

class StartGameButton(pygame.sprite.Sprite):
    def __init__(self,screen_width,screen_height):
        super().__init__()
        width = 90
        height = 45
        
        self.image = pygame.Surface((width, height))
        self.image.fill(guild_primary)
        self.rect = self.image.get_rect(center=(int((screen_width // 2)), int(screen_height-(height//2))))

        # Set the "Submit" text on the button in black
        font = pygame.font.Font(None, 18)
        text_surface = font.render("Start Game", True, guild_secondary)
        text_rect = text_surface.get_rect(center=self.image.get_rect().center)
        self.image.blit(text_surface, text_rect)

