import pygame,Assets
class Card:
    def __init__(self, rankandsuit,cardUpOrDown,cardRect,col,row):
        self.cardInObjective = False
        self.rankandsuit = rankandsuit
        self.cardUpOrDown = cardUpOrDown.upper()
        if(len(self.rankandsuit) == 2):
            self.rank = int(self.rankandsuit[0:1])
            self.suit = self.rankandsuit[1:]
        else:
            self.rank = int(self.rankandsuit[0:2])
            self.suit = self.suit = self.rankandsuit[2:]
        if(self.suit == "s" or self.suit == "c"):
            self.colorIndex = 1
        else:
            self.colorIndex = 0
        self.cardlocationx=cardRect.x
        self.cardlocationy=cardRect.y
        self.cardRect = cardRect
        self.col = col
        self.row = row
        self.cardStack = []
        self.isStacked = False
        self.isStackedInDeck = True
        match rankandsuit:
            case "2s":
                self.card = Assets.twos
            case "2d":
                self.card = Assets.twod
            case "2h":
                self.card = Assets.twoh
            case "2c":
                self.card = Assets.twoc
            case "3s":
                self.card = Assets.threes
            case "3d":
                self.card = Assets.threed
            case "3h":
                self.card = Assets.threeh
            case "3c":
                self.card = Assets.threec
            case "4s":
                self.card = Assets.fours
            case "4d":
                self.card = Assets.fourd
            case "4h":
                self.card = Assets.fourh
            case "4c":
                self.card = Assets.fourc
            case "5s":
                self.card = Assets.fives
            case "5d":
                self.card = Assets.fived
            case "5h":
                self.card = Assets.fiveh
            case "5c":
                self.card = Assets.fivec
            case "6s":
                self.card = Assets.sixs
            case "6d":
                self.card = Assets.sixd
            case "6h":
                self.card = Assets.sixh
            case "6c":
                self.card = Assets.sixc
            case "7s":
                self.card = Assets.sevens
            case "7d":
                self.card = Assets.sevend
            case "7h":
                self.card = Assets.sevenh
            case "7c":
                self.card = Assets.sevenc
            case "8s":
                self.card = Assets.eights
            case "8d":
                self.card = Assets.eightd
            case "8h":
                self.card = Assets.eighth
            case "8c":
                self.card = Assets.eightc
            case "9s":
                self.card = Assets.nines
            case "9d":
                self.card = Assets.nined
            case "9h":
                self.card = Assets.nineh
            case "9c":
                self.card = Assets.ninec
            case "10s":
                self.card = Assets.tens
            case "10d":
                self.card = Assets.tend
            case "10h":
                self.card = Assets.tenh
            case "10c":
                self.card = Assets.tenc
            case "11s":
                self.card = Assets.jacks
            case "11d":
                self.card = Assets.jackd
            case "11h":
                self.card = Assets.jackh
            case "11c":
                self.card = Assets.jackc
            case "12s":
                self.card = Assets.queens
            case "12d":
                self.card = Assets.queend
            case "12h":
                self.card = Assets.queenh
            case "12c":
                self.card = Assets.queenc
            case "13s":
                self.card = Assets.kings
            case "13d":
                self.card = Assets.kingd
            case "13h":
                self.card = Assets.kingh
            case "13c":
                self.card = Assets.kingc
            case "1s":
                self.card = Assets.aces
            case "1d":
                self.card = Assets.aced
            case "1h":
                self.card = Assets.aceh
            case "1c":
                self.card = Assets.acec

    #its really dumb and silly, however, i had to add this as a function, otherwise the card cannot initilize or change properly.
    def setCard(self, newVal):
        match newVal:
            case "2s":
                self.card = Assets.twos
            case "2d":
                self.card = Assets.twod
            case "2h":
                self.card = Assets.twoh
            case "2c":
                self.card = Assets.twoc
            case "3s":
                self.card = Assets.threes
            case "3d":
                self.card = Assets.threed
            case "3h":
                self.card = Assets.threeh
            case "3c":
                self.card = Assets.threec
            case "4s":
                self.card = Assets.fours
            case "4d":
                self.card = Assets.fourd
            case "4h":
                self.card = Assets.fourh
            case "4c":
                self.card = Assets.fourc
            case "5s":
                self.card = Assets.fives
            case "5d":
                self.card = Assets.fived
            case "5h":
                self.card = Assets.fiveh
            case "5c":
                self.card = Assets.fivec
            case "6s":
                self.card = Assets.sixs
            case "6d":
                self.card = Assets.sixd
            case "6h":
                self.card = Assets.sixh
            case "6c":
                self.card = Assets.sixc
            case "7s":
                self.card = Assets.sevens
            case "7d":
                self.card = Assets.sevend
            case "7h":
                self.card = Assets.sevenh
            case "7c":
                self.card = Assets.sevenc
            case "8s":
                self.card = Assets.eights
            case "8d":
                self.card = Assets.eightd
            case "8h":
                self.card = Assets.eighth
            case "8c":
                self.card = Assets.eightc
            case "9s":
                self.card = Assets.nines
            case "9d":
                self.card = Assets.nined
            case "9h":
                self.card = Assets.nineh
            case "9c":
                self.card = Assets.ninec
            case "10s":
                self.card = Assets.tens
            case "10d":
                self.card = Assets.tend
            case "10h":
                self.card = Assets.tenh
            case "10c":
                self.card = Assets.tenc
            case "11s":
                self.card = Assets.jacks
            case "11d":
                self.card = Assets.jackd
            case "11h":
                self.card = Assets.jackh
            case "11c":
                self.card = Assets.jackc
            case "12s":
                self.card = Assets.queens
            case "12d":
                self.card = Assets.queend
            case "12h":
                self.card = Assets.queenh
            case "12c":
                self.card = Assets.queenc
            case "13s":
                self.card = Assets.kings
            case "13d":
                self.card = Assets.kingd
            case "13h":
                self.card = Assets.kingh
            case "13c":
                self.card = Assets.kingc
            case "1s":
                self.card = Assets.aces
            case "1d":
                self.card = Assets.aced
            case "1h":
                self.card = Assets.aceh
            case "1c":
                self.card = Assets.acec