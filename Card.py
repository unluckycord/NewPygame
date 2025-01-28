import pygame,Assets
class Card:
    def __init__(self, rankandsuit,cardlocationx,cardlocationy):
        self.rankandsuit = rankandsuit
        self.Card = None
        self.cardlocationx=cardlocationx
        self.cardlocationy=cardlocationy
        match rankandsuit:
            case "2s":
                self.rankandsuit = "2s"
                self.Card = Assets.twos
            case "2d":
                self.rankandsuit = "2d"
                self.Card = Assets.twod
            case "2h":
                self.rankandsuit = "2h"
                self.Card = Assets.twoh
            case "2c":
                self.rankandsuit = "2c"
                self.Card = Assets.twoc
            case "3s":
                self.rankandsuit = "3s"
                self.Card = Assets.threes
            case "3d":
                self.rankandsuit = "3d"
                self.Card = Assets.threed
            case "3h":
                self.rankandsuit = "3h"
                self.Card = Assets.threeh
            case "3c":
                self.rankandsuit = "3c"
                self.Card = Assets.threec
            case "4s":
                self.rankandsuit = "4s"
                self.Card = Assets.fours
            case "4d":
                self.rankandsuit = "4d"
                self.Card = Assets.fourd
            case "4h":
                self.rankandsuit = "4h"
                self.Card = Assets.fourh
            case "4c":
                self.rankandsuit = "4c"
                self.Card = Assets.fourc
            case "5s":
                self.rankandsuit = "5s"
                self.Card = Assets.fives
            case "5d":
                self.rankandsuit = "5d"
                self.Card = Assets.fived
            case "5h":
                self.rankandsuit = "5h"
                self.Card = Assets.fiveh
            case "5c":
                self.rankandsuit = "5c"
                self.Card = Assets.fivec
            case "6s":
                self.rankandsuit = "6s"
                self.Card = Assets.sixs
            case "6d":
                self.rankandsuit = "6d"
                self.Card = Assets.sixd
            case "6h":
                self.rankandsuit = "6h"
                self.Card = Assets.sixh
            case "6c":
                self.rankandsuit = "6c"
                self.Card = Assets.sixc
            case "7s":
                self.rankandsuit = "7s"
                self.Card = Assets.sevens
            case "7d":
                self.rankandsuit = "7d"
                self.Card = Assets.sevend
            case "7h":
                self.rankandsuit = "7h"
                self.Card = Assets.sevenh
            case "7c":
                self.rankandsuit = "7c"
                self.Card = Assets.sevenc
            case "8s":
                self.rankandsuit = "8s"
                self.Card = Assets.eights
            case "8d":
                self.rankandsuit = "8d"
                self.Card = Assets.eightd
            case "8h":
                self.rankandsuit = "8h"
                self.Card = Assets.eighth
            case "8c":
                self.rankandsuit = "8c"
                self.Card = Assets.eightc
            case "9s":
                self.rankandsuit = "9s"
                self.Card = Assets.nines
            case "9d":
                self.rankandsuit = "9d"
                self.Card = Assets.nined
            case "9h":
                self.rankandsuit = "9h"
                self.Card = Assets.nineh
            case "9c":
                self.rankandsuit = "9c"
                self.Card = Assets.ninec
            case "10s":
                self.rankandsuit = "10s"
                self.Card = Assets.tens
            case "10d":
                self.rankandsuit = "10d"
                self.Card = Assets.tend
            case "10h":
                self.rankandsuit = "10h"
                self.Card = Assets.tenh
            case "10c":
                self.rankandsuit = "10c"
                self.Card = Assets.tenc
            case "12s":
                self.rankandsuit = "12s"
                self.Card = Assets.jacks
            case "12d":
                self.rankandsuit = "12d"
                self.Card = Assets.jackd
            case "12h":
                self.rankandsuit = "12h"
                self.Card = Assets.jackh
            case "12c":
                self.rankandsuit = "12c"
                self.Card = Assets.jackc
            case "13s":
                self.rankandsuit = "13s"
                self.Card = Assets.queens
            case "13d":
                self.rankandsuit = "13d"
                self.Card = Assets.queend
            case "13h":
                self.rankandsuit = "13h"
                self.Card = Assets.queenh
            case "13c":
                self.rankandsuit = "13c"
                self.Card = Assets.queenc
            case "14s":
                self.rankandsuit = "14s"
                self.Card = Assets.kings
            case "14d":
                self.rankandsuit = "14d"
                self.Card = Assets.kingd
            case "14h":
                self.rankandsuit = "14h"
                self.Card = Assets.kingh
            case "14c":
                self.rankandsuit = "14c"
                self.Card = Assets.kingc
            case "11s":
                self.rankandsuit = "11s"
                self.Card = Assets.aces
            case "11d":
                self.rankandsuit = "11d"
                self.Card = Assets.aced
            case "11h":
                self.rankandsuit = "11h"
                self.Card = Assets.aceh
            case "11c":
                self.rankandsuit = "11c"
                self.Card = Assets.acec
        def setRankAndSuit(newVal):
            self.rankandsuit = newVal
