import pygame
from constants import *
from circleshape import CircleShape
from player import Player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((0,0,0))

    clock = pygame.time.Clock()
    dt = 0

    p1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60)/1000

        screen.fill((0,0,0))
        p1.update(dt)
        p1.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
