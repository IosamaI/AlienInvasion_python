import pygame

class Ship(pygame.sprite.Sprite):
     """A class to manage the ship."""

     def __init__(self,game):
          """Initialize the ship and set its starting position."""
          super().__init__()
          self.screen = game.screen
          self.screen_rect = game.screen.get_rect()
            # Movement flag; start with a ship that's not moving.
          self.moving_right = False
          self.moving_left = False
          


          # Load the ship image and get its rect.
          self.image = pygame.image.load('spaceship.png').convert_alpha()
          self.rect = self.image.get_rect()

          self.rect.midbottom = self.screen_rect.midbottom

     def update(self):
          if self.moving_right and self.rect.right < self.screen_rect.right:
               self.rect.right +=5
          
          if self.moving_left and self.rect.left > self.screen_rect.left:
               self.rect.left -=5

     def blitme(self):
         """Draw the ship at its current location."""
         self.screen.blit(self.image,self.rect)