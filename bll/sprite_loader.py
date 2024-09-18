import pygame


class SpriteLoader:
    def __init__(self, sprite_sheet_path):
        self.sprite_sheet_path = sprite_sheet_path
        self.current_frame_index = 0
        self.frame_counts = {
            "idle": 0,
            "run": 0,
            "attack": 0,
        }
        self.sprite_frames = {
            "idle": 0,
            "run": 0,
            "attack": 0,
        }

    def _load_sprites(self, sprite_sheet, y_start, num_of_frames, sprite_width, sprite_height):
        sprites = []
        for i in range(num_of_frames):
            image = sprite_sheet.subsurface(
                (i * sprite_width, y_start, sprite_width, sprite_height)
            )
            image = pygame.transform.scale(image, (128, 128))
            sprites.append(image)
        return sprites

    def _flip_sprites(self, sprite):
        return [pygame.transform.flip(frame, True, False) for frame in sprite]

    def load_character_sprites(self, widths, heights, number_of_frames):
        sprite_sheet = pygame.image.load(self.sprite_sheet_path).convert_alpha()
        current_y = 0

        # Idle
        idle_height = heights[0]
        idle_down_right = self._load_sprites(sprite_sheet, current_y, number_of_frames[0], widths[0], idle_height)
        idle_down_left = self._flip_sprites(idle_down_right)
        current_y += idle_height

        idle_up_height = heights[1]
        idle_up = self._load_sprites(sprite_sheet, current_y, number_of_frames[1], widths[1], idle_up_height)
        current_y += idle_up_height

        # Run
        run_height = heights[2]
        run_down_right = self._load_sprites(sprite_sheet, current_y, number_of_frames[2], widths[2], run_height)
        run_down_left = self._flip_sprites(run_down_right)
        current_y += run_height

        run_up_height = heights[3]
        run_up = self._load_sprites(sprite_sheet, current_y, number_of_frames[3], widths[3], run_up_height)
        current_y += run_up_height

        # Attack
        attack_height = heights[4]
        attack_down_right = self._load_sprites(sprite_sheet, current_y, number_of_frames[4], widths[4], attack_height)
        attack_down_left = self._flip_sprites(attack_down_right)
        current_y += attack_height

        attack_up_height = heights[5]
        attack_up = self._load_sprites(sprite_sheet, current_y, number_of_frames[5], widths[5], attack_up_height)
        current_y += attack_up_height

        player_sprites = {
            "idle_down_right": idle_down_right,
            "idle_down_left": idle_down_left,
            "idle_up": idle_up,
            "run_down_right": run_down_right,
            "run_down_left": run_down_left,
            "run_up": run_up,
            "attack_down_right": attack_down_right,
            "attack_down_left": attack_down_left,
            "attack_up": attack_up,
        }
        return player_sprites
