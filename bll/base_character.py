import pygame

from ..bll.moving_tile import MovingTile
from ..bll.sprite_loader import SpriteLoader
from ..bll.animation_controller import AnimationController
from ..bll.event_dick import event_dick


class BaseCharacter(MovingTile, SpriteLoader, AnimationController):
    def __init__(self, display, sprite_sheet_path):
        super().__init__(display)
        SpriteLoader.__init__(self, sprite_sheet_path)
        AnimationController.__init__(self)

        self.life_points = 0
        self.attack_power = 0
        self.attack_range = 0

    def attack(self):
        self.current_state = "attack"

    def take_damage(self, damage):
        from ..bll.player import Player
        from ..bll.goblin import Goblin
        self.life_points -= damage
        if self.life_points <= 0:
            if isinstance(self, Player):
                event = pygame.event.Event(event_dick["player_dead"])
                pygame.event.post(event)
            elif isinstance(self, Goblin):
                event = pygame.event.Event(event_dick["enemy_dead"])
                pygame.event.post(event)
