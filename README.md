# Alien Invasion Game

![Alien Invasion (Ubuntu) 8_11_2024 2_24_50 PM](https://github.com/user-attachments/assets/8118d7db-a5fb-4b33-b2f2-8db47a835296)

## Overview

**Alien Invasion** is a side-scrolling shooter game where the player controls a spaceship, battling waves of aliens. The game increases in difficulty as the player's score increases, with faster alien spawn rates at higher levels. The goal is to achieve the highest score possible before the aliens overwhelm the player.

## Features

- Move the spaceship up and down to dodge aliens.
- Fire bullets to destroy incoming aliens.
- Increasing difficulty with faster alien spawn rates as the score increases.
- Sound effects for laser shots and explosions.
- Background music to enhance the gaming experience.

## Game Controls

- **Left Arrow (`←`)**: Move the spaceship left.
- **Right Arrow (`→`)**: Move the spaceship right.
- **Spacebar**: Fire bullets.
- **Q**: Quit the game.

## Installation

### Prerequisites

- Python 3.10+
- Pygame
- Pytest (for running tests)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/alien_invasion.git
   cd alien_invasion

## Project Structure

   alien_invasion/
├── alien_invasion.py        # Main game file
├── settings.py              # Game settings
├── ship.py                  # Ship class
├── alien.py                 # Alien class
├── bullet.py                # Bullet class
├── backg.py                 # Background class
├── test_AlienInvasion.py    # Pytest file for testing
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
└── assets/                  # Folder containing sound and image files
    ├── background.wav       # Background music
    ├── laser.wav            # Laser sound effect
    ├── explosion.wav        # Explosion sound effect
    └── spaceship.png        # Image of the spaceship

