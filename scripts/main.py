import pygame
import sys
pygame.init()


class Game:
    def __init__(self, size):
        self.width = size[0]
        self.height = size[1]
        self.win = pygame.display.set_mode(size)
        pygame.display.set_caption("Racing Game")
        self.background = (0, 0, 0)

    def input(self, keys):
        pass

    def logic(self, delta):
        print(delta)

    def render(self, window):
        window.fill(self.background)

        pygame.draw.rect(window, (255, 255, 255), (100, 100, 50, 50))

        pygame.display.update()


def main():
    g = Game((800, 600))
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
