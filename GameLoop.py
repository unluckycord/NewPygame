from array import *
from random import choice, randint
import pygame,Assets,math,time,PaintGame,Card,DealCards,ListOfCards

def start():
    prevTime = time.time()
    deltaTime = 0
    clock = pygame.time.Clock()
    run = True
    currentTick = pygame.time.get_ticks()
    renderCheck,grabCheck = False,False
    DealCards.shuffle()
    currentCard = DealCards.drawCardFromDeck()

    testCard = Card.Card(currentCard,400,400, None, "UP")
    ListOfCards.cardStackOject.clear()
    
    mousex,mousey = pygame.mouse.get_pos()
    mouseRect = pygame.Rect(mousex,mousey,20,20)

    cardStackLocationX,cardStackLocationY = 440*Assets.scalingVal, 30*Assets.scalingVal
    offset = 190*Assets.scalingVal
    stackList = []
    for i in range(4):
        stackList.append(pygame.Rect(cardStackLocationX+offset*i,cardStackLocationY, Assets.CARDWIDTH,Assets.CARDHEIGHT))

    drawnFromDeckCardloctionx, drawnFromDeckCardloctiony = 220*Assets.scalingVal,30*Assets.scalingVal
    cardLocationRect = pygame.Rect(drawnFromDeckCardloctionx,drawnFromDeckCardloctiony, Assets.CARDWIDTH,Assets.CARDHEIGHT)

    tableauCardlocationx,tableauCardlocationy = -180*Assets.scalingVal,350*Assets.scalingVal
    tabeauCardRectList = [[]for i in range(8)]
    for i in range(8):
        for f in range(i):
            ListOfCards.tableau[i].append(ListOfCards.listOfActiveCards[0])
            ListOfCards.tableauObj[i].append(Card.Card(ListOfCards.listOfActiveCards[0], tableauCardlocationx+(250*Assets.scalingVal*i),tableauCardlocationy+(50*f), None, "DOWN"))
            tabeauCardRectList[i].append(pygame.Rect(tableauCardlocationx+(250*Assets.scalingVal*i),tableauCardlocationy+(50*f),Assets.CARDWIDTH,Assets.CARDHEIGHT))
            ListOfCards.listOfActiveCards.pop(0)

    for i in range(len(ListOfCards.listOfActiveCards)):
        ListOfCards.cardStackOject.append(Card.Card(ListOfCards.listOfActiveCards[i], 400,400, None, "DOWN"))

    while run:
        keysPressed = pygame.key.get_pressed()
        currentTime = time.time()
        deltaTime = currentTime - prevTime
        prevTime = currentTime
        mousex, mousey = pygame.mouse.get_pos()
        mouseRect.x,mouseRect.y = mousex-5,mousey-5
        nowDraw = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            mouseInput = pygame.mouse.get_pressed()
        if mouseInput == (0, 0, 1) and nowDraw - currentTick  >= 200 and pygame.Rect.colliderect(mouseRect,cardLocationRect):
            for i in range(10):
                cardLocationRect.x-=22*(deltaTime*Assets.TARGETFPS)*Assets.scalingVal
                cardLocationRect.y-=22*(deltaTime*Assets.TARGETFPS)*Assets.scalingVal
            Assets.cardFlick.play()
            for i in range(10):
                cardLocationRect.x+=22*(deltaTime*Assets.TARGETFPS)*Assets.scalingVal
                cardLocationRect.y+=22*(deltaTime*Assets.TARGETFPS)*Assets.scalingVal
            currentCard = DealCards.drawCardFromDeck()
            flipCardCheck = True
            currentTick = nowDraw
        else:
            flipCardCheck = False
        for i in range(len(tabeauCardRectList)):
            for f in range(len(tabeauCardRectList[i])):
                if mouseInput == (1,0,0) and pygame.Rect.colliderect(tabeauCardRectList[i][f], mouseRect) and ListOfCards.tableauObj[i][f].cardUpOrDown == "UP":
                    currentCardTableau = tabeauCardRectList[i][f]
                    print(True)
                    ListOfCards.tableauObj[i][f].cardlocationx = mousex-Assets.CARDWIDTH//2
                    ListOfCards.tableauObj[i][f].cardlocationy = mousey-Assets.CARDHEIGHT//2
                    currentCardTableau.x = mousex-Assets.CARDWIDTH//2
                    currentCardTableau.y = mousey-Assets.CARDHEIGHT//2
                    grabCheck = True
                else:
                    grabCheck = False
        PaintGame.drawWindow(flipCardCheck,grabCheck, testCard, currentCard,mouseRect,cardLocationRect,stackList)
        pygame.display.update()
    pygame.quit()