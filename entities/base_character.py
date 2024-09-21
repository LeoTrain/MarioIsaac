import pygame

from ..entities.moving_tile import MovingTile
from ..logic.sprite_loader import SpriteLoader
from ..logic.animation_controller import AnimationController
from ..logic.event_dick import event_dick


class BaseCharacter(MovingTile):
    def __init__(self, display, sprite_sheet_path):
        super().__init__(display)
        self.sprite_loader = SpriteLoader(sprite_sheet_path)
        self.animation_controller = AnimationController(self.sprite_loader, self)
        self.sprites = self.sprite_loader.load_character_sprites(self.number_of_frames, self.sprite_widths, self.sprite_heights)

        self.life_points = 0
        self.attack_power = 0
        self.attack_range = 0

        self.current_state = "idle"
        self.current_x_direction = "right"
        self.current_y_direction = "down"

    def attack(self):
        self.current_state = "attack"

    def take_damage(self, damage):
        from ..entities.player import Player
        from ..entities.goblin import Goblin
        self.life_points -= damage
        if self.life_points <= 0:
            if isinstance(self, Player):
                event = pygame.event.Event(event_dick["player_dead"])
                pygame.event.post(event)
            elif isinstance(self, Goblin):
                event = pygame.event.Event(event_dick["enemy_dead"])
                pygame.event.post(event)
