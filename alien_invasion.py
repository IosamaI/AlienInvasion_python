import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
from bullet import Bullet
from backg import Backg
from pygame import mixer

import random

class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.score_value = 0
            # Load the background music using the correct method
        mixer.music.load("background.wav")
         # Load the laser sound effect
        self.laser_sound = mixer.Sound("laser.wav")
        self.explosion_sound = mixer.Sound("explosion.wav")
        mixer.music.play(-1)
        self.clock = pygame.time.Clock()
        self.settings=Settings()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.backg=Backg(self)
        self.ship = Ship(self)
        self.bullet= Bullet(self)
        self.alien = Alien(self)
        self.font =pygame.font.Font(None,50)
        self.fFont = pygame.font.Font(None,128)
        self.level1 = pygame.font.Font(None,128)
        self.level2 = pygame.font.Font(None,128)
        self.level3 = pygame.font.Font(None,128)
        self.level4 = pygame.font.Font(None,128)
        self.level5 = pygame.font.Font(None,128)
        pygame.display.set_caption("Alien Invasion")

        self.bullets = pygame.sprite.Group()
        
        # Create a group to hold multiple aliens
        self.aliens= pygame.sprite.Group()

         # Create a sprite group for the ship
        self.ship_group = pygame.sprite.Group()
        self.ship_group.add(self.ship)
        
             # Initialize timer variables
        self.last_alien_spawn_time = pygame.time.get_ticks()
        self.alien_spawn_interval = 1000  # 1 seconds
        self.update_score()
        

    def run_game(self):
        while True:
          self._check_events()
          self.ship.update()
          self.update_aliens()
          self.update_bullets()

          self.check_collisions()
          self.time()
          self._update_screen()
          self.clock.tick(100)

    def time(self):
        """Check if it’s time to spawn a new alien."""
        current_time = pygame.time.get_ticks()
        if current_time - self.last_alien_spawn_time > self.alien_spawn_interval:
            self.create_aliens()
            self.last_alien_spawn_time = current_time

            




    def check_collisions(self):
        """Check for collisions between bullets and aliens."""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            # You can add code here to handle what happens when an alien is hit
           self.explosion_sound.play()
           self.score_value += len(collisions) # Increment score
           self.update_score()# Update the score surface
           self.adjust_spawn_rate()

    def adjust_spawn_rate(self):
        """Adjust alien spawn rate based on the score."""
        if self.score_value == 70:
            self.alien_spawn_interval = 60
            self.over5 = self.level5.render("LEVEL 1", True, (255, 255, 255))
            self.screen.blit(self.over5, (self.screen.get_width() // 2 - self.over5.get_width() // 2, self.screen.get_height() // 2 - self.over5.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(2000)
        elif self.score_value == 60:
            self.alien_spawn_interval = 600  # Increase difficulty
            self.over4 = self.level4.render("LEVEL 4", True, (255, 255, 255))
            self.screen.blit(self.over4, (self.screen.get_width() // 2 - self.over4.get_width() // 2, self.screen.get_height() // 2 - self.over4.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(2000)
        elif self.score_value == 40:
            self.alien_spawn_interval = 700
            self.over3 = self.level3.render("LEVEL 3", True, (255, 0, 0))
            self.screen.blit(self.over3, (self.screen.get_width() // 2 - self.over3.get_width() // 2, self.screen.get_height() // 2 - self.over3.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(2000)

        elif self.score_value == 20:
            self.alien_spawn_interval = 800
            self.over2 = self.level2.render("LEVEL 2", True, (255, 0, 0))
            self.screen.blit(self.over2, (self.screen.get_width() // 2 - self.over2.get_width() // 2, self.screen.get_height() // 2 - self.over2.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(2000)
        elif self.score_value == 10:
             self.alien_spawn_interval = 900
             self.over1 = self.level1.render("LEVEL 1", True, (255, 0, 0))
             self.screen.blit(self.over1, (self.screen.get_width() // 2 - self.over1.get_width() // 2, self.screen.get_height() // 2 - self.over1.get_height() // 2))
             pygame.display.update()
             pygame.time.delay(2000)
         

    def update_score(self):
        """Update the score surface."""
        self.score = self.font.render(f"Score: {self.score_value}", True, (255, 255, 255))


    def update_aliens(self):
        """Update the position of aliens and handle collisions with the ship."""
        self.aliens.update()
        for alien in self.aliens.copy():
            if alien.rect.top >= self.screen.get_height():
                self.aliens.remove(alien)
            if pygame.sprite.spritecollideany(alien, self.ship_group):
                self.ship_hit()



    def ship_hit(self):
        """Handle the event when an alien hits the ship."""
        # Implement what should happen when the ship is hit, e.g., end the game
        """Handle the event when an alien hits the ship."""
        self.over = self.fFont.render("GAME OVER", True, (255, 0, 0))
        self.screen.blit(self.over, (self.screen.get_width() // 2 - self.over.get_width() // 2, self.screen.get_height() // 2 - self.over.get_height() // 2))
        pygame.display.update()
        pygame.time.delay(2000)  # Display "GAME OVER" for 2 seconds before quitting
        pygame.quit()
        sys.exit()


    def fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        self.laser_sound.play()  # Play the laser sound effect
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def update_bullets(self):
        """Update the position of bullets and remove off-screen bullets."""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)



    def create_aliens(self):

        #self.alien = Alien(self)
        # for i in range(5):
            
        alien = Alien(self)
        alien.rect.x = random.randint(0, self.screen.get_width() - self.alien.rect.width)
        # print(self.alien.rect.width)
        alien.rect.y = random.randint(-100, 0)  # Random starting y position
        if pygame.sprite.spritecollideany(alien, self.aliens):
            self.create_aliens()

        else: 
            alien.moving_down = True
            self.aliens.add(alien)


    def _check_events(self):
            """Respond to keypresses and mouse events."""
        # Watch for keyboard and mouse events.
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.ship.moving_left =True
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    if event.key == pygame.K_SPACE:
                        self.fire_bullet()

                    if event.key == pygame.K_q:
                        sys.exit()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.ship.moving_left=False
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right= False 
                

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.backg.blitme()
        self.ship.blitme()
        # self.alien.blitme()
        
        self.bullets.draw(self.screen)
        self.aliens.draw(self.screen)
        self.screen.blit(self.score ,(10,10))
        pygame.display.update()




        
if __name__ == '__main__':
 # Make a game instance, and run the game.
 ai = AlienInvasion()
 ai.run_game()
