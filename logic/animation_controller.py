import pygame
from pygame.math import Vector2
from ..helpers.directions import Directions


class AnimationController:
    def __init__(self, sprite_loader, entity):

        self.current_frame_index = 0
        self.sprite_frames = entity.number_of_frames
        self.sprites = sprite_loader.load_character_sprites(
            entity.number_of_frames,
            entity.sprite_widths,
            entity.sprite_heights
        )
        self.entity = entity

    def get_current_direction_index(self, direction:Vector2):
        directions = {
            "down": 0,
            "up": 1,
            "left": 2,
            "right": 3
        }
        return directions[Directions.to_string(direction)]

    def increment_frame(self):
        current_state = self.entity.current_state
        current_direction_index = self.get_current_direction_index(self.entity.last_pressed_direction)
        total_frames = self.entity.frame_counts[current_state][current_direction_index] * self.sprite_frames[current_state][current_direction_index]
        self.current_frame_index = (self.current_frame_index + 1) % total_frames

    def select_state_image(self):
        if (self.entity.isEnemy() and self.entity.current_state == "attack"):
            pass
        frame_count = self.entity.frame_counts[self.entity.current_state][0]
        state_key = f"{self.entity.current_state}_{Directions.to_string(self.entity.last_pressed_direction)}"
        self.entity.image = self.sprites[state_key][self.current_frame_index // frame_count]

    def _update_mask(self):
        self.entity.mask = pygame.mask.from_surface(self.entity.image)

    def _update_rectangle(self):
        old_center = self.entity.rect.center
        self.entity.rect = self.entity.image.get_rect()
        self.entity.rect.center = old_center

    def update_sprite(self):
        self.increment_frame()
        self.select_state_image()
        self._update_mask()
        self._update_rectangle()
