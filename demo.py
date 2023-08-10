import pyautogui
import random
import time

for i in range (1000000):
    x = random.randint(250,590)
    y = random.randint(250,590)
    pyautogui.moveTo(x,y)
    for z in range(100):
        pyautogui.moveTo(x+z,y+z)
    time.sleep(15)