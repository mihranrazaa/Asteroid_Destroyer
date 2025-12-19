"""
Project By - mihranrazaa
Date - 18-12-2025
License - None
Name - Not yet Decided :?
"""

import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from endscreen import end_screen
from logger import log_event, log_state
from player import Player
from shot import Shot


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    pygame.init()
    refresh = pygame.time.Clock()
    dt = 0
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    score = 0
    font = pygame.font.Font(None, 36)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        pygame.Surface.fill(screen, "black")
        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        for asteroid in list(asteroids):
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                end_screen(screen, score)
                sys.exit()
            for shot in list(shots):
                if shot.collides_with(asteroid):
                    if asteroid.alive() and shot.alive():
                        log_event("asteroid_shot")
                        score += 5
                        asteroid.split()
                        shot.kill()

        pygame.display.flip()
        dt = refresh.tick(60) / 1000.0


main()
