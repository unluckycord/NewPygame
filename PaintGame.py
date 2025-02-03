from time import sleep
import pygame,Assets,random,Card,DealCards,ListOfCards
def drawMouseBox(mouseRect):
    
    pygame.draw.rect(Assets.WIN, Assets.WHITE, mouseRect)

def drawDeckOfCards(stackLocationX, stackLocationY):
    for i in range (9):
        pygame.draw.rect(Assets.WIN, Assets.BLACK, (stackLocationX+4+(i*-3),stackLocationY+4+(i*-3), Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
    pygame.draw.rect(Assets.WIN, Assets.WHITE, (stackLocationX+(9*-3),stackLocationY+(9*-3), Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
    Assets.WIN.blit(Assets.cardback_black, (stackLocationX+9+(9*-3),stackLocationY+11+(9*-3)))

def drawCard(cardLocationRect,card):
    #shadow
    pygame.draw.rect(Assets.WIN, Assets.BLACK, (cardLocationRect.x+(4*Assets.scalingVal),cardLocationRect.y+(4*Assets.scalingVal), Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
    #white card surface
    pygame.draw.rect(Assets.WIN, Assets.WHITE, cardLocationRect, width=0, border_radius=13)
    #card face
    Assets.WIN.blit(card, (cardLocationRect.x,cardLocationRect.y))

def drawCardStackLocation(stackList):
    for i in range(4):
        pygame.draw.rect(Assets.WIN, Assets.BLACK, (stackList[i].x,stackList[i].y, Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
        pygame.draw.rect(Assets.WIN, Assets.GREEN, (stackList[i].x+1,stackList[i].y+1, Assets.CARDWIDTH-2,Assets.CARDHEIGHT-2),width=0, border_radius=13)
    
def drawTableau(grabCheck,mouseRect):
    for i in range(len(ListOfCards.tableauObj)):
        for f in range(len(ListOfCards.tableauObj[i])):
            pygame.draw.rect(Assets.WIN, Assets.BLACK, (ListOfCards.tableauObj[i][f].cardlocationx+(4*Assets.scalingVal),ListOfCards.tableauObj[i][f].cardlocationy+(4*Assets.scalingVal), Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
            pygame.draw.rect(Assets.WIN, Assets.WHITE, (ListOfCards.tableauObj[i][f].cardlocationx,ListOfCards.tableauObj[i][f].cardlocationy, Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
            if(f+1 < i):
                Assets.WIN.blit(Assets.cardback_black, (ListOfCards.tableauObj[i][f].cardlocationx+(9*Assets.scalingVal),ListOfCards.tableauObj[i][f].cardlocationy+(11*Assets.scalingVal)))
            else:
                Assets.WIN.blit(ListOfCards.tableauObj[i][f].card, (ListOfCards.tableauObj[i][f].cardlocationx,ListOfCards.tableauObj[i][f].cardlocationy))
                ListOfCards.tableauObj[i][f].cardUpOrDown = "UP"



def drawWindow(flipCardCheck,grabCheck,activeCard,currentCard,mouseRect,cardLocationRect,stackList):
    cardloctionx, cardlocationy = 220*Assets.scalingVal,30*Assets.scalingVal
    stackLocationX, stackLocationY = 30*Assets.scalingVal,30*Assets.scalingVal
    #testCard = Card.Card(DealCards.randomRankAndSuit(),cardloctionx,cardlocationy)

    Assets.WIN.fill(Assets.GREEN)
    if flipCardCheck:
        newval= currentCard
        activeCard.setCard(newval)
        activeCard.rankandsuit=newval
    #print(testCard.rankandsuit, renderCheck)
    drawCard(cardLocationRect,activeCard.card)
    drawDeckOfCards(stackLocationX,stackLocationY)
    drawCardStackLocation(stackList)
    drawTableau(grabCheck,mouseRect)
    drawMouseBox(mouseRect)