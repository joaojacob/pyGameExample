import pygame
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((600,600))
screen.fill((0,0,0))
pygame.display.set_caption('tela')


clock = pygame.time.Clock()

while True:
    
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    


    screen.fill((255,0,0))
    pygame.display.update()