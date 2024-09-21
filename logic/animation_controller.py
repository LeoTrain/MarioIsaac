import pygame


class AnimationController:
    def __init__(self, sprite_loader):
        self.current_state = "idle"
        self.current_x_direction = "right"
        self.current_y_direction = "down"
        self.current_frame_index = 0
        self.frame_counts = sprite_loader.frame_counts
        self.sprite_frames = sprite_loader.number_of_frames
        self.sprites = sprite_loader.load_character_sprites(
            sprite_loader.frame_counts,
            sprite_loader.sprite_widths,
            sprite_loader.sprite_heights
        )
        self.image = self.sprites["idle_down"][0]
        self.rect = self.image.get_rect()

    def _increment_frame(self):
        self.current_frame_index += 1
        total_frames = self.frame_counts[self.current_state] * self.sprite_frames[self.current_state] - 1
        if self.current_frame_index > total_frames:
            self.current_frame_index = 0

    def select_state_image(self):
        frame_count = self.frame_counts[self.current_state]
        last_direction = self.last_pressed_direction if self.last_pressed_direction is not None else "down"
        print(self.current_state, last_direction)
        state_key = f"{self.current_state}_{last_direction}"
        self.image = self.sprites[state_key][self.current_frame_index // frame_count]

    def _update_mask(self):
        self.mask = pygame.mask.from_surface(self.image)

    def _update_rectangle(self):
        old_center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = old_center

    def update_sprite(self):
        self._increment_frame()
        self.select_state_image()
        self._update_rectangle()
        self._update_mask()
