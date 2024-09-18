from ..bll.tile import Tile


class MovingTile(Tile):
    def __init__(self, display):
        super().__init__(display)
        self.speed = 0
        self.last_pressed_direction = None

    def move(self, dx, dy):
        self.update_old_rect()
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
