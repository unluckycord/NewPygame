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
    
    
    mousex,mousey = pygame.mouse.get_pos()
    mouseRect = pygame.Rect(mousex,mousey,20,20)

    cardloctionx, cardlocationy = 220*Assets.scalingVal,30*Assets.scalingVal
    cardLocationRect = pygame.Rect(cardloctionx,cardlocationy, Assets.CARDWIDTH,Assets.CARDHEIGHT)

    for i in range(8):
        for f in range(i):
            ListOfCards.tableau[i].append(ListOfCards.listOfActiveCards[0])
            ListOfCards.tableauObj[i].append(Card.Card(ListOfCards.listOfActiveCards[0], 400,400, None, "DOWN"))
            ListOfCards.tableauText[i].append(ListOfCards.listOfActiveCards[0])
            ListOfCards.listOfActiveCards.pop(0)
    for i in range(len(ListOfCards.listOfActiveCards)):
        ListOfCards.cardStackOject.append(Card.Card(ListOfCards.listOfActiveCards[i], 400,400, None, "DOWN"))

    while run:
        
        mouseRect.x,mouseRect.y = mousex-5,mousey-5
        print(mouseRect.left,mouseRect.top)
        #print(len(ListOfCards.tableauObj))
        nowDraw = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            mouseInput = pygame.mouse.get_pressed()
        if mouseInput == (1, 0, 0) and (nowDraw - currentTick  >= 300 and pygame.Rect.colliderect(mouseRect,cardLocationRect)):
            currentCard = DealCards.drawCardFromDeck()
            flipCardCheck = True
            currentTick = nowDraw
        else:
            flipCardCheck = False
        PaintGame.drawWindow(flipCardCheck, testCard, currentCard,mouseRect,cardLocationRect)
        keysPressed = pygame.key.get_pressed()
        currentTime = time.time()
        deltaTime = currentTime - prevTime
        prevTime = currentTime
        
        mousex, mousey = pygame.mouse.get_pos()
        
        pygame.display.update()
        
    pygame.quit()