import pygame, sys
from pygame.locals import *

pygame.init()

start = False

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

inp = input("")

num = ['1', '2']

if inp.lower() in num:
    start = True

while start: # the main game loop

    DISPLAYSURF = pygame.display.set_mode((700, 700), 0, 32)
    pygame.display.set_caption('Animation')

    WHITE = (255, 255, 255)

    posx = 0
    posy = 0

    DISPLAYSURF.fill(WHITE)

    if inp == '1':
        Img = pygame.image.load('jex.jpg')

    elif inp == '2':
        Img = pygame.image.load('ex2.jpg')
        img2 = pygame.image.load('jap.png')
        posx2 = 280
        posy2 = 550


    DISPLAYSURF.blit(Img, (posx, posy))
    if inp == '2':
        DISPLAYSURF.blit(img2, (posx2, posy2))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)