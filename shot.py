from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.radius = SHOT_RADIUS


    def draw(self, screen):
        pygame.draw.circle(screen,"white",(self.position.x,self.position.y),self.radius,width=2)
        return super().draw(screen)


    def update(self, dt):
        self.position += self.velocity * -dt
