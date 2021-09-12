import pygame
import os

class Player(pygame.sprite.Sprite):
    def __init__(self,rectobj):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.image.load(os.path.join('rev1.png'))
        self.images = []
        self.images.append(pygame.image.load(os.path.join('rev1.png')))
        self.images.append(pygame.image.load(os.path.join('rev2-4.png')))
       # self.image = pygame.Surface((50, 50))
       # self.image.fill((139, 129, 0))
        self.rect = rectobj
        self.index = 0
        self.image = self.images[self.index]

    def update(self):
        self.index += 1
        pygame.time.wait(100)
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
    def center(self):
        return self.rect.center
    def centerx(self):
        return self.rect.centerx
    def centery(self):
        return self.rect.centery
    def move_ip(self,x,y):
        self.rect.move_ip(x,y)
