import time
import pygame

from typing import Dict
from pygame.math import Vector2
from ..entities.base_character import BaseCharacter
from ..logic.experience import Xp
from ..helpers.directions import Directions


class Player(BaseCharacter):
    def __init__(self, display, sprite_sheet_path, set_position:Vector2=Vector2(0, 0)):
        self.number_of_frames = {
            "idle": [12, 4, 12, 12],
            "run": [8, 8, 8, 8],
            "attack": [8, 8, 8, 8],
        }
        self.frame_counts = {
            "idle": [12, 4, 12, 12],
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
        super().__init__(display, sprite_sheet_path, set_position)
        self.image = self.sprites["idle_down"][0]
        self.speed = 5
        self.velocity = 0.8
        self.attack_counter = 0
        self.life_points = self.max_life_points = 5
        self.attack_power = 3
        self.in_attack = False
        self.xp = Xp()
        self.attack_start_time = time.time()
        self.sounds = self._init_sounds()

    def _init_sounds(self) -> Dict[str, pygame.mixer.Sound]:
        sounds = {
            "attack": pygame.mixer.Sound("MarioIsaac/assets/sounds/sword/sword_stab_sound.mp3")
        }
        return sounds

    def set_direction(self, direction:Vector2):
        self.last_pressed_direction = direction

    def can_attack(self):
        can_attack = False
        time_passed = time.time() - self.attack_start_time
        if time_passed > 2:
            can_attack = True
        return can_attack

    def attack(self, enemies):
        super().attack()
        self.sounds["attack"].play()
        self.attack_start_time = time.time()
        attack_rect = self.rect.copy()
        attack_size = 20

        if self.last_pressed_direction == Directions.LEFT:
            attack_rect.width += attack_size
            attack_rect.x -= attack_size
        elif self.last_pressed_direction == Directions.RIGHT:
            attack_rect.width += attack_size
        elif self.last_pressed_direction == Directions.UP:
            attack_rect.height += attack_size
            attack_rect.y -= attack_size
        elif self.last_pressed_direction == Directions.DOWN:
            attack_rect.height += attack_size

        for enemy in enemies:
            if attack_rect.colliderect(enemy.rect):
                enemy.take_damage(self.attack_power)
                if enemy.life_points <= 0:
                    self.xp.add_xp(enemy.xp_value)

    def updateSprite(self):
        self.animation_controller.update_sprite()

    def draw_xp_bar(self, screen):
        bar_width = 200
        bar_height = 20
        bar_x = 50
        bar_y = 50
        background_color = (50, 50, 50)
        xp_color = (0, 0, 200)
        xp_ratio = self.xp.now_xp / self.xp.current_xp_cap
        pygame.draw.rect(screen, background_color, (bar_x, bar_y, bar_width, bar_height))
        pygame.draw.rect(screen, xp_color, (bar_x, bar_y, bar_width * xp_ratio, bar_height))
        font = pygame.font.SysFont(None, 30)
        level_text = font.render(f"Level: {self.xp.now_level}", True, (255, 255, 255))
        screen.blit(level_text, (bar_x, bar_y - 30))

    def isPlayer(self) -> bool:
        return True
