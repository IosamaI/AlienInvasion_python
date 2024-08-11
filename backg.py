import pygame

class Backg():
    def __init__(self,game):
        self.screen=game.screen


        self.image=pygame.image.load("vecteezy_a-banner-outer-space-scence-background_.jpg").convert_alpha()

    


    def blitme(self):
        self.screen.blit(self.image,(0,0))
