# Run this at the root, before working on this repo = source venv/bin/activate
# This allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() # Clock Object
    dt = 0 # Delta Time Variable Initialized
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    rockables = pygame.sprite.Group()

    # Player containers
    Player.containers = (updatable, drawable)
    # Instantiate Player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
                return
        # updatable
        updatable.update(dt)

        screen.fill("black") # (Red, Green, Blue)
        # drawable
        for drawable_object in drawable:
            drawable_object.draw(screen)
        pygame.display.flip()
    
        dt = clock.tick(60) / 1000 # Tick at the end of each iteration, get delta time and update dt

if __name__ == "__main__":
    main()