"""
Project By - mihranrazaa
Date - 18-12-2025
License - MIT License
Copyright (c) 2025 mihranrazaa
Name - Asteroid Destroyer? (yay name!)
"""

import pygame
from pygame import mixer

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from endscreen import end_screen
from logger import log_event, log_state
from player import Player
from resource_path import resource_path
from shot import Shot
from sound import init_sounds


def game_loop(screen, font):
    score = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroid_field = AsteroidField()

    refresh = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        # Increase difficulty based on score
        asteroid_field.update_difficulty(score)

        log_state()

        if score >= 400:
            bg_color = "white"
            fg_color = "black"
        else:
            bg_color = "black"
            fg_color = "white"

        pygame.Surface.fill(screen, bg_color)
        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen, color=fg_color)
        score_text = font.render(f"Score: {score}", True, fg_color)
        screen.blit(score_text, (10, 10))
        if pygame.key.get_pressed()[pygame.K_m]:
            mixer.music.pause()
        if pygame.key.get_pressed()[pygame.K_n]:
            mixer.music.unpause()
        for asteroid in list(asteroids):
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                return end_screen(screen, score)
            for shot in list(shots):
                if shot.collides_with(asteroid):
                    if asteroid.alive() and shot.alive():
                        log_event("asteroid_shot")
                        score += 5
                        asteroid.split()
                        shot.kill()

        pygame.display.flip()
        dt = refresh.tick(60) / 1000.0


def main():
    print(f"Starting Asteroid Destroyer!!! with pygame version: {pygame.version.ver}")
    print("HOPE YOU ENJOY THIS GAME :) ~ MIHRANRAZAA")
    print("https://github.com/mihranrazaa/Asteroid_Destroyer")
    pygame.init()
    mixer.init()
    init_sounds()
    pygame.mixer.music.load(resource_path("assets/music.wav"))
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font(None, 36)

    while True:
        if not game_loop(screen, font):
            break


main()
