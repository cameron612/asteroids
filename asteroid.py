from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            angle_delta = random.uniform(20, 50)
            first_vel = self.velocity.rotate(angle_delta)
            second_vel = self.velocity.rotate(-angle_delta)
            updated_radius = self.radius - ASTEROID_MIN_RADIUS

            first = Asteroid(self.position.x, self.position.y, updated_radius)
            first.velocity = first_vel * 1.2

            second = Asteroid(self.position.x, self.position.y, updated_radius)
            second.velocity = second_vel * 1.2

        