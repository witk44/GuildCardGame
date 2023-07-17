import pygame
import os,sys
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