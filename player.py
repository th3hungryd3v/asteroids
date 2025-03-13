import pygame
from constants import PLAYER_RADIUS

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(PLAYER_RADIUS)
        pass