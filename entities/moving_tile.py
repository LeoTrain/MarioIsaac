from pygame.mixer_music import set_pos
from ..entities.tile import Tile
from ..helpers.directions import Directions
from pygame.math import Vector2


class MovingTile(Tile):
    def __init__(self, display, set_position:Vector2):
        super().__init__(display, set_position=set_position)
        self.speed = 0
        self.acceleration = 1
        self.last_pressed_direction = Directions.DOWN
        self.can_move_left = True
        self.can_move_right = True
        self.can_move_up = True
        self.can_move_down = True
        self.can_move = True
        self.is_colliding = False

    def move(self, direction:Vector2=Directions.LEFT):
        if (self.can_move):
            self.update_old_rect()
            # x = x0+v0*t+ 1/2*a*t^2
            speed = Vector2(direction.x*self.speed, direction.y*self.speed) * 1
            acceleration = Vector2(direction.x*self.acceleration, direction.y*self.acceleration) / 2 * (1**2)
            self.position += speed + acceleration
            self._update_rectangle()

    def collided(self) -> bool:
        self.is_colliding = True
        return True

    def stoppedColliding(self) -> bool:
        self.is_colliding = False
        return False
        
    def isMoving(self):
        return self.can_move_left or self.can_move_right or self.can_move_up or self.can_move_left

    def changeMoving(self, can_move: bool):
        self.can_move_left = can_move
        self.can_move_right = can_move
        self.can_move_up = can_move
        self.can_move_down = can_move
        self.can_move = can_move
