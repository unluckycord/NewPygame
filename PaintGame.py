from time import sleep
import pygame,Assets,random,Card,DealCards

def drawDeckOfCards(cardlocationx, cardlocationy):
    pygame.draw.rect(Assets.WIN, Assets.BLACK, (cardlocationx+4,cardlocationy+4, Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
    pygame.draw.rect(Assets.WIN, Assets.WHITE, (cardlocationx,cardlocationy, Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
    Assets.WIN.blit(Assets.cardback_black, (cardlocationx,cardlocationy))

def drawCard(cardlocationx, cardlocationy,card):
    pygame.draw.rect(Assets.WIN, Assets.BLACK, (cardlocationx+4,cardlocationy+4, Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
    pygame.draw.rect(Assets.WIN, Assets.WHITE, (cardlocationx,cardlocationy, Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
    Assets.WIN.blit(card, (cardlocationx,cardlocationy))

def drawWindow(renderCheck, testCard):
    cardloctionx, cardlocationy = 400,400
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