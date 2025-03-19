import pygame
from config import *

class Paddle(pygame.sprite.Sprite):
    def __init__(self, location = [0, 0]):
        pygame.sprite.Sprite.__init__(self)
        surface_image = pygame.surface.Surface((PADDLE_WIDTH,
                                                PADDLE_HEIGHT))
        #rgb(146, 26, 64)
        surface_image.fill((146, 26, 64))
        self.image = surface_image
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = 0