from circleshape import CircleShape
import pygame
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white",(self.position.x,self.position.y),self.radius,width=2)
        return super().draw(screen)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # Split the asteroid into two smaller asteroids
        random_angle = random.uniform(20, 50)

        new_vector_pos = self.velocity.rotate(random_angle)
        new_vector_neg = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x,  self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x,  self.position.y, new_radius)
        asteroid1.velocity = new_vector_pos * 1.2
        asteroid2.velocity = new_vector_neg * 1.2

  

'''
        random_angle = random.uniform(20, 50)
        new_vector_pos = pygame.Vector2(self.position.x, self.position.y).rotate(random_angle)
        new_vector_neg = pygame.Vector2(self.position.x, self.position.y).rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x + new_vector_pos.x ,  self.position.y + new_vector_pos.y, new_radius)
        asteroid2 = Asteroid(self.position.x + new_vector_neg.x ,  self.position.y + new_vector_neg.y, new_radius)
        asteroid1.velocity = self.velocity.rotate(random_angle) * 1.2
        asteroid2.velocity = self.velocity.rotate(-random_angle) * 1.2 *
'''