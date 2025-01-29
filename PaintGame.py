from time import sleep
import pygame,Assets,random,Card,DealCards

def drawDeckOfCards(stackLocationX, stackLocationY):
    for i in range (9):
        pygame.draw.rect(Assets.WIN, Assets.BLACK, (stackLocationX+4+(i*-3),stackLocationY+4+(i*-3), Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
    pygame.draw.rect(Assets.WIN, Assets.WHITE, (stackLocationX+(9*-3),stackLocationY+(9*-3), Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
    Assets.WIN.blit(Assets.cardback_black, (stackLocationX+9+(9*-3),stackLocationY+11+(9*-3)))

def drawCard(cardlocationx, cardlocationy,card):
    pygame.draw.rect(Assets.WIN, Assets.BLACK, (cardlocationx+4,cardlocationy+4, Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
    pygame.draw.rect(Assets.WIN, Assets.WHITE, (cardlocationx,cardlocationy, Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
    Assets.WIN.blit(card, (cardlocationx,cardlocationy))

def drawWindow(renderCheck, testCard):
    cardloctionx, cardlocationy = 220,30
    stackLocationX, stackLocationY = 30,30
    #testCard = Card.Card(DealCards.randomRankAndSuit(),cardloctionx,cardlocationy)
    Assets.WIN.fill(Assets.GREEN)
    #Draws Rectanle taking in window size, color, 
    #as well as a tuple containing x, y, then width and height
    if renderCheck:
        newval= DealCards.randomRankAndSuit()
        testCard.setCard(newval)
        testCard.rankandsuit=newval
        print("YAY", testCard.rankandsuit)
    #print(testCard.rankandsuit, renderCheck)
    drawCard(cardloctionx,cardlocationy,testCard.card)
    drawDeckOfCards(stackLocationX,stackLocationY)