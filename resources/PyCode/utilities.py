
import os,sys
import socket
import pygame
import math

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
 

class SinusoidalSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, amplitude, frequency,SCREEN_HEIGHT):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)  # Start in the middle of the screen
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.amplitude = amplitude
        self.frequency = frequency
        self.angle = 0

    def update(self):
        self.rect.y = self.rect.y // 2 + int(self.amplitude * math.sin(self.angle))
        self.angle += self.frequency


def quick_sort(l):
    if len(l) <= 1:
        return l
    else:
        return quick_sort([e for e in l[1:] if e <= l[0]]) + [l[0]] +\
            quick_sort([e for e in l[1:] if e > l[0]])

def kill_player_card(player):
    pass