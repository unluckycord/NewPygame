import pygame,Assets,random,Card,DealCards



def drawWindow():

    cardloctionx, cardlocationy = 400,400
    #testCard = Card.Card(DealCards.randomRankAndSuit(),cardloctionx,cardlocationy)
    Assets.WIN.fill(Assets.GREEN)
    #Draws Rectanle taking in window size, color, 
    #as well as a tuple containing x, y, then width and height
    for i in range(52):
        pygame.draw.rect(Assets.WIN, Assets.BLACK, (cardloctionx+4-((i+5)*-1),cardlocationy+4-((i+5)*-1), Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
        pygame.draw.rect(Assets.WIN, Assets.WHITE, (cardloctionx-i,cardlocationy-i, Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
        Assets.WIN.blit(Assets.cardback_black, (cardloctionx+6-((i+4)),cardlocationy+7-((i+4))))
    #Assets.WIN.blit(testCard.Card, (30,31))