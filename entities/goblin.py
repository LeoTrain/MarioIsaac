import pygame
import random
import time

from typing import Dict
from ..entities.enemy import Enemy
from pygame.math import Vector2


class Goblin(Enemy):
    def __init__(self, display, sprite_sheet_path, set_position:Vector2):
        self.number_of_frames = {
            "idle": [4, 4, 4, 4],
            "run": [8, 8, 8, 8],
            "attack": [8, 8, 8, 8],
        }
        self.frame_counts = {
            "idle": [4, 4, 4, 4],
            "run": [8, 8, 8, 8],
            "attack": [10, 10, 10, 10],
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
        super().__init__(display, sprite_sheet_path, set_position)

        self.image = self.sprites["idle_down"][0]
        self.current_frame_index = 0
        self.speed = 3
        self.life_points = self.max_life_points = random.randint(5, 8)
        self.attack_range = 100
        self.attack_power = 1
        self.attack_start_time = time.time()
        self.xp_value = self.life_points + random.randint(1, 3)
        self.velocity = 0.6
        self.sounds = self._init_sounds()

    def _init_sounds(self) -> Dict[str, pygame.mixer.Sound]:
        assets_path = "MarioIsaac/assets/sounds/orc/"
        damage_sounds = [assets_path + "orc_taking_damage1.wav", assets_path+"orc_taking_damage2.wav", assets_path+"orc_taking_damage3.wav"]
        sounds = {
            "damageTaken": pygame.mixer.Sound(damage_sounds[random.randint(1, len(damage_sounds)-1)])
        }
        return sounds

    def take_damage(self, damage):
        self.sounds["damageTaken"].play()
        return super().take_damage(damage)

    def with_position(self, position):
        self.rect.topleft = position
        return self
