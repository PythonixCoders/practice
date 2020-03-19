import sys
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
        self.display = pygame.Surface((5000, 5000))
        pygame.display.set_caption("Racing Game")
        self.background = (255, 255, 255)

        self.p = Car((self.width / 2, self.height / 2))

    def input(self, keys):
        rot_speed = 4
        acc = 2

        if keys[pygame.K_LEFT]:
            self.p.hdg -= rot_speed
        if keys[pygame.K_RIGHT]:
            self.p.hdg += rot_speed

        if keys[pygame.K_UP]:
            self.p.accelerating = True
            self.p.speed += acc
        elif keys[pygame.K_DOWN]:
            self.p.accelerating = True
            self.p.speed -= acc
        else:
            self.p.accelerating = False

    def logic(self, delta):
        self.p.apply_friction(0.96)
        self.p.update(delta)

    def render(self, window, disp):
        self.display.fill(self.background)
        window.fill(self.background)

        self.p.render(disp)

        window.blit(disp, (0, 0))
        pygame.display.update()


def main():
    pygame.init()
    g = Game((1200, 800))
    clock = pygame.time.Clock()
    fps = 60

    while True:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        g.input(pygame.key.get_pressed())
        g.logic(clock.get_time() / 1000)
        g.render(g.win, g.display)


if __name__ == "__main__":
    main()
    sys.exit()
