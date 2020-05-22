import pygame
from pygame.locals import *
import random

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('robot')

def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10*10, y//10 *10)

def collision (c1,c2):
    return (c1[0]== c2[0]) and (c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


robotX, robotY = on_grid_random()
pos = (robotX, robotY)
robot_skin = pygame.Surface((10,10))
robot_skin.fill((255,255,255))

apple = pygame.Surface((10,10))
apple.fill((255,0,0))
apple_pos= (on_grid_random())


my_direction = LEFT

clock = pygame.time.Clock()


while True:
    
    clock.tick(20)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_RIGHT:
                my_direction = RIGHT
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT

    if my_direction == UP:
        robotX = robotX
        robotY = robotY - 10

    if my_direction == RIGHT:
        robotX = robotX + 10
        robotY = robotY

    if my_direction == DOWN:
        robotX = robotX
        robotY = robotY + 10

    if my_direction == LEFT:
        robotX = robotX - 10
        robotY = robotY

    pos = (robotX,robotY)

    #for i in range(len(robot)-1,0,-1):
    #    robot[i] = (robot[i-1][0], robot[i-1][1])

    #robotX = robotX 
    #robotY = robotY

    my_direction = ''

    screen.fill((0,0,0))
    screen.blit(robot_skin,pos)
    #if collision(robot[0],apple_pos):
    #    apple_pos = on_grid_random()
    #    robot.append((0,0))

    
    screen.blit(apple,apple_pos)

    #for pos in robot:
    #    screen.blit(robot_skin,pos)

    pygame.display.update()

