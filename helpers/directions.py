from pygame.math import Vector2

class Directions:
    EMPTY = Vector2(0, 0)
    UP = Vector2(0, -1)
    DOWN = Vector2(0, 1)
    RIGHT = Vector2(1, 0)
    LEFT = Vector2(-1, 0)
    UPLEFT = UP + LEFT
    UPRIGHT = UP + RIGHT
    DOWNLEFT = DOWN + LEFT
    DOWNRIGHT = DOWN + RIGHT

    @classmethod
    def all_directions(cls):
        return [cls.EMPTY, cls.LEFT, cls.RIGHT, cls.UP, cls.DOWN, cls.UPLEFT, cls.UPRIGHT, cls.DOWNLEFT, cls.DOWNRIGHT]

    @staticmethod
    def to_string(direction:Vector2):
        direction_map = {
            (0, 0): "empty",
            (0, -1): "up",
            (0, 1): "down",
            (1, 0): "right",
            (-1, 0): "left",
            (-1, -1): "upleft",
            (1, -1): "upright",
            (-1, 1): "downleft",
            (1, 1): "downright",
        }
        return direction_map.get((int(direction.x), int(direction.y)), "Unknown Direction")
