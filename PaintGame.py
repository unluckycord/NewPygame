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
    
    #pygame.draw.rect(Assets.WIN, Assets.WHITE, (cardLocationRect.x,cardLocationRect.y, Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
    #card face
    Assets.WIN.blit(card, (cardLocationRect.x,cardLocationRect.y))

def drawCardStackLocation():
    stackLocationX,stackLocationY = 440*Assets.scalingVal, 30*Assets.scalingVal
    offset = 190*Assets.scalingVal
    pygame.draw.rect(Assets.WIN, Assets.BLACK, (stackLocationX,stackLocationY, Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
    pygame.draw.rect(Assets.WIN, Assets.GREEN, (stackLocationX+1,stackLocationY+1, Assets.CARDWIDTH-2,Assets.CARDHEIGHT-2),width=0, border_radius=13)
    pygame.draw.rect(Assets.WIN, Assets.BLACK, (stackLocationX+offset,stackLocationY, Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
    pygame.draw.rect(Assets.WIN, Assets.GREEN, (stackLocationX+offset+1,stackLocationY+1, Assets.CARDWIDTH-2,Assets.CARDHEIGHT-2),width=0, border_radius=13)
    pygame.draw.rect(Assets.WIN, Assets.BLACK, (stackLocationX+offset*2,stackLocationY, Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
    pygame.draw.rect(Assets.WIN, Assets.GREEN, (stackLocationX+offset*2+1,stackLocationY+1, Assets.CARDWIDTH-2,Assets.CARDHEIGHT-2),width=0, border_radius=13)
    pygame.draw.rect(Assets.WIN, Assets.BLACK, (stackLocationX+offset*3,stackLocationY, Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
    pygame.draw.rect(Assets.WIN, Assets.GREEN, (stackLocationX+offset*3+1,stackLocationY+1, Assets.CARDWIDTH-2,Assets.CARDHEIGHT-2),width=0, border_radius=13)

def drawTableau():
    cardlocationx,cardlocationy = -180*Assets.scalingVal,350*Assets.scalingVal
    for i in range(len(ListOfCards.tableauObj)):
        for f in range(len(ListOfCards.tableauObj[i])):
            pygame.draw.rect(Assets.WIN, Assets.BLACK, (cardlocationx+(4*Assets.scalingVal)+(250*Assets.scalingVal*i),cardlocationy+(4*Assets.scalingVal)+(50*f), Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
            pygame.draw.rect(Assets.WIN, Assets.WHITE, (cardlocationx+(250*Assets.scalingVal*i),cardlocationy+(50*f), Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
            if(f+1 < i):
                Assets.WIN.blit(Assets.cardback_black, (cardlocationx+(9*Assets.scalingVal)+(i*250*Assets.scalingVal),cardlocationy+(11*Assets.scalingVal)+(f*50)))
            else:
                Assets.WIN.blit(ListOfCards.tableauObj[i][f].card, (cardlocationx+(i*250*Assets.scalingVal),cardlocationy+(f*50)))
                ListOfCards.tableauObj[i][f].cardUpOrDown = "UP"



def drawWindow(flipCardCheck, activeCard,currentCard,mouseRect,cardLocationRect):
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
    drawCardStackLocation()
    drawTableau()
    drawMouseBox(mouseRect)