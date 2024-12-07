from circleshape import CircleShape
import pygame
from constants import *
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
    def draw(self,screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            vel1 = self.velocity.rotate(random_angle)
            vel2 = self.velocity.rotate(-random_angle)
            vel1 *= 1.2
            vel2 *= 1.2
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            new_ast1 = Asteroid(self.position.x,self.position.y,new_rad)
            new_ast1.velocity = vel1
            new_ast2 = Asteroid(self.position.x,self.position.y,new_rad)
            new_ast2.velocity = vel2

