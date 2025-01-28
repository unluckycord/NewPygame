from time import sleep
import pygame,Assets,random,Card,DealCards

def drawCard(cardloctionx, cardlocationy,card):
    pygame.draw.rect(Assets.WIN, Assets.BLACK, (cardloctionx+4,cardlocationy+4, Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
    pygame.draw.rect(Assets.WIN, Assets.WHITE, (cardloctionx,cardlocationy, Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
    Assets.WIN.blit(card, (cardloctionx,cardlocationy))

def drawWindow(renderCheck):
    cardloctionx, cardlocationy = 400,400
    testCard = Card.Card("4s",400,400)
    #testCard = Card.Card(DealCards.randomRankAndSuit(),cardloctionx,cardlocationy)
    Assets.WIN.fill(Assets.GREEN)
    #Draws Rectanle taking in window size, color, 
    #as well as a tuple containing x, y, then width and height
    if renderCheck:
        testCard.rankandsuit=DealCards.randomRankAndSuit()
        print("YAY", testCard.rankandsuit)
    #print(testCard.rankandsuit, renderCheck)
    drawCard(cardloctionx,cardlocationy,testCard.Card)