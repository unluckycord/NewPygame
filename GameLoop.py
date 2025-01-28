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
    testCard = Card.Card("4s",400,400, None)
    while run:
        nowDraw = pygame.time.get_ticks()
        mouseInput = pygame.mouse.get_pressed()
        if mouseInput == (1, 0, 0) and (nowDraw - currentTick  >= 2000):
            renderCheck = True
            currentTick = nowDraw
        else:
            renderCheck = False
        #print("current tick = ", currentTick, "now draw = ", nowDraw, "difference check = ", nowDraw - currentTick)
        PaintGame.drawWindow(renderCheck, testCard)
        keysPressed = pygame.key.get_pressed()
        currentTime = time.time()
        deltaTime = currentTime - prevTime
        prevTime = currentTime
        
        mousex, mousey = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            #checks for click, does not work outside of loop
            pass
        pygame.display.update()
        
    pygame.quit()