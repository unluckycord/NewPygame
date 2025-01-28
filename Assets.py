import pygame
TARGETFPS = 120
GREEN = (0,99,33)
WHITE = (255,255,255)
WIDTH, HEIGHT = 1200, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mixer.init()
cardFlick = pygame.mixer.Sound("Assets/shuffling-cards.wav")

H = "HEARTS"
S = "SPADES"
D = "DIAMONDS"
C = "CLUBS"
J = 10
Q = 10
K = 10

sevenS = pygame.transform.scale(pygame.image.load(
    "Assets/png/7_of_spades.png"), (219,320))


twos = pygame.transform.scale(pygame.image.load("Assets/png/2_of_spades.png"), (219,320))
twod = pygame.transform.scale(pygame.image.load("Assets/png/2_of_diamonds.png"), (219,320))
twoh = pygame.transform.scale(pygame.image.load("Assets/png/2_of_hearts.png"), (219,320))
twoc = pygame.transform.scale(pygame.image.load("Assets/png/2_of_clubs.png"), (219,320))
threes = pygame.transform.scale(pygame.image.load("Assets/png/3_of_spades.png"), (219,320))
threed = pygame.transform.scale(pygame.image.load("Assets/png/3_of_diamonds.png"), (219,320))
threeh = pygame.transform.scale(pygame.image.load("Assets/png/3_of_hearts.png"), (219,320))
threec = pygame.transform.scale(pygame.image.load("Assets/png/3_of_clubs.png"), (219,320))
fours = pygame.transform.scale(pygame.image.load("Assets/png/4_of_spades.png"), (219,320))
fourd = pygame.transform.scale(pygame.image.load("Assets/png/4_of_diamonds.png"), (219,320))
fourh = pygame.transform.scale(pygame.image.load("Assets/png/4_of_hearts.png"), (219,320))
fourc = pygame.transform.scale(pygame.image.load("Assets/png/4_of_clubs.png"), (219,320))
fives = pygame.transform.scale(pygame.image.load("Assets/png/5_of_spades.png"), (219,320))
fived = pygame.transform.scale(pygame.image.load("Assets/png/5_of_diamonds.png"), (219,320))
fiveh = pygame.transform.scale(pygame.image.load("Assets/png/5_of_hearts.png"), (219,320))
fivec = pygame.transform.scale(pygame.image.load("Assets/png/5_of_clubs.png"), (219,320))
sixs = pygame.transform.scale(pygame.image.load("Assets/png/6_of_spades.png"), (219,320))
sixd = pygame.transform.scale(pygame.image.load("Assets/png/6_of_diamonds.png"), (219,320))
sixh = pygame.transform.scale(pygame.image.load("Assets/png/6_of_hearts.png"), (219,320))
sixc = pygame.transform.scale(pygame.image.load("Assets/png/6_of_clubs.png"), (219,320))
sevens = pygame.transform.scale(pygame.image.load("Assets/png/7_of_spades.png"), (219,320))
sevend = pygame.transform.scale(pygame.image.load("Assets/png/7_of_diamonds.png"), (219,320))
sevenh = pygame.transform.scale(pygame.image.load("Assets/png/7_of_hearts.png"), (219,320))
sevenc = pygame.transform.scale(pygame.image.load("Assets/png/7_of_clubs.png"), (219,320))
eights = pygame.transform.scale(pygame.image.load("Assets/png/8_of_spades.png"), (219,320))
eightd = pygame.transform.scale(pygame.image.load("Assets/png/8_of_diamonds.png"), (219,320))
eighth = pygame.transform.scale(pygame.image.load("Assets/png/8_of_hearts.png"), (219,320))
eightc = pygame.transform.scale(pygame.image.load("Assets/png/8_of_clubs.png"), (219,320))
nines = pygame.transform.scale(pygame.image.load("Assets/png/9_of_spades.png"), (219,320))
nined = pygame.transform.scale(pygame.image.load("Assets/png/9_of_diamonds.png"), (219,320))
nineh = pygame.transform.scale(pygame.image.load("Assets/png/9_of_hearts.png"), (219,320))
ninec = pygame.transform.scale(pygame.image.load("Assets/png/9_of_clubs.png"), (219,320))
tens = pygame.transform.scale(pygame.image.load("Assets/png/10_of_spades.png"), (219,320))
tend = pygame.transform.scale(pygame.image.load("Assets/png/10_of_diamonds.png"), (219,320))
tenh = pygame.transform.scale(pygame.image.load("Assets/png/10_of_hearts.png"), (219,320))
tenc = pygame.transform.scale(pygame.image.load("Assets/png/10_of_clubs.png"), (219,320))
jacks = pygame.transform.scale(pygame.image.load("Assets/png/jack_of_spades.png"), (219,320))
jackd = pygame.transform.scale(pygame.image.load("Assets/png/jack_of_diamonds.png"), (219,320))
jackh = pygame.transform.scale(pygame.image.load("Assets/png/jack_of_hearts.png"), (219,320))
jackc = pygame.transform.scale(pygame.image.load("Assets/png/jack_of_clubs.png"), (219,320))
queens = pygame.transform.scale(pygame.image.load("Assets/png/queen_of_spades.png"), (219,320))
queend = pygame.transform.scale(pygame.image.load("Assets/png/queen_of_diamonds.png"), (219,320))
queenh = pygame.transform.scale(pygame.image.load("Assets/png/queen_of_hearts.png"), (219,320))
queenc = pygame.transform.scale(pygame.image.load("Assets/png/queen_of_clubs.png"), (219,320))
kings = pygame.transform.scale(pygame.image.load("Assets/png/king_of_spades.png"), (219,320))
kingd = pygame.transform.scale(pygame.image.load("Assets/png/king_of_diamonds.png"), (219,320))
kingh = pygame.transform.scale(pygame.image.load("Assets/png/king_of_hearts.png"), (219,320))
kingc = pygame.transform.scale(pygame.image.load("Assets/png/king_of_clubs.png"), (219,320))
aces = pygame.transform.scale(pygame.image.load("Assets/png/ace_of_spades.png"), (219,320))
aced = pygame.transform.scale(pygame.image.load("Assets/png/ace_of_diamonds.png"), (219,320))
aceh = pygame.transform.scale(pygame.image.load("Assets/png/ace_of_hearts.png"), (219,320))
acec = pygame.transform.scale(pygame.image.load("Assets/png/ace_of_clubs.png"), (219,320))
