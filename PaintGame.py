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
    #card face
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
    
def drawTableau(grabCheck,currentCardTableau,mouseRect):
    for i in range(len(ListOfCards.tableauObj)):
        for f in range(len(ListOfCards.tableauObj[i])):
            if(grabCheck):
                pygame.draw.rect(Assets.WIN, Assets.GOLD, (currentCardTableau.cardlocationx+(4*Assets.scalingVal),currentCardTableau.cardlocationy+(4*Assets.scalingVal), Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
            else:
                #shadow
                pygame.draw.rect(Assets.WIN, Assets.BLACK, (ListOfCards.tableauObj[i][f].cardlocationx+(4*Assets.scalingVal),ListOfCards.tableauObj[i][f].cardlocationy+(4*Assets.scalingVal), Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
            #white card surface
            pygame.draw.rect(Assets.WIN, Assets.WHITE, (ListOfCards.tableauObj[i][f].cardlocationx,ListOfCards.tableauObj[i][f].cardlocationy, Assets.CARDWIDTH,Assets.CARDHEIGHT),width=0, border_radius=13)
            if(f+1 < i):
                #card back
                Assets.WIN.blit(Assets.cardback_black, (ListOfCards.tableauObj[i][f].cardlocationx+(9*Assets.scalingVal),ListOfCards.tableauObj[i][f].cardlocationy+(11*Assets.scalingVal)))
            else:
                #card face
                Assets.WIN.blit(ListOfCards.tableauObj[i][f].card, (ListOfCards.tableauObj[i][f].cardlocationx,ListOfCards.tableauObj[i][f].cardlocationy))
                ListOfCards.tableauObj[i][f].cardUpOrDown = "UP"



def drawWindow(flipCardCheck,grabCheck,activeCard,currentCard,mouseRect,cardLocationRect,stackList,currentCardTableau,pileLocationShadow):

    Assets.WIN.fill(Assets.GREEN)
    if flipCardCheck:
        newval= currentCard
        activeCard.setCard(newval)
        activeCard.rankandsuit=newval
    #print(testCard.rankandsuit, renderCheck)
    drawCard(cardLocationRect,activeCard.card)
    drawDeckOfCards(pileLocationShadow)
    drawCardStackLocation(stackList)
    drawTableau(grabCheck,currentCardTableau,mouseRect)