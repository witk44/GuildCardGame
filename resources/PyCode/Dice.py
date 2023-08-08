import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (255, 255, 255)
DICE_COLOR = (0, 0, 0)
FONT_SIZE = 48

# Die class
class Die:
    def __init__(self):
        self.value = 1
        self.roll_animation = False
        self.animation_frames = 20
        self.animation_frame = 0

    def roll(self):
        self.roll_animation = True
        self.animation_frame = 0

    def update(self):
        if self.roll_animation:
            if self.animation_frame < self.animation_frames:
                self.value = random.randint(1, 6)
                self.animation_frame += 1
            else:
                self.roll_animation = False

    def draw(self, surface):
        if self.roll_animation:
            # Display rolling animation
            frame_value = random.randint(1, 6)
            self._draw_number(surface, frame_value)
        else:
            # Display current value
            self._draw_number(surface, self.value)

    def _draw_number(self, surface, number):
        font = pygame.font.Font(None, FONT_SIZE)
        text = font.render(str(number), True, DICE_COLOR)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        surface.blit(text, text_rect)
    
# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dice Roller")

# Create a Die instance
die = Die()

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            die.roll()

    # Update the die and screen
    die.update()
    
    screen.fill(BACKGROUND_COLOR)
    die.draw(screen)

    pygame.display.flip()
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
