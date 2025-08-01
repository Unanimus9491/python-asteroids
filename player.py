from circleshape import CircleShape
from constants import *
import pygame
from shot import Shot

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y, PLAYER_RADIUS)
        self.radius = PLAYER_RADIUS
        self.rotation = 0
        self.shoot_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen,"white",self.triangle(),width=2)
        return super().draw(screen)

    def rotate(self, dt):
        self.rotation += TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
       keys = pygame.key.get_pressed()
       if keys[pygame.K_a]:
           self.rotate(-dt)
       if keys[pygame.K_d]:
           self.rotate(dt)
       if keys[pygame.K_w]:
           self.move(-dt)
       if keys[pygame.K_s]:
           self.move(dt)
       if keys[pygame.K_SPACE]:
           self.shoot()
       self.shoot_timer -= dt
    
    def shoot(self):
        if self.shoot_timer <= 0:
            forward = pygame.Vector2(0, -1).rotate(self.rotation)
            shot = Shot(self.position.x - forward.x * self.radius, 
                        self.position.y - forward.y * self.radius)
            shot.velocity = forward * SHOT_SPEED
            self.shoot_timer = SHOT_COOL_DOWN
            return shot