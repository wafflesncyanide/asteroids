import pygame # type: ignore
from constants import *
from player import Player

def main():
    pygame.init()
    clockspeed = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    while True:
        screen.fill(000)
        player.update(dt)
        player.draw(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.display.flip()
        dt = clockspeed.tick(60) / 1000


if __name__ == "__main__":
    main()
