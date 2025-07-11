import pygame # type: ignore
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clockspeed = pygame.time.Clock()
    dt = 0
    asteroids = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updateable, drawable)
    AsteroidField.containers = (updateable)
    Asteroid.containers = (asteroids, updateable, drawable)
    Player.containers = (updateable, drawable)
    asteroid_field = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    

    while True:
        screen.fill(000)
        updateable.update(dt)
        for thing in drawable:
            thing.draw(screen)
        for rock in asteroids:
            if rock.collision(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collision(rock):
                    shot.kill()
                    rock.split()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.display.flip()
        dt = clockspeed.tick(60) / 1000


if __name__ == "__main__":
    main()
