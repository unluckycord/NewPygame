import random
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
    print(str(str(num)+suit))
    return str(str(num)+suit)