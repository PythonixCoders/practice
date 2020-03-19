import os
from math import cos, sin, radians
import pygame


class Car:
    """
    Class for making a car.

    Arguments:
        pos {tuple} -- starting position of cars
    """

    def __init__(self, pos):
        self.img = pygame.image.load(os.path.join("data", "racecar.png"))

        self.x = pos[0]
        self.y = pos[1]
        self.x_vel = 0
        self.y_vel = 0

        ratio_mult = 0.7
        self.size = (int(135 * ratio_mult), int(64 * ratio_mult))
        self.speed = 0 # It's really the acceleration of the car :p
        self.hdg = 0
        self.rect = self.img.get_rect()

        self.accelerating = False

    def apply_friction(self, friction):
        self.speed *= friction
        self.x_vel *= friction
        self.y_vel *= friction

    def update(self, delta):
        if self.accelerating:
            self.x_vel += cos(radians(self.hdg)) * self.speed
            self.y_vel += sin(radians(self.hdg)) * self.speed

        self.x += self.x_vel * delta
        self.y += self.y_vel * delta

    def render(self, window):
        transformed = pygame.transform.rotate(
            pygame.transform.scale(self.img, self.size),
            -self.hdg
        )
        size = transformed.get_size()
        window.blit(transformed, (self.x - size[0] / 2, self.y - size[1] / 2))
        self.rect = transformed.get_rect()
