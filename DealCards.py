import random, ListOfCards
def randomRankAndSuit():
    suitSwitcher = random.randrange(1,4,1)
    suit = None
    if(suitSwitcher == 1):
        suit = "s"
    if(suitSwitcher == 2):
        suit = "h"
    if(suitSwitcher == 3):
        suit = "d"
    if(suitSwitcher == 4):
        suit = "c"
    num = random.randrange(2,14,1)
    return str(str(num)+suit)
def shuffle():
    random.shuffle(ListOfCards.listOfActiveCards)
    ListOfCards.listOfActiveCardsPostShuffle = ListOfCards.listOfActiveCards
def resetCards():
    ListOfCards.listOfActiveCards = ListOfCards.LISTOFALLDEFAULTCARDS
def drawCardFromDeck():
    print("\n","\n",ListOfCards.listOfActiveCards)
    tempVal = ListOfCards.listOfActiveCards[0]
    ListOfCards.listOfActiveCards.append(tempVal)
    ListOfCards.listOfActiveCards.pop(0)
    return tempVal