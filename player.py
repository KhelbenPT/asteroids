from circleshape import *
from constants import *
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (255,255,255), self.triangle(),2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        
    def update(self, dt):
        self.shot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
           
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shot_timer <= 0:
            shot = Shot(self.position[0], self.position[1], self.rotation)
            self.shot_timer = PLAYER_SHOOT_COOLDOWN

class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y , SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 1)
        self.velocity = pygame.math.Vector2.rotate(self.velocity, rotation)
        self.velocity *= PLAYER_SHOOT_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position , SHOT_RADIUS,  2)

    def update(self, dt):
        self.position += self.velocity * dt