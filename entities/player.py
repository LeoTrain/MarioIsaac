import time
import pygame

from ..entities.base_character import BaseCharacter
from ..logic.experience import Xp


class Player(BaseCharacter):
    def __init__(self, display, sprite_sheet_path):
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
        super().__init__(display, sprite_sheet_path)
        self.image = self.sprites["idle_down"][0]
        self.speed = 5
        self.attack_counter = 0
        self.life_points = self.starting_life_points = 5
        self.attack_power = 3
        self.in_attack = False
        self.xp = Xp()
        self.attack_start_time = time.time()

    def set_direction(self, direction):
        self.last_pressed_direction = direction

    def can_attack(self):
        can_attack = False
        time_passed = time.time() - self.attack_start_time
        if time_passed > 2:
            can_attack = True
        return can_attack

    def attack(self, enemies):
        super().attack()
        self.attack_start_time = time.time()
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
                if enemy.life_points <= 0:
                    self.xp.add_xp(enemy.xp_value)

    def update(self):
        self.animation_controller.update_sprite()

    def draw_xp_bar(self, screen):
        bar_width = 200
        bar_height = 20
        bar_x = 50
        bar_y = 50
        background_color = (50, 50, 50)
        xp_color = (0, 0, 200)
        xp_ratio = self.xp.now_xp / self.xp.current_xp_cap
        pygame.draw.rect(
            screen, background_color, (bar_x, bar_y, bar_width, bar_height)
        )
        pygame.draw.rect(
            screen, xp_color, (bar_x, bar_y, bar_width * xp_ratio, bar_height)
        )
        font = pygame.font.SysFont(None, 30)
        level_text = font.render(f"Level: {self.xp.now_level}", True, (255, 255, 255))
        screen.blit(
            level_text, (bar_x, bar_y - 30)
        )
