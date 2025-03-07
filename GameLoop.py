from array import *
from random import choice, randint
import pygame,Assets,math,time,PaintGame,Card,DealCards,ListOfCards

def cardMove(currentCard,prevCard):
    print("passed")
    #the great card migration
    if(currentCard.isStackedInDeck):
        ListOfCards.tableauObj[prevCard.col].append(ListOfCards.cardStackOject[0])
        ListOfCards.tableauObj[prevCard.col][prevCard.row].cardStack.append(prevCard)
        ListOfCards.tableauObj[prevCard.col][prevCard.row].cardStack.append(currentCard)
        ListOfCards.tableauObj[prevCard.col][prevCard.row].isStacked = True
        ListOfCards.cardStackOject[0].cardRect.x, ListOfCards.cardStackOject[0].cardRect.y = prevCard.cardRect.x, prevCard.cardRect.y+50
        ListOfCards.cardStackOject.pop(0)
        DealCards.drawCardFromDeck()
        ListOfCards.tableauObj[prevCard.col][len(ListOfCards.tableauObj[prevCard.col])-1].row = len(ListOfCards.tableauObj[prevCard.col])-1
        ListOfCards.tableauObj[prevCard.col][currentCard.row].col = prevCard.col
        ListOfCards.tableauObj[currentCard.col][currentCard.row].cardUpOrDown = "UP"
    if(currentCard.isStacked):
        ListOfCards.tableauObj[prevCard.col][prevCard.row].cardStack.append(prevCard)
        ListOfCards.tableauObj[prevCard.col][prevCard.row].isStacked = True
        ListOfCards.tableauObj[currentCard.col][currentCard.row-1].cardUpOrDown="UP"
        for i in range(len(currentCard.cardStack)):
            ListOfCards.tableauObj[prevCard.col].append(currentCard.cardStack[i])
            ListOfCards.tableauObj[prevCard.col][prevCard.row].cardStack.append(currentCard.cardStack[i])
            ListOfCards.tableauObj[prevCard.col][prevCard.row+i].isStacked = True
            currentCard.cardStack[i].cardRect.x, currentCard.cardStack[i].cardRect.y = prevCard.cardRect.x, prevCard.cardRect.y+50
            ListOfCards.tableauObj[currentCard.col].pop(currentCard.row+i)
            ListOfCards.tableauObj[prevCard.col][len(ListOfCards.tableauObj[prevCard.col])-1].row = len(ListOfCards.tableauObj[prevCard.col])-1
            ListOfCards.tableauObj[prevCard.col][currentCard.row].col = prevCard.col
    else:
        ListOfCards.tableauObj[prevCard.col].append(currentCard)
        ListOfCards.tableauObj[prevCard.col][prevCard.row].cardStack.append(prevCard)
        ListOfCards.tableauObj[prevCard.col][prevCard.row].cardStack.append(currentCard)
        ListOfCards.tableauObj[prevCard.col][prevCard.row].isStacked = True
        ListOfCards.tableauObj[currentCard.col][currentCard.row-1].cardUpOrDown="UP"
        currentCard.cardRect.x, currentCard.cardRect.y = prevCard.cardRect.x, prevCard.cardRect.y+50
        ListOfCards.tableauObj[currentCard.col].pop(currentCard.row)
        ListOfCards.tableauObj[prevCard.col][len(ListOfCards.tableauObj[prevCard.col])-1].row = len(ListOfCards.tableauObj[prevCard.col])-1
        ListOfCards.tableauObj[prevCard.col][currentCard.row].col = prevCard.col

def removeCardsInObjective(grabCheck,currentCard,prevCard):
    #for some reason, removing cards from deck causes index error
    for i in range(len(ListOfCards.cardStackOject)):
        if(ListOfCards.cardStackOject[i].cardInObjective == True):
            DealCards.drawCardFromDeck()
            currentCard = None
            prevCard = None
            grabCheck = False
            ListOfCards.cardStackOject.pop(i)
    for i in range(len(ListOfCards.tableauObj)):
        for f in range(len(ListOfCards.tableauObj[i])):
            if(ListOfCards.tableauObj[i][f].cardInObjective == True):
                currentCard = None
                prevCard = None
                grabCheck = False
                if(f > 0):
                    ListOfCards.tableauObj[i][f-1].cardUpOrDown = "UP"
                ListOfCards.tableauObj[i].pop(f)

