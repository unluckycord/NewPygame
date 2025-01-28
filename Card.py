import pygame,Assets
class Card:
    def __init__(self, rankandsuit,cardlocationx,cardlocationy):
        self.rankandsuit = rankandsuit
        self.Card = None
        self.cardlocationx=cardlocationx
        self.cardlocationy=cardlocationy
        match rankandsuit:
            case "2s":
                self.Card = Assets.twos
            case "2d":
                self.Card = Assets.twod
            case "2h":
                self.Card = Assets.twoh
            case "2c":
                self.Card = Assets.twoc
            case "3s":
                self.Card = Assets.threes
            case "3d":
                self.Card = Assets.threed
            case "3h":
                self.Card = Assets.threeh
            case "3c":
                self.Card = Assets.threec
            case "4s":
                self.Card = Assets.fours
            case "4d":
                self.Card = Assets.fourd
            case "4h":
                self.Card = Assets.fourh
            case "4c":
                self.Card = Assets.fourc
            case "5s":
                self.Card = Assets.fives
            case "5d":
                self.Card = Assets.fived
            case "5h":
                self.Card = Assets.fiveh
            case "5c":
                self.Card = Assets.fivec
            case "6s":
                self.Card = Assets.sixs
            case "6d":
                self.Card = Assets.sixd
            case "6h":
                self.Card = Assets.sixh
            case "6c":
                self.Card = Assets.sixc
            case "7s":
                self.Card = Assets.sevens
            case "7d":
                self.Card = Assets.sevend
            case "7h":
                self.Card = Assets.sevenh
            case "7c":
                self.Card = Assets.sevenc
            case "8s":
                self.Card = Assets.eights
            case "8d":
                self.Card = Assets.eightd
            case "8h":
                self.Card = Assets.eighth
            case "8c":
                self.Card = Assets.eightc
            case "9s":
                self.Card = Assets.nines
            case "9d":
                self.Card = Assets.nined
            case "9h":
                self.Card = Assets.nineh
            case "9c":
                self.Card = Assets.ninec
            case "10s":
                self.Card = Assets.tens
            case "10d":
                self.Card = Assets.tend
            case "10h":
                self.Card = Assets.tenh
            case "10c":
                self.Card = Assets.tenc
            case "12s":
                self.Card = Assets.jacks
            case "12d":
                self.Card = Assets.jackd
            case "12h":
                self.Card = Assets.jackh
            case "12c":
                self.Card = Assets.jackc
            case "13s":
                self.Card = Assets.queens
            case "13d":
                self.Card = Assets.queend
            case "13h":
                self.Card = Assets.queenh
            case "13c":
                self.Card = Assets.queenc
            case "14s":
                self.Card = Assets.kings
            case "14d":
                self.Card = Assets.kingd
            case "14h":
                self.Card = Assets.kingh
            case "14c":
                self.Card = Assets.kingc
            case "11s":
                self.Card = Assets.aces
            case "11d":
                self.Card = Assets.aced
            case "11h":
                self.Card = Assets.aceh
            case "11c":
                self.Card = Assets.acec
                
