import pygame
import sys
import socket
import threading
from resources.PyCode.utilities import *
import subprocess

# Initialize Pygame
pygame.init()

class MainMenu:
    def __init__(self,screen,screen_width,screen_height) -> None:
        # Set up the display
        self.screen_width, self.screen_height = screen_width,screen_height
        self.screen = screen
        pygame.display.set_caption("Guild Card Game Main Menu")

        # Load the background image
        self.background_image = pygame.image.load(app_path("resources/images/GuildPoster.png")) 
        self.main_menu_image = pygame.image.load(app_path("resources/images/Guild_Logo_Clear.png")) 
        # Create a sprite group
        self.all_sprites = pygame.sprite.Group()
        self.main_menu_image = pygame.transform.scale(self.main_menu_image,(self.screen_width//4,self.screen_height//3))
        # Create the sinusoidal sprite
        self.sinusoidal_sprite = SinusoidalSprite(self.main_menu_image, self.screen_width//2,100, 15, 0.10,self.screen_height)
        self.all_sprites.add(self.sinusoidal_sprite)
        # Resize the background image to fit the screen
        self.background_image = pygame.transform.scale(self.background_image, (self.screen_width, screen_height))


        # Set up colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

        # Set up fonts
        self.font_title = pygame.font.Font(None, 72)
        self.font_options = pygame.font.Font(None, 48)

        self.join_text = self.font_options.render("Join Game", True, self.WHITE)
        self.host_text = self.font_options.render("Host Game", True, self.WHITE)

        self.join_text_rect = self.join_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
        self.host_text_rect = self.host_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 50))

        self.client_on, self.server_on = False, False

   
    def main_menu(self):

        # Main menu loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        
                        pygame.quit()
                        sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.join_text_rect.collidepoint(mouse_pos):
                        return True
                    elif self.host_text_rect.collidepoint(mouse_pos):
                        return False

            # Draw the background
            self.screen.fill(self.BLACK)
            # Draw the background image
            self.screen.blit(self.background_image, (0, 0))
            
            self.screen.blit(self.join_text, self.join_text_rect)
            self.screen.blit(self.host_text, self.host_text_rect)
            
            self.all_sprites.update()
            self.all_sprites.draw(self.screen)

            # Update the display
            pygame.display.flip()