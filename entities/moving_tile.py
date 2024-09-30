from ..entities.tile import Tile


class MovingTile(Tile):
    def __init__(self, display):
        super().__init__(display)
        self.speed = 0
        self.last_pressed_direction = "down"
        self.can_move_left = True
        self.can_move_right = True
        self.can_move_up = True
        self.can_move_down = True

    def move(self, dx, dy):
        self.update_old_rect()

        if dx < 0:
            if self.can_move_left:
                self.rect.x += dx * self.speed
        elif dx > 0:
            if self.can_move_right:
                self.rect.x += dx * self.speed
        else:
            self.rect.x += dx * self.speed

        if dy < 0:
            if self.can_move_up:
                self.rect.y += dy * self.speed
        elif dy > 0:
            if self.can_move_down:
                self.rect.y += dy * self.speed               
        else:
            self.rect.y += dy * self.speed
