import pygame,Assets
class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        self.suitandnumber = str(str(number)+suit)
        self.Card = None
        if(self.suitandnumber == "2s"):
            self.Card = Assets.twos
        if(self.suitandnumber == "2d"):
            self.Card = Assets.twod
        if(self.suitandnumber == "2h"):
            self.Card = Assets.twoh
        if(self.suitandnumber == "2c"):
            self.Card = Assets.twoc
        if(self.suitandnumber == "3s"):
            self.Card = Assets.threes
        if(self.suitandnumber == "3d"):
            self.Card = Assets.threed
        if(self.suitandnumber == "3h"):
            self.Card = Assets.threeh
        if(self.suitandnumber == "3c"):
            self.Card = Assets.threec
        if(self.suitandnumber == "4s"):
            self.Card = Assets.fours
        if(self.suitandnumber == "4d"):
            self.Card = Assets.fourd
        if(self.suitandnumber == "4h"):
            self.Card = Assets.fourh
        if(self.suitandnumber == "4c"):
            self.Card = Assets.fourc
        if(self.suitandnumber == "5s"):
            self.Card = Assets.fives
        if(self.suitandnumber == "5d"):
            self.Card = Assets.fived
        if(self.suitandnumber == "5h"):
            self.Card = Assets.fiveh
        if(self.suitandnumber == "5c"):
            self.Card = Assets.fivec
        if(self.suitandnumber == "6s"):
            self.Card = Assets.sixs
        if(self.suitandnumber == "6d"):
            self.Card = Assets.sixd
        if(self.suitandnumber == "6h"):
            self.Card = Assets.sixh
        if(self.suitandnumber == "6c"):
            self.Card = Assets.sixc
        if(self.suitandnumber == "7s"):
            self.Card = Assets.sevens
        if(self.suitandnumber == "7d"):
            self.Card = Assets.sevend
        if(self.suitandnumber == "7h"):
            self.Card = Assets.sevenh
        if(self.suitandnumber == "7c"):
            self.Card = Assets.sevenc
        if(self.suitandnumber == "8s"):
            self.Card = Assets.eights
        if(self.suitandnumber == "8d"):
            self.Card = Assets.eightd
        if(self.suitandnumber == "8h"):
            self.Card = Assets.eighth
        if(self.suitandnumber == "8c"):
            self.Card = Assets.eightc
        if(self.suitandnumber == "9s"):
            self.Card = Assets.nines
        if(self.suitandnumber == "9d"):
            self.Card = Assets.nined
        if(self.suitandnumber == "9h"):
            self.Card = Assets.nineh
        if(self.suitandnumber == "9c"):
            self.Card = Assets.ninec

    def getSuit(self):
        return self.suit
    def getNumber(self):
        return self.number
