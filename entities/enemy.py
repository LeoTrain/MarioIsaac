import time
import math

from pygame.math import Vector2
from ..helpers.directions import Directions
from ..entities.base_character import BaseCharacter


class Enemy(BaseCharacter):
    def __init__(self, display, sprite_sheet, set_position:Vector2=Vector2(0, 0)):
        super().__init__(display, sprite_sheet, set_position)

    def _is_in_attack_range(self, player_pos):
        in_range = False
        if (
            abs(self.rect.x - player_pos[0]) <= self.attack_range
            and abs(self.rect.y - player_pos[1]) <= self.attack_range):
            in_range = True
        return in_range

    def move_to_player(self, player_pos:Vector2) -> None:
        if self.can_move:
            direction = player_pos - self.position
            if direction.length() > 0:
                direction = direction.normalize()

            if direction.x < 0:
                self.current_direction = Directions.LEFT
            elif direction.x > 0:
                self.current_direction = Directions.RIGHT
            if direction.y < 0:
                self.current_direction = Directions.UP
            elif direction.y > 0:
                self.current_direction = Directions.DOWN

            self.move(direction)
            self.current_state = "run"

    def try_attack(self, player):
        if self.can_attack(player):
            self.attack()
            player.take_damage(self.attack_power)

    def can_attack(self, player):
        can_attack = False
        time_passed = time.time() - self.attack_start_time
        if time_passed > 2 and self.isCloseEnough(player, self.rect.width):
            can_attack = True
        return can_attack

    def isCloseEnough(self, player, threshold):
        return math.sqrt((player.rect.centerx - self.rect.centerx)**2 + (player.rect.centery - self.rect.centery)**2) < threshold

    def attack(self) -> None:
        super().attack()
        self.attack_start_time = time.time()

    def isEnemy(self) -> bool:
        return True

    def updateSprite(self):
        self.animation_controller.update_sprite()
