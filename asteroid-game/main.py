import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

import sys

# from database import connect_database, databse_version

from constants import *


def main():

    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clk = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        updatable.update(dt=dt)

        for obj in asteroids:
            if player.collide(obj):
                print("Game Over!")
                sys.exit("Game Over!")

        # player.draw(screen=screen)

        for drawable_object in drawable:
            drawable_object.draw(screen=screen)

        # player.update(dt=dt)

        pygame.display.flip()

        # limit frame rate to 60
        dt = clk.tick(60) / 1000


if __name__ == "__main__":
    main()
