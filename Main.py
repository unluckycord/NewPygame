import pygame, os, GameLoop,Assets

pygame.display.set_caption("Card Game")
pygame.init()

vol = 1.0

def main():
    
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    #Game.start()
    GameLoop.start()

if __name__ == "__main__":
    main()
    