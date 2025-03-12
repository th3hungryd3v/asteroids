# This allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() # Clock Object
    dt = 0 # Delta Time Variable Initialized

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return

        screen.fill((0, 0, 0)) # (Red, Green, Blue)

    pygame.display.flip()
    
    dt = clock.tick(60) / 1000 # Tick at the end of each iteration, get delta time and update dt

if __name__ == "__main__":
    main()