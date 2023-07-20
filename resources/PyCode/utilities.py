import pygame
import os,sys
import socket
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
