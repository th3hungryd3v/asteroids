import pygame
import random
from circleshapes import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "gray", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return # small asteroids -- no splitting
        new_radius = self.radius / 2
        random_angle = random.randint(20, 50)
        for angle in [random_angle, -random_angle]:
            new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            new_speed = random.randint(40, 100)
            new_direction = pygame.Vector2(1, 0).rotate(angle)
            new_asteroid_velocity = new_direction * new_speed
