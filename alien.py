import pygame
import random

class Alien(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.screen=game.screen
        self.screen_rect=game.screen.get_rect()

        # Movement flag; start with a alien that's not moving.
        self.moving_down = False


        self.image=pygame.image.load("alien.png").convert_alpha()
        self.rect = self.image.get_rect()

        # Randomize the horizontal position (x) while keeping the alien at the top (y)
        self.rect.x = random.randint(0, self.screen_rect.width + self.rect.width)
        self.rect.y = 0  # Keep the alien at the top of the screen
        

    def update(self):
        if self.moving_down:
            self.rect.y += 2



    # def blitme(self):
    #     self.screen.blit(self.image,self.rect)
