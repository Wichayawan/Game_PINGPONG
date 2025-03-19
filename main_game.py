import pygame
import sys
from config import *
from ball import Ball
from paddle import Paddle
import random

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
my_ball = Ball('images/moo.png', (400, 300))
paddle = Paddle((400, 550))

font = pygame.font.Font('Bouncy-Black-PERSONAL_USE_ONLY.otf', 80)
score_font = pygame.font.Font('KOMIKAX_.ttf', 30)
score_surface = font.render('Score: 0', True, (200, 255, 200))
text_surface = font.render('Moo Deng', True, (255, 255, 255))

background_image = pygame.image.load("images/background.png")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH,
                                                            SCREEN_HEIGHT))
background_image.set_alpha(128+64)
lives = 3
score = 0
ball_small_image = pygame.transform.scale(my_ball.image, (30, 30))

bar_surface = pygame.surface.Surface((SCREEN_HEIGHT, 80))
bar_surface.fill((0, 128, 0))
bar_surface.set_alpha(128)

def animate():
    screen.fill((255, 255, 255))
    screen.blit(background_image, (0, 0))
    screen.blit(bar_surface, (0, 0))
    screen.blit(paddle.image, paddle.rect)
    screen.blit(score_surface, (0, 0))
    screen.blit(my_ball.image, my_ball.rect)
    screen.blit(text_surface, (200, 60))
    
    pygame.display.flip()

running = True

x = random.randint(0, SCREEN_WIDTH - my_ball.rect.width)
y = random.randint(0, SCREEN_HEIGHT - my_ball.rect.height)
x = min(x, 10)
y = min(y, 10)
my_ball.speed = [x, y]

bllGroup = pygame.sprite.Group(my_ball)
bllGroup.add(my_ball)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            paddle.rect.centerx = event.pos[0]
    if pygame.sprite.spritecollide(paddle, bllGroup, False):
        my_ball.speed[1] = -my_ball.speed[1]
        score += 1
        
    #rgb(145, 221, 207)
    animate()
    my_ball.move()
    clock.tick(30)

pygame.quit()
sys.exit()
