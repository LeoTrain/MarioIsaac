import time

from ..entities.enemy import Enemy


class Goblin(Enemy):
    def __init__(self, display, sprite_sheet_path):
        super().__init__(display, sprite_sheet_path)
        self.sprites = self.load_character_sprites(
            [48, 48, 48, 48, 64, 64],
            [48, 48, 48, 48, 64, 64],
            [4, 4, 8, 8, 8, 8],
        )
        self.image = self.sprites["idle_down_right"][0]
        self.current_frame_index = 0
        self.frame_counts = {
            "idle": 4,
            "run": 8,
            "attack": 8,
        }
        self.sprite_frames = {
            "idle": 4,
            "run": 8,
            "attack": 8,
        }
        self.speed = 1
        self.life_points = 5
        self.attack_range = 100
        self.attack_power = 1
        self.attack_start_time = time.time()
