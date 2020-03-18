import sys
from random import randint
import pygame
from car import Car


class Game:
    """
    Game class

    Arguments:
        size {tuple} -- window size
    """

    def __init__(self, size):
        self.width = size[0]
        self.height = size[1]
        self.win = pygame.display.set_mode(size)
        pygame.display.set_caption("Racing Game")
        self.background = (255, 255, 255)

        self.p = Car((self.width / 2, self.height / 2))
        self.p.speed = 2
        self.p.hdg = randint(0, 360)

    def input(self, keys):
        pass

    def logic(self, delta):
        self.p.update(delta)

    def render(self, window):
        window.fill(self.background)

        self.p.render(window)

        pygame.display.update()


def main():
    pygame.init()
    g = Game((1024, 720))
    clock = pygame.time.Clock()
    fps = 60

    while True:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        g.input(pygame.key.get_pressed())
        g.logic(clock.get_time() / 1000)
        g.render(g.win)


if __name__ == "__main__":
    main()
    sys.exit()
