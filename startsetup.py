import pygame
from pygame.locals import *
import sys;

#test window size
displaysurface = pygame.display.set_mode((300, 300))

image = pygame.Surface([640,480], pygame.SRCALPHA, 32)
image = image.convert_alpha()
 
mySurface = pygame.Surface((50, 50))
#mySurface.fill((0,255,0))
 
mySurface2 = pygame.Surface((100, 50))
mySurface2.fill((0,255,0))
 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    displaysurface.blit(mySurface, (50,50))
    displaysurface.blit(mySurface2, (50,150))
 
    pygame.display.update()