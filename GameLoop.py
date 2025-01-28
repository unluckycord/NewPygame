from array import *
from random import choice, randint
import pygame,Assets,math,time,PaintGame,Card

def start():
    prevTime = time.time()
    deltaTime = 0
    clock = pygame.time.Clock()
    run = True
    currentTick = pygame.time.get_ticks()
    renderCheck = False
    while run:
        nowDraw = pygame.time.get_ticks()
        if(nowDraw - currentTick  >= 1000):
            renderCheck = True
            currentTick = nowDraw
        else:
            renderCheck = False
        #print("current tick = ", currentTick, "now draw = ", nowDraw, "difference check = ", nowDraw - currentTick)
        PaintGame.drawWindow(renderCheck)
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