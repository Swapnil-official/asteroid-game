import pygame

# from database import connect_database, databse_version

from constants import *


def main():

    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clk = pygame.time.Clock
    dt = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        pygame.display.flip()

        delta = clk().tick(60)

        print(delta)

        dt = delta / 1000

        print(dt)


if __name__ == "__main__":
    main()
