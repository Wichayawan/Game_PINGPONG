import pygame
from config import *

class Ball(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)

        self.image = pygame.transform.scale(self.image,
                                            (BALL_WIDTH, BALL_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = [0, 0]

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.speed[1] = -self.speed[1]