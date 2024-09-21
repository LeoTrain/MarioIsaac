import pygame

from ..entities.base_character import BaseCharacter


class Player(BaseCharacter):
    def __init__(self, display, sprite_sheet_path):
        self.number_of_frames = {
            "idle": [12, 12, 12, 4],
            "run": [8, 8, 8, 8],
            "attack": [8, 8, 8, 8],
        }
        self.sprite_widths = {
            "idle": [64, 64, 64, 64],
            "run": [64, 64, 64, 64],
            "attack": [64, 64, 64, 64],
        }
        self.sprite_heights = {
            "idle": [64, 64, 64, 64],
            "run": [64, 64, 64, 64],
            "attack": [64, 64, 64, 64],
        }
        super().__init__(display, sprite_sheet_path)

        self.image = self.sprites["idle_down"][0]
        self.speed = 5
        self.attack_counter = 0
        self.life_points = self.starting_life_points = 5
        self.attack_power = 3

    def set_direction(self, direction):
        self.last_pressed_direction = direction

    def attack(self, enemies):
        super().attack()
        attack_rect = self.rect.copy()
        attack_size = 20

        if self.last_pressed_direction == "left":
            attack_rect.width += attack_size
            attack_rect.x -= attack_size
        elif self.last_pressed_direction == "right":
            attack_rect.width += attack_size
        elif self.last_pressed_direction == "up":
            attack_rect.height += attack_size
            attack_rect.y -= attack_size
        elif self.last_pressed_direction == "down":
            attack_rect.height += attack_size

        for enemy in enemies:
            if attack_rect.colliderect(enemy.rect):
                enemy.take_damage(self.attack_power)

    def update(self):
        self.update_sprite()
