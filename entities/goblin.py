import time

from ..entities.enemy import Enemy


class Goblin(Enemy):
    def __init__(self, display, sprite_sheet_path):
        self.number_of_frames = {
            "idle": [4, 4, 4, 4],
            "run": [8, 8, 8, 8],
            "attack": [8, 8, 8, 8],
        }
        self.sprite_widths = {
            "idle": [64, 64, 64, 64],
            "run": [64, 64, 64, 64],
            "attack": [64, 64, 64, 64],
        }
        self.sprite_heights = {
            "idle": [64, 64, 64, 64],
            "run": [64, 64, 64, 64],
            "attack": [64, 64, 64, 64],
        }
        super().__init__(display, sprite_sheet_path)
        self.image = self.sprites["idle_down"][0]
        self.current_frame_index = 0
        self.speed = 1
        self.life_points = 5
        self.attack_range = 100
        self.attack_power = 1
        self.attack_start_time = time.time()
