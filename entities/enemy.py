import time

from ..entities.base_character import BaseCharacter


class Enemy(BaseCharacter):
    def __init__(self, display, sprite_sheet):
        super().__init__(display, sprite_sheet)

    def _is_in_attack_range(self, player_pos):
        in_range = False
        if (
            abs(self.rect.x - player_pos[0]) <= self.attack_range
            and abs(self.rect.y - player_pos[1]) <= self.attack_range
        ):
            in_range = True
        return in_range

    def move_to_player(self, player_pos):
        if player_pos[0] < self.rect.x:
            x_direction = -1
            self.current_x_direction = "left"
        elif player_pos[0] > self.rect.x:
            x_direction = 1
            self.current_x_direction = "right"
        else:
            x_direction = 0

        if player_pos[1] < self.rect.y:
            y_direction = -1
            self.current_y_direction = "up"
        elif player_pos[1] > self.rect.y:
            y_direction = 1
            self.current_y_direction = "down"
        else:
            y_direction = 0

        self.move(x_direction, y_direction)
        self.current_state = "run"

    def can_attack(self):
        can_attack = False
        time_passed = time.time() - self.attack_start_time
        if time_passed > 2:
            can_attack = True
        return can_attack

    def attack(self, player):
        super().attack()
        self.attack_start_time = time.time()
        player.take_damage(self.attack_power)

    def update(self, player_pos):
        self.move_to_player(player_pos)
        self.animation_controller.update_sprite()
