import pygame

from circleshape import CircleShape
from constants import (
    LINE_WIDTH,
    PLAYER_RADIUS,
    PLAYER_SHOOT_COOLDOWN_SECONDS,
    PLAYER_SHOT_SPEED,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
    SHORT_RADIUS,
)
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen, color="white"):
        pygame.draw.polygon(screen, color, self.triangle(), LINE_WIDTH)

    def rotate(self, dt, angle_offset=0):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.shot_cooldown_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotation = 90
            self.move(dt)
        if keys[pygame.K_d]:
            self.rotation = -90
            self.move(dt)
        if keys[pygame.K_w]:
            self.rotation = 180
            self.move(dt)
        if keys[pygame.K_s]:
            self.rotation = 0
            self.move(dt)

        if keys[pygame.K_SPACE]:
            if self.shot_cooldown_timer <= 0:
                self.shoot()
                self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(self.position.x, self.position.y, SHORT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
