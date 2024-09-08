# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # create env
        screen.fill("black")

        # set fps
        ms_dt = clock.tick(60)
        dt = ms_dt/1000

        player.update(dt)
        player.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()