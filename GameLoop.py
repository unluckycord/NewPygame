from array import *
from random import choice, randint
import pygame,Assets,math,time,PaintGame,Card,DealCards,ListOfCards

def start():
    prevTime = time.time()
    deltaTime = 0
    clock = pygame.time.Clock()
    run = True
    currentTickDrawCard,currentTickAnimation = pygame.time.get_ticks(),pygame.time.get_ticks()
    renderCheck,grabCheck = False,False
    DealCards.shuffle()
    currentCard = DealCards.drawCardFromDeck()
    ListOfCards.cardStackOject.clear()
    
    mousex,mousey = pygame.mouse.get_pos()
    mouseRect = pygame.Rect(mousex,mousey,20,20)

    cardStackLocationX,cardStackLocationY = 440*Assets.scalingVal, 30*Assets.scalingVal
    offset = 190*Assets.scalingVal
    stackList = []
    for i in range(4):
        stackList.append(pygame.Rect(cardStackLocationX+offset*i,cardStackLocationY, Assets.CARDWIDTH,Assets.CARDHEIGHT))

    DrawnCard = Card.Card(currentCard,220*Assets.scalingVal,30*Assets.scalingVal, None, "UP", pygame.Rect(220*Assets.scalingVal,30*Assets.scalingVal,Assets.CARDWIDTH,Assets.CARDHEIGHT),0,0)

    pileLocationX, pileLocationY = 30*Assets.scalingVal,30*Assets.scalingVal
    pileLocationShadow = []
    for i in range (9):
        pileLocationShadow.append(pygame.Rect(pileLocationX+4+(i*-3),pileLocationY+4+(i*-3), Assets.CARDWIDTH,Assets.CARDHEIGHT))

    tableauCardlocationx,tableauCardlocationy = -180*Assets.scalingVal,350*Assets.scalingVal
    for i in range(8):
        for f in range(i):
            ListOfCards.tableauObj[i].append(Card.Card(ListOfCards.listOfActiveCards[0], tableauCardlocationx+(250*Assets.scalingVal*i),tableauCardlocationy+(50*f), None, "DOWN", pygame.Rect(tableauCardlocationx+(250*Assets.scalingVal*i),tableauCardlocationy+(50*f),Assets.CARDWIDTH,Assets.CARDHEIGHT),i,f))
            ListOfCards.listOfActiveCards.pop(0)

    for i in range(len(ListOfCards.listOfActiveCards)):
        ListOfCards.cardStackOject.append(Card.Card(ListOfCards.listOfActiveCards[i], 30*Assets.scalingVal,30*Assets.scalingVal, None, "DOWN", pygame.Rect(30*Assets.scalingVal,30*Assets.scalingVal,Assets.CARDWIDTH,Assets.CARDHEIGHT),0,0))

    currentCardTableau = None
    prevCard = None

    while run:
        keysPressed = pygame.key.get_pressed()
        currentTime = time.time()
        deltaTime = currentTime - prevTime
        prevTime = currentTime
        mousex, mousey = pygame.mouse.get_pos()
        mouseRect.x,mouseRect.y = mousex-5,mousey-5
        nowDraw,nowAnimate = pygame.time.get_ticks(),pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            mouseInput = pygame.mouse.get_pressed()
        if mouseInput == (0, 0, 1) and nowDraw - currentTickDrawCard  >= 200 and pygame.Rect.colliderect(mouseRect,DrawnCard.cardRect):
            for i in range(100):
                #if(nowAnimate - currentTickAnimation >=10):
                DrawnCard.cardlocationx-=22*(deltaTime*Assets.TARGETFPS)*Assets.scalingVal
                DrawnCard.cardlocationy-=3*(deltaTime*Assets.TARGETFPS)*Assets.scalingVal
                #currentTickAnimation = nowAnimate
            Assets.cardFlick.play()
            for i in range(100):
                #if(nowAnimate - currentTickAnimation >=10):
                DrawnCard.cardlocationx+=22*(deltaTime*Assets.TARGETFPS)*Assets.scalingVal
                DrawnCard.cardlocationy+=3*(deltaTime*Assets.TARGETFPS)*Assets.scalingVal
                #currentTickAnimation = nowAnimate
            currentCard = DealCards.drawCardFromDeck()
            flipCardCheck = True
            currentTickDrawCard = nowDraw
        else:
            flipCardCheck = False
            
        for i in range(len(ListOfCards.tableauObj)):
            for f in range(len(ListOfCards.tableauObj[i])):
                print(ListOfCards.tableauObj[i][f].col,ListOfCards.tableauObj[i][f].row)
                if mouseInput == (1,0,0) and pygame.Rect.colliderect(ListOfCards.tableauObj[i][f].cardRect, mouseRect) and ListOfCards.tableauObj[i][f].cardUpOrDown == "UP":
                    currentCardTableau = ListOfCards.tableauObj[i][f]
                    if(prevCard == None):
                        prevCard = ListOfCards.tableauObj[i][f]
                    grabCheck = True
                    if(currentCardTableau.rank+1 == prevCard.rank):
                        print("yes")
                        currentCardTableau.cardRect.x, currentCardTableau.cardRect.y = prevCard.cardRect.x, prevCard.cardRect.y+50
                        #ListOfCards.tableauObj[currentCardTableau.col].pop(currentCardTableau.row)
                        #ListOfCards.tableauObj[prevCard.col].append(currentCardTableau)
                        prevCard = None
                        currentCard = None
                else:
                    pass
                    #grabCheck = False
        PaintGame.drawWindow(flipCardCheck,grabCheck, DrawnCard, currentCard,mouseRect,DrawnCard.cardRect,stackList,currentCardTableau,pileLocationShadow)
        pygame.display.update()
    pygame.quit()