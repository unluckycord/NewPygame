from time import sleep
import pygame,Assets,random,Card,DealCards,ListOfCards
def drawMouseBox():
    pass

def drawDeckOfCards(stackLocationX, stackLocationY):
    for i in range (9):
        pygame.draw.rect(Assets.WIN, Assets.BLACK, (stackLocationX+4+(i*-3),stackLocationY+4+(i*-3), Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
    pygame.draw.rect(Assets.WIN, Assets.WHITE, (stackLocationX+(9*-3),stackLocationY+(9*-3), Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
    Assets.WIN.blit(Assets.cardback_black, (stackLocationX+9+(9*-3),stackLocationY+11+(9*-3)))

def drawCard(cardlocationx, cardlocationy,card):
    pygame.draw.rect(Assets.WIN, Assets.BLACK, (cardlocationx+(4*Assets.scalingVal),cardlocationy+(4*Assets.scalingVal), Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
    pygame.draw.rect(Assets.WIN, Assets.WHITE, (cardlocationx,cardlocationy, Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
    Assets.WIN.blit(card, (cardlocationx,cardlocationy))

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
    for i in range(8):
        for f in range(i):
            pygame.draw.rect(Assets.WIN, Assets.BLACK, (cardlocationx+(4*Assets.scalingVal)+(250*Assets.scalingVal*i),cardlocationy+(4*Assets.scalingVal)+(50*f), Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
            pygame.draw.rect(Assets.WIN, Assets.WHITE, (cardlocationx+(250*Assets.scalingVal*i),cardlocationy+(50*f), Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
            if(f < i-1):
                Assets.WIN.blit(Assets.cardback_black, (cardlocationx+(9*Assets.scalingVal)+(i*250*Assets.scalingVal),cardlocationy+(11*Assets.scalingVal)+(f*50)))
                
            elif(f == i-1):
                Assets.WIN.blit(ListOfCards.tableauObj[0].card, (cardlocationx+(i*250*Assets.scalingVal),cardlocationy+(f*50)))

def drawWindow(renderCheck, activeCard,currentCard):
    cardloctionx, cardlocationy = 220*Assets.scalingVal,30*Assets.scalingVal
    stackLocationX, stackLocationY = 30*Assets.scalingVal,30*Assets.scalingVal
    #testCard = Card.Card(DealCards.randomRankAndSuit(),cardloctionx,cardlocationy)

    Assets.WIN.fill(Assets.GREEN)
    if renderCheck:
        newval= currentCard
        activeCard.setCard(newval)
        activeCard.rankandsuit=newval
    #print(testCard.rankandsuit, renderCheck)
    drawCard(cardloctionx,cardlocationy,activeCard.card)
    drawDeckOfCards(stackLocationX,stackLocationY)
    drawCardStackLocation()
    drawTableau()