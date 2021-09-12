import pygame
import win32api
import win32con
import win32gui
import movement
from pygame import mixer  # Load the popular external library

# mixer.init()
# mixer.music.load('C:/Users/Clown/Downloads/Rick_Roll.mp3')
# mixer.music.play()


pygame.init()
flags = pygame.NOFRAME
screen = pygame.display.set_mode((0,0), flags)
x,y = pygame.display.get_window_size()
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
    
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(fuchsia)  # Transparent background
    win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,0,0,0,0,0x0001)

    rev = movement.update(rev)
    pygame.draw.rect(screen, dark_red, rev)
    pygame.display.update()