def start():
    prevTime = time.time()
    deltaTime = 0
    clock = pygame.time.Clock()
    run = True
    currentTickDrawCard,currentTickAnimation = pygame.time.get_ticks(),pygame.time.get_ticks()
    renderCheck,grabCheck = False,False
    DealCards.shuffle()
    ListOfCards.cardStackOject.clear()
    
    mousex,mousey = pygame.mouse.get_pos()
    mouseRect = pygame.Rect(mousex,mousey,20,20)

    pileLocationX, pileLocationY = 30*Assets.scalingVal,30*Assets.scalingVal
    pileLocationShadow = []
    #the pile shadow
    for i in range (9):
        pileLocationShadow.append(pygame.Rect(pileLocationX+4+(i*-3),pileLocationY+4+(i*-3), Assets.CARDWIDTH,Assets.CARDHEIGHT))

    #the tableau
    tableauCardlocationx,tableauCardlocationy = -180*Assets.scalingVal,350*Assets.scalingVal
    for i in range(8):
        for f in range(i):
            if(f+1<i):
                ListOfCards.tableauObj[i].append(Card.Card(ListOfCards.listOfActiveCards[0], "DOWN", pygame.Rect(tableauCardlocationx+(250*Assets.scalingVal*i),tableauCardlocationy+(50*f),Assets.CARDWIDTH,Assets.CARDHEIGHT),i-1,f))
            else:
                ListOfCards.tableauObj[i].append(Card.Card(ListOfCards.listOfActiveCards[0], "UP", pygame.Rect(tableauCardlocationx+(250*Assets.scalingVal*i),tableauCardlocationy+(50*f),Assets.CARDWIDTH,Assets.CARDHEIGHT),i-1,f))
            ListOfCards.tableauObj[i][f].isStackedInDeck=False
            ListOfCards.listOfActiveCards.pop(0)
    
    #where cards are stacked
    cardStackLocationX,cardStackLocationY = 440*Assets.scalingVal, 30*Assets.scalingVal
    offset = 190*Assets.scalingVal
    stackList = []
    for i in range(4):
        stackList.append(pygame.Rect(cardStackLocationX+offset*i,cardStackLocationY, Assets.CARDWIDTH,Assets.CARDHEIGHT))

    #the cards remaining within deck
    for i in range(len(ListOfCards.listOfActiveCards)):
        ListOfCards.cardStackOject.append(Card.Card(ListOfCards.listOfActiveCards[i], "DOWN", pygame.Rect(30*Assets.scalingVal,30*Assets.scalingVal,Assets.CARDWIDTH,Assets.CARDHEIGHT),0,0))
    ListOfCards.cardStackOject[0].cardRect = pygame.Rect(220*Assets.scalingVal,30*Assets.scalingVal,Assets.CARDWIDTH,Assets.CARDHEIGHT)
    ListOfCards.cardStackOject[0].cardUpOrDown = "UP"

    currentCard = None
    prevCard = None
    grabCheck = False

    #python is silly, so I had to remove an extra array, that, or I am stupid
    ListOfCards.tableauObj.pop(0)

    while run:
        keysPressed = pygame.key.get_pressed()
        currentTime = time.time()
        deltaTime = currentTime - prevTime
        prevTime = currentTime
        mousex, mousey = pygame.mouse.get_pos()
        mouseRect.x,mouseRect.y = mousex-5,mousey-5
        nowDraw,nowAnimate = pygame.time.get_ticks(),pygame.time.get_ticks()
        removeCardsInObjective(grabCheck,currentCard,prevCard)
        #|--------------------------------------------------------------------------------|
        #|Starting from here, everthing is related to button presses and moving the cards|
        #|------------------------------------------------------------------------------|
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            mouseInput = pygame.mouse.get_pressed()

        if keysPressed[pygame.K_c] and (prevCard != None or currentCard != None):
            grabCheck = False
            prevCard = None
            currentCard = None
        #cycling cards
        if mouseInput == (0, 0, 1) and nowDraw - currentTickDrawCard  >= 200 and pygame.Rect.colliderect(mouseRect,ListOfCards.cardStackOject[0].cardRect):
            ListOfCards.cardStackOject[0].cardlocationx-=22*Assets.scalingVal
            ListOfCards.cardStackOject[0].cardlocationy-=3*Assets.scalingVal
            currentTickAnimation = nowAnimate
            Assets.cardFlick.play()
            ListOfCards.cardStackOject[0].cardlocationx+=22*Assets.scalingVal
            ListOfCards.cardStackOject[0].cardlocationy+=3*Assets.scalingVal
            DealCards.drawCardFromDeck()
            flipCardCheck = True
            currentTickDrawCard = nowDraw
        else:
            flipCardCheck = False
        #checks for card within deck to be moved
        if mouseInput == (1,0,0) and pygame.Rect.colliderect(ListOfCards.cardStackOject[0].cardRect, mouseRect):
            currentCard = ListOfCards.cardStackOject[0]

        #scans tableau for cards to be moved
        for i in range(len(ListOfCards.tableauObj)):
            for f in range(len(ListOfCards.tableauObj[i])):
                if mouseInput == (1,0,0) and pygame.Rect.colliderect(ListOfCards.tableauObj[i][f].cardRect, mouseRect) and ListOfCards.tableauObj[i][f].cardUpOrDown == "UP":
                    currentCard = ListOfCards.tableauObj[i][f]
                    if(prevCard == None):
                        prevCard = ListOfCards.tableauObj[i][f]
                    grabCheck = True
        #movement for cards, regardless of deck or tableau
        if(prevCard!=None and currentCard!=None):
            if(prevCard.isStacked == False and currentCard.rank+1 == prevCard.rank and currentCard.colorIndex != prevCard.colorIndex):
                cardMove(currentCard,prevCard)
                Assets.cardFlick.play()
                grabCheck = False
                prevCard = None
                currentCard = None
        if currentCard!=None:
            for i in range(4):
                if mouseInput == (1,0,0) and pygame.Rect.colliderect(stackList[i],mouseRect):
                    if len(ListOfCards.listOfCardsInObjective[i]) == 0 and currentCard.rank == 1:
                        ListOfCards.listOfCardsInObjective[i].append(Card.Card(currentCard.rankandsuit, "UP", stackList[i], None,None))
                        currentCard.cardInObjective = True
                    elif(len(ListOfCards.listOfCardsInObjective[i])!=0 and currentCard.rank == ListOfCards.listOfCardsInObjective[i][len(ListOfCards.listOfCardsInObjective[i])-1].rank+1) and currentCard.suit == ListOfCards.listOfCardsInObjective[i][len(ListOfCards.listOfCardsInObjective[i])-1].suit :
                        ListOfCards.listOfCardsInObjective[i].append(Card.Card(currentCard.rankandsuit, "UP", stackList[i], None,None))
                        currentCard.cardInObjective = True
        PaintGame.drawWindow(flipCardCheck,grabCheck,mouseRect,stackList,currentCard,pileLocationShadow)
        pygame.display.update()
    pygame.quit()