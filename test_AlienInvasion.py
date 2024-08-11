import pytest
import pygame
from alien_invasion import AlienInvasion
from ship import Ship
from alien import Alien
from bullet import Bullet

@pytest.fixture
def game_instance():
    """Fixture to create a game instance for testing."""
    ai = AlienInvasion()
    return ai


def test_alien_spawn_rate_adjustment(game_instance):
    """Test alien spawn rate adjustment based on score."""
    game_instance.score_value = 10
    game_instance.adjust_spawn_rate()
    assert game_instance.alien_spawn_interval == 900

    game_instance.score_value = 20
    game_instance.adjust_spawn_rate()
    assert game_instance.alien_spawn_interval == 800

    game_instance.score_value = 40
    game_instance.adjust_spawn_rate()
    assert game_instance.alien_spawn_interval == 700

    game_instance.score_value = 60
    game_instance.adjust_spawn_rate()
    assert game_instance.alien_spawn_interval == 600

def test_check_collisions(game_instance):
    """Test collisions between bullets and aliens."""
    game_instance.fire_bullet()
    bullet = game_instance.bullets.sprites()[0]
    alien = Alien(game_instance)
    alien.rect.x = bullet.rect.x
    alien.rect.y = bullet.rect.y
    game_instance.aliens.add(alien)

    game_instance.check_collisions()
    assert len(game_instance.aliens) == 0
    assert game_instance.score_value == 1

def test_game_over(game_instance):
    """Test game over when the ship is hit."""
    alien = Alien(game_instance)
    alien.rect.midbottom = game_instance.ship.rect.midbottom
    game_instance.aliens.add(alien)

    with pytest.raises(SystemExit):
        game_instance.ship_hit()
