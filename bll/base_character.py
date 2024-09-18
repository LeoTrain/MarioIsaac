from ..bll.moving_tile import MovingTile
from ..bll.sprite_loader import SpriteLoader
from ..bll.animation_controller import AnimationController


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
