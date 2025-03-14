import pygame
from circleshapes import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius ) # without the parameter it defaults to "width=0" and the circle is 'filled' by default

    def update(self, dt):
        self.position += self.velocity * dt