import pygame

guild_primary = (131,120,180)
guild_secondary = (248,186,139)
guild_background = (216,159,152)
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
        self.rect = self.image.get_rect(center=(int((screen_width // 2)), int(screen_height-(screen_height//4))))

        # Set the "Submit" text on the button in black
        font = pygame.font.Font(None, 18)
        text_surface = font.render("Start Game", True, guild_secondary)
        text_rect = text_surface.get_rect(center=self.image.get_rect().center)
        self.image.blit(text_surface, text_rect)

class CopyButton(pygame.sprite.Sprite):
    def __init__(self,screen_width,screen_height):
        super().__init__()
        width = 30
        height = 30
        
        self.image = pygame.Surface((width, height))
        self.image.fill(guild_primary)
        self.rect = self.image.get_rect(center=(int((screen_width -90)), int(screen_height // 2 - 50)))

        # Set the "Submit" text on the button in black
        font = pygame.font.Font(None, 18)
        text_surface = font.render("Start Game", True, guild_secondary)
        text_rect = text_surface.get_rect(center=self.image.get_rect().center)
        self.image.blit(text_surface, text_rect)