from array import *
from random import choice, randint
import pygame,Assets,math,time,PaintGame,Card

def start():
    prevTime = time.time()
    deltaTime = 0
    clock = pygame.time.Clock()
    run = True
    
    while run:
        PaintGame.drawWindow()
        keysPressed = pygame.key.get_pressed()
        currentTime = time.time()
        deltaTime = currentTime - prevTime
        prevTime = currentTime
        
        mousex, mousey = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        mouseInput = pygame.mouse.get_pressed()
        if mouseInput == (1, 0, 0):
            #checks for click, does not work outside of loop
            pass
        pygame.display.update()
        
    pygame.quit()