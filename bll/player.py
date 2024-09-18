import pygame

from ..bll.base_character import BaseCharacter
from ..bll.event_dick import event_dick


class Player(BaseCharacter):
    def __init__(self, display, sprite_sheet_path):
        super().__init__(display, sprite_sheet_path)
        self.sprites = self.load_character_sprites(
            [48, 48, 48, 48, 48, 48],
            [48, 48, 48, 48, 48, 48],
            [12, 12, 8, 8, 8, 8]
        )
        self.image = self.sprites["idle_down_right"][0]
        self.speed = 5
        self.attack_counter = 0
        self.frame_counts = {
            "idle": 12,
            "run": 8,
            "attack": 8,
        }
        self.sprite_frames = {
            "idle": 12,
            "run": 8,
            "attack": 8,
        }
        self.life_points = self.starting_life_points = 5
        self.attack_power = 3

    def update_current_state(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_s]:
            self.current_state = "run"
        elif self.current_state == "attack":
            self.attack_counter += 1
            if self.attack_counter >= 15:
                self.attack_counter = 0
                self.current_state = "idle"
        else:
            self.current_state = "idle"

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
        self.update_current_state()
        self.update_sprite()
