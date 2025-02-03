from array import *
from random import choice, randint
import pygame,Assets,math,time,PaintGame,Card,DealCards,ListOfCards

def start():
    prevTime = time.time()
    deltaTime = 0
    clock = pygame.time.Clock()
    run = True
    currentTick = pygame.time.get_ticks()
    renderCheck = False
    DealCards.shuffle()
    currentCard = DealCards.drawCardFromDeck()
    testCard = Card.Card(currentCard,400,400, None, "UP")
    ListOfCards.cardStackOject.clear()
    for i in range(8):
        for f in range(i):
            ListOfCards.tableau[i].append(ListOfCards.listOfActiveCards[0])
            ListOfCards.tableauObj[i].append(Card.Card(ListOfCards.listOfActiveCards[0], 400,400, None, "DOWN"))
            ListOfCards.tableauText[i].append(ListOfCards.listOfActiveCards[0])
            ListOfCards.listOfActiveCards.pop(0)
    for i in range(len(ListOfCards.listOfActiveCards)):
        ListOfCards.cardStackOject.append(Card.Card(ListOfCards.listOfActiveCards[i], 400,400, None, "DOWN"))

    while run:
        print(ListOfCards.tableauText)
        #print(len(ListOfCards.tableauObj))
        nowDraw = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            mouseInput = pygame.mouse.get_pressed()
        if mouseInput == (1, 0, 0) and (nowDraw - currentTick  >= 300):
            currentCard = DealCards.drawCardFromDeck()
            renderCheck = True
            currentTick = nowDraw
        else:
            renderCheck = False
        PaintGame.drawWindow(renderCheck, testCard, currentCard)
        keysPressed = pygame.key.get_pressed()
        currentTime = time.time()
        deltaTime = currentTime - prevTime
        prevTime = currentTime
        
        mousex, mousey = pygame.mouse.get_pos()
        
        pygame.display.update()
        
    pygame.quit()