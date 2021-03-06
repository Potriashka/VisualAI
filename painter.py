import pygame, sys
from pygame.locals import *
import requests
import re
import pyrebase

config = {
    "apiKey": "AIzaSyAsickaqxGF3TLmQ5Z9YYXm66MbpmM2CD4",
    "authDomain": "image-storer-948f7.firebaseapp.com",
    "databaseURL": "https://image-storer-948f7.firebaseio.com",
    "projectId": "image-storer-948f7",
    "storageBucket": "image-storer-948f7.appspot.com",
    "messagingSenderId": "783186859731",
    "appId": "1:783186859731:web:9a33964ddf11b4fb5e6626",
    "measurementId": "G-E3NYZ71QLR"
}

pygame.init()
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

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
        path_on_cloud = "images/foo.jpg"
        storage.child(path_on_cloud).download("test_download.jpg")
        Img = pygame.image.load('test_download.jpg')

    elif inp == '2':
        path_on_cloud = "images/Y6vdnJ.jpg"
        storage.child(path_on_cloud).download("test_download2.jpg")
        Img = pygame.image.load('test_download2.jpg')
        path_on_cloud = "images/cat.jpeg"
        storage.child(path_on_cloud).download("test_download3.jpg")
        img2 = pygame.image.load('test_download3.jpg')
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
