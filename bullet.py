import pygame
from ship import Ship

class Bullet(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.screen=game.screen
        self.ship = game.ship 
        self.screen_rect=game.screen.get_rect()

        


        self.image=pygame.image.load("bullet.png").convert_alpha()
        self.rect = self.image.get_rect()

   # Start the bullet at the midbottom of the ship's rect.
        self.rect.midbottom = self.ship.rect.midtop  # Assuming the ship has a rect attribute
        
        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

        # Bullet speed (modify this value as needed).
        self.speed = 5.0

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.speed
        # Update the rect position.
        self.rect.y = self.y

    def blitme(self):
        """Draw the bullet at its current location."""
        self.screen.blit(self.image, self.rect)