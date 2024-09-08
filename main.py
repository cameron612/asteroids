# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    hazards = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, hazards)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()
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

        for thing in updatable:
            thing.update(dt)
        
        for hazard in hazards:
            if hazard.hasCollided(player):
                print("Game over!")
                exit(0)
            
            for shot in shots:
                if hazard.hasCollided(shot):
                    hazard.split()

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()