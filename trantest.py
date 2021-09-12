import pygame
import win32api
import win32con
import win32gui
import movement
import random
from pygame import mixer  # Load the popular external library
# mixer.init()
# mixer.music.load('C:/Users/Clown/Downloads/Rick_Roll.mp3')
# mixer.music.play()
pygame.init()
flags = pygame.NOFRAME
screen = pygame.display.set_mode((0,0), flags)
x,y = pygame.display.get_window_size()
pointarr = movement.init(x,y)
goal = list(random.choice(pointarr))
done = False
fuchsia = (255, 0, 128)  # Transparency color
dark_red = (139, 0, 0)
# Create layered window
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
# Set window transparency color
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)
rev = pygame.draw.rect(screen, dark_red, pygame.Rect(30, 30, 60, 60))
revbox = pygame.draw.rect(screen, dark_red, pygame.Rect(x-120,y-120, 60,30))
revboxVal = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:#Add something for touching reveille
            if revbox.collidepoint(event.pos):
                revboxVal = True
        elif event.type == pygame.MOUSEBUTTONUP:
            revboxVal = False
        if event.type == pygame.QUIT:
            done = True
    screen.fill(fuchsia)  # Transparent background
    #rev = movement.update(rev)
    pygame.draw.rect(screen, dark_red, rev)
    pygame.display.update()