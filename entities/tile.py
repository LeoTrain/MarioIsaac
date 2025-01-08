import pygame
from typing import Tuple
from pygame import Surface
from pygame.math import Vector2


class Tile(pygame.sprite.Sprite):
    def __init__(self, display, image:Surface=Surface((128, 128)), set_position:Vector2=Vector2(0, 0)):
        super().__init__()
        self.display = display
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(set_position.x, set_position.y))
        self.inflated_rect = self.rect.inflate(-(self.rect.width / 2), -(self.rect.height / 2))
        self.old_rect = self.rect.copy()
        self.max_offset = 200
        self.draw_rect_border = False
        self.color_mask = False

        self.position = set_position
        @property
        def position(self):
            return self._value

        @position.setter
        def position(self, new_value:Vector2):
            self._value = new_value
            self.rect.topleft = (int(self.position.x), int(self.position.y))

    def draw_mask(self, offset_x, offset_y, color=(128, 0, 128)):
        mask_surface = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
        width, height = self.mask.get_size()
        for x in range(width):
            for y in range(height):
                if self.mask.get_at((x, y)):
                    mask_surface.set_at((x, y), color)
        self.display.blit(
            mask_surface, (self.rect.x - offset_x, self.rect.y - offset_y)
        )

    def draw(self, offset_x, offset_y):
        self.display.blit(self.image, (self.rect.x - offset_x, self.rect.y - offset_y))
        if self.draw_rect_border:
            pygame.draw.rect(self.display, (255, 0, 0), self.rect.move(-offset_x, -offset_y), 1)
            pygame.draw.rect(self.display, (0, 255, 0), self.inflated_rect.move(-offset_x, -offset_y), 1)
        if self.color_mask:
            self.draw_mask(offset_x, offset_y)

    def update_old_rect(self):
        self.old_rect = self.rect.copy()

    def _update_rectangle(self) -> None:
        self.rect.x = int(self.position.x)
        self.rect.y = int(self.position.y)
        self.inflated_rect = self.rect.inflate(-(self.rect.width / 2), -(self.rect.height / 2))
