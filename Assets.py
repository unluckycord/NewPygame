import pygame
TARGETFPS = 120
GREEN = (0,99,33)
WHITE = (255,255,255)
BLACK = (0,0,0)
GOLD = (218, 165, 32)

WIDTH, HEIGHT = 1200,800
#WIDTH, HEIGHT = 1800, 1080
pygame.display.init()
displayInformation = pygame.display.Info()
scalingVal = .85
#WIDTH, HEIGHT = displayInformation.current_w, displayInformation.current_h
WIN=pygame.display.set_mode((int(displayInformation.current_w*scalingVal),int(displayInformation.current_h*scalingVal)))
#WIN=pygame.display.set_mode((0,0),pygame.FULLSCREEN)

pygame.mixer.init()
cardFlick = pygame.mixer.Sound("Assets/cardFlick.wav")
cardFlick.set_volume(0.3)
CARDWIDTH, CARDHEIGHT = int((219*.80)*scalingVal), int((320*.80)*scalingVal)

H = "HEARTS"
S = "SPADES"
D = "DIAMONDS"
C = "CLUBS"
J = 10
Q = 10
K = 10



twos = pygame.transform.scale(pygame.image.load("Assets/png/2_of_spades.png"), (CARDWIDTH,CARDHEIGHT))
twod = pygame.transform.scale(pygame.image.load("Assets/png/2_of_diamonds.png"), (CARDWIDTH,CARDHEIGHT))
twoh = pygame.transform.scale(pygame.image.load("Assets/png/2_of_hearts.png"), (CARDWIDTH,CARDHEIGHT))
twoc = pygame.transform.scale(pygame.image.load("Assets/png/2_of_clubs.png"), (CARDWIDTH,CARDHEIGHT))
threes = pygame.transform.scale(pygame.image.load("Assets/png/3_of_spades.png"), (CARDWIDTH,CARDHEIGHT))
threed = pygame.transform.scale(pygame.image.load("Assets/png/3_of_diamonds.png"), (CARDWIDTH,CARDHEIGHT))
threeh = pygame.transform.scale(pygame.image.load("Assets/png/3_of_hearts.png"), (CARDWIDTH,CARDHEIGHT))
threec = pygame.transform.scale(pygame.image.load("Assets/png/3_of_clubs.png"), (CARDWIDTH,CARDHEIGHT))
fours = pygame.transform.scale(pygame.image.load("Assets/png/4_of_spades.png"), (CARDWIDTH,CARDHEIGHT))
fourd = pygame.transform.scale(pygame.image.load("Assets/png/4_of_diamonds.png"), (CARDWIDTH,CARDHEIGHT))
fourh = pygame.transform.scale(pygame.image.load("Assets/png/4_of_hearts.png"), (CARDWIDTH,CARDHEIGHT))
fourc = pygame.transform.scale(pygame.image.load("Assets/png/4_of_clubs.png"), (CARDWIDTH,CARDHEIGHT))
fives = pygame.transform.scale(pygame.image.load("Assets/png/5_of_spades.png"), (CARDWIDTH,CARDHEIGHT))
fived = pygame.transform.scale(pygame.image.load("Assets/png/5_of_diamonds.png"), (CARDWIDTH,CARDHEIGHT))
fiveh = pygame.transform.scale(pygame.image.load("Assets/png/5_of_hearts.png"), (CARDWIDTH,CARDHEIGHT))
fivec = pygame.transform.scale(pygame.image.load("Assets/png/5_of_clubs.png"), (CARDWIDTH,CARDHEIGHT))
sixs = pygame.transform.scale(pygame.image.load("Assets/png/6_of_spades.png"), (CARDWIDTH,CARDHEIGHT))
sixd = pygame.transform.scale(pygame.image.load("Assets/png/6_of_diamonds.png"), (CARDWIDTH,CARDHEIGHT))
sixh = pygame.transform.scale(pygame.image.load("Assets/png/6_of_hearts.png"), (CARDWIDTH,CARDHEIGHT))
sixc = pygame.transform.scale(pygame.image.load("Assets/png/6_of_clubs.png"), (CARDWIDTH,CARDHEIGHT))
sevens = pygame.transform.scale(pygame.image.load("Assets/png/7_of_spades.png"), (CARDWIDTH,CARDHEIGHT))
sevend = pygame.transform.scale(pygame.image.load("Assets/png/7_of_diamonds.png"), (CARDWIDTH,CARDHEIGHT))
sevenh = pygame.transform.scale(pygame.image.load("Assets/png/7_of_hearts.png"), (CARDWIDTH,CARDHEIGHT))
sevenc = pygame.transform.scale(pygame.image.load("Assets/png/7_of_clubs.png"), (CARDWIDTH,CARDHEIGHT))
eights = pygame.transform.scale(pygame.image.load("Assets/png/8_of_spades.png"), (CARDWIDTH,CARDHEIGHT))
eightd = pygame.transform.scale(pygame.image.load("Assets/png/8_of_diamonds.png"), (CARDWIDTH,CARDHEIGHT))
eighth = pygame.transform.scale(pygame.image.load("Assets/png/8_of_hearts.png"), (CARDWIDTH,CARDHEIGHT))
eightc = pygame.transform.scale(pygame.image.load("Assets/png/8_of_clubs.png"), (CARDWIDTH,CARDHEIGHT))
nines = pygame.transform.scale(pygame.image.load("Assets/png/9_of_spades.png"), (CARDWIDTH,CARDHEIGHT))
nined = pygame.transform.scale(pygame.image.load("Assets/png/9_of_diamonds.png"), (CARDWIDTH,CARDHEIGHT))
nineh = pygame.transform.scale(pygame.image.load("Assets/png/9_of_hearts.png"), (CARDWIDTH,CARDHEIGHT))
ninec = pygame.transform.scale(pygame.image.load("Assets/png/9_of_clubs.png"), (CARDWIDTH,CARDHEIGHT))
tens = pygame.transform.scale(pygame.image.load("Assets/png/10_of_spades.png"), (CARDWIDTH,CARDHEIGHT))
tend = pygame.transform.scale(pygame.image.load("Assets/png/10_of_diamonds.png"), (CARDWIDTH,CARDHEIGHT))
tenh = pygame.transform.scale(pygame.image.load("Assets/png/10_of_hearts.png"), (CARDWIDTH,CARDHEIGHT))
tenc = pygame.transform.scale(pygame.image.load("Assets/png/10_of_clubs.png"), (CARDWIDTH,CARDHEIGHT))
jacks = pygame.transform.scale(pygame.image.load("Assets/png/jack_of_spades.png"), (CARDWIDTH,CARDHEIGHT))
jackd = pygame.transform.scale(pygame.image.load("Assets/png/jack_of_diamonds.png"), (CARDWIDTH,CARDHEIGHT))
jackh = pygame.transform.scale(pygame.image.load("Assets/png/jack_of_hearts.png"), (CARDWIDTH,CARDHEIGHT))
jackc = pygame.transform.scale(pygame.image.load("Assets/png/jack_of_clubs.png"), (CARDWIDTH,CARDHEIGHT))
queens = pygame.transform.scale(pygame.image.load("Assets/png/queen_of_spades.png"), (CARDWIDTH,CARDHEIGHT))
queend = pygame.transform.scale(pygame.image.load("Assets/png/queen_of_diamonds.png"), (CARDWIDTH,CARDHEIGHT))
queenh = pygame.transform.scale(pygame.image.load("Assets/png/queen_of_hearts.png"), (CARDWIDTH,CARDHEIGHT))
queenc = pygame.transform.scale(pygame.image.load("Assets/png/queen_of_clubs.png"), (CARDWIDTH,CARDHEIGHT))
kings = pygame.transform.scale(pygame.image.load("Assets/png/king_of_spades.png"), (CARDWIDTH,CARDHEIGHT))
kingd = pygame.transform.scale(pygame.image.load("Assets/png/king_of_diamonds.png"), (CARDWIDTH,CARDHEIGHT))
kingh = pygame.transform.scale(pygame.image.load("Assets/png/king_of_hearts.png"), (CARDWIDTH,CARDHEIGHT))
kingc = pygame.transform.scale(pygame.image.load("Assets/png/king_of_clubs.png"), (CARDWIDTH,CARDHEIGHT))
aces = pygame.transform.scale(pygame.image.load("Assets/png/ace_of_spades.png"), (CARDWIDTH,CARDHEIGHT))
aced = pygame.transform.scale(pygame.image.load("Assets/png/ace_of_diamonds.png"), (CARDWIDTH,CARDHEIGHT))
aceh = pygame.transform.scale(pygame.image.load("Assets/png/ace_of_hearts.png"), (CARDWIDTH,CARDHEIGHT))
acec = pygame.transform.scale(pygame.image.load("Assets/png/ace_of_clubs.png"), (CARDWIDTH,CARDHEIGHT))
cardback_black = pygame.transform.scale(pygame.image.load("Assets/png/cardback-black.png"), (int((CARDWIDTH*.90)),int(((CARDHEIGHT+5)*.90))))