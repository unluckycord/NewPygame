import pygame,Assets,random,Card,DealCards



def drawWindow():


    testCard = Card.Card(DealCards.randomRankAndSuit())
    Assets.WIN.fill(Assets.GREEN)
    #Draws Rectanle taking in window size, color, 
    #as well as a tuple containing x, y, then width and height
    pygame.draw.rect(Assets.WIN, Assets.WHITE, (30,30, 222,323),width=0, border_radius=13)
    Assets.WIN.blit(testCard.Card, (30,31))