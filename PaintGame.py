import pygame,Assets,random,Card

def randomSuit():
    suitSwitcher = random.randrange(1,4,1)
    Assets.cardFlick.play()
    if(suitSwitcher == 1):
        return "s"
    if(suitSwitcher == 2):
        return "h"
    if(suitSwitcher == 3):
        return "d"
    if(suitSwitcher == 4):
        return "c"

def drawWindow():

    num = random.randrange(2,9,1)
    print(num)


    testCard = Card.Card(randomSuit(),num)
    Assets.WIN.fill(Assets.GREEN)
    #Draws Rectanle taking in window size, color, 
    #as well as a tuple containing x, y, then width and height
    pygame.draw.rect(Assets.WIN, Assets.WHITE, (30,30, 222,323),width=0, border_radius=13)
    Assets.WIN.blit(testCard.Card, (30,31))