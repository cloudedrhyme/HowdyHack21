import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,rectobj):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((139, 129, 0))
        self.rect = rectobj
    def center(self):
        return self.rect.center
    def centerx(self):
        return self.rect.centerx
    def centery(self):
        return self.rect.centery
    def move_ip(self,x,y):
        self.rect.move_ip(x,y)
