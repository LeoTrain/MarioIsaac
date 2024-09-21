import pygame


class SpriteLoader:
    def __init__(self, sprite_sheet_path):
        self.sprite_sheet = pygame.image.load(sprite_sheet_path)

    def _load_sprites(self, y_start, num_of_frames, sprite_width, sprite_height):
        sprites = []
        for i in range(num_of_frames):
            image = self.sprite_sheet.subsurface(
                (i * sprite_width, y_start, sprite_width, sprite_height)
            )
            image = pygame.transform.scale(image, (128, 128))
            sprites.append(image)
        return sprites

    def load_sprites_by_direction(self, current_y, number_of_frames, widths, heights, action):
        sprites = {}

        down_height = heights[0]
        sprites[f'{action}_down'] = self._load_sprites(current_y, number_of_frames[0], widths[0], down_height)
        current_y += down_height

        up_height = heights[1]
        sprites[f'{action}_up'] = self._load_sprites(current_y, number_of_frames[1], widths[1], up_height)
        current_y += up_height

        left_height = heights[2]
        sprites[f'{action}_left'] = self._load_sprites(current_y, number_of_frames[2], widths[2], left_height)
        current_y += left_height

        right_height = heights[3]
        sprites[f'{action}_right'] = self._load_sprites(current_y, number_of_frames[3], widths[3], right_height)
        current_y += right_height

        return sprites, current_y

    def load_idle_sprites(self, current_y, number_of_frames, widths, heights):
        return self.load_sprites_by_direction(current_y, number_of_frames, widths, heights, action='idle')

    def load_run_sprites(self, current_y, number_of_frames, widths, heights):
        return self.load_sprites_by_direction(current_y, number_of_frames, widths, heights, action='run')

    def load_attack_sprites(self, current_y, number_of_frames, widths, heights):
        return self.load_sprites_by_direction(current_y, number_of_frames, widths, heights, action='attack')

    def load_character_sprites(self, number_of_frames, widths, heights):
        current_y = 0

        idle_sprites, current_y = self.load_idle_sprites(current_y, number_of_frames["idle"], widths["idle"], heights["idle"])
        run_sprites, current_y = self.load_run_sprites(current_y, number_of_frames["run"], widths["run"], heights["run"])
        attack_sprites, current_y = self.load_attack_sprites(current_y, number_of_frames["attack"], widths["attack"], heights["attack"])

        character_sprites = {
            **idle_sprites,
            **run_sprites,
            **attack_sprites
        }

        return character_sprites
