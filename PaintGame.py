from time import sleep
import pygame,Assets,random,Card,DealCards,ListOfCards
def drawMouseBox(mouseRect):
    
    pygame.draw.rect(Assets.WIN, Assets.WHITE, mouseRect)

def drawDeckOfCards(pileLocationShadow):
    for i in range (9):
        #shadow
        pygame.draw.rect(Assets.WIN, Assets.BLACK, (pileLocationShadow[i].x,pileLocationShadow[i].y, pileLocationShadow[i].width,pileLocationShadow[i].height),width=0, border_radius=13)
    #white card surface
    pygame.draw.rect(Assets.WIN, Assets.WHITE, (pileLocationShadow[0].x+(9*-3),pileLocationShadow[0].y+(9*-3), Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
    #card back
    Assets.WIN.blit(Assets.cardback_black, (pileLocationShadow[0].x+9+(9*-3),pileLocationShadow[0].y+11+(9*-3)))

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
        for f in range(len(ListOfCards.listOfCardsInObjective[i])):
            pygame.draw.rect(Assets.WIN, Assets.WHITE, ListOfCards.listOfCardsInObjective[i][f].cardRect, width=0, border_radius=13)
            Assets.WIN.blit(ListOfCards.listOfCardsInObjective[i][f].card,ListOfCards.listOfCardsInObjective[i][f].cardRect)

def drawHighlight(grabCheck,currentCardTableau):
    if(grabCheck):
        pygame.draw.rect(Assets.WIN, Assets.GOLD, (currentCardTableau.cardRect.x+(6*Assets.scalingVal),currentCardTableau.cardRect.y+(6*Assets.scalingVal), Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)

def drawTableau():
    for i in range(len(ListOfCards.tableauObj)):
        for f in range(len(ListOfCards.tableauObj[i])):
            #shadow
            pygame.draw.rect(Assets.WIN, Assets.BLACK, (ListOfCards.tableauObj[i][f].cardRect.x+(4*Assets.scalingVal),ListOfCards.tableauObj[i][f].cardRect.y+(4*Assets.scalingVal), Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
            #white card surface
            pygame.draw.rect(Assets.WIN, Assets.WHITE, (ListOfCards.tableauObj[i][f].cardRect.x,ListOfCards.tableauObj[i][f].cardRect.y, Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
            if(ListOfCards.tableauObj[i][f].cardUpOrDown == "DOWN"):
                #card back
                Assets.WIN.blit(Assets.cardback_black, (ListOfCards.tableauObj[i][f].cardRect.x+(9*Assets.scalingVal),ListOfCards.tableauObj[i][f].cardRect.y+(11*Assets.scalingVal)))
            else:
                #card face
                Assets.WIN.blit(ListOfCards.tableauObj[i][f].card, (ListOfCards.tableauObj[i][f].cardRect.x,ListOfCards.tableauObj[i][f].cardRect.y))



def drawWindow(flipCardCheck,grabCheck,mouseRect,stackList,currentCardTableau,pileLocationShadow):

    Assets.WIN.fill(Assets.GREEN)
    if flipCardCheck:
        newval= ListOfCards.cardStackOject[0].rankandsuit
        ListOfCards.cardStackOject[0].setCard(newval)
        ListOfCards.cardStackOject[0].rankandsuit=newval
    #print(testCard.rankandsuit, renderCheck)
    drawHighlight(grabCheck,currentCardTableau)
    drawCard(ListOfCards.cardStackOject[0].cardRect,ListOfCards.cardStackOject[0].card)
    drawDeckOfCards(pileLocationShadow)
    drawCardStackLocation(stackList)
    drawTableau()