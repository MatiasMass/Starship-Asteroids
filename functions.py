import sys
import pygame
from pygame.locals import *

def terminate():
    pygame.quit()
    sys.exit()


def draw_text(text, font, surface, x, y, TEXTCOLOR):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def wait():

    waiting = True    
    
    while waiting:
        
        for event in pygame.event.get():

            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                waiting = False


def choose_starship():
    waiting = True    
    
    while waiting:
        
        for event in pygame.event.get():

            if event.type == QUIT:
                terminate()
                
            if event.type == KEYDOWN:
            
                if event.key == K_1:
                    return 1
                    waiting = False
                    break
                if event.key == K_2:
                    return 2
                    waiting = False
                    break
                if event.key == K_3:
                    return 3
                    waiting = False
                    break
