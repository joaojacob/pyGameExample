import pygame
from pygame.locals import *
import simple-pygame-menu


red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

menu_data = (
    'Main',
    'Item 0',
    'Item 1',
    (
        'Things',
        'Item 0',
        'Item 1',
        'Item 2',
        (
            'More Things',
            'Item 0',
            'Item 1',
        ),
    ),
    'Quit',
)
PopupMenu(menu_data)
for e in pygame.event.get():
    if e.type == USEREVENT and e.code == 'MENU':
        print('menu event: %s.%d: %s' % (e.name,e.item_id,e.text))
        if (e.name,e.text) == ('Main','Quit'):
            quit()