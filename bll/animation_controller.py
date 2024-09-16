import pygame


class AnimationController:
    def __init__(self):
        self.current_state = "idle"
        self.current_x_direction = "right"
        self.current_y_direction = "down"
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
        self.sprites = []

    def _increment_frame(self):
        self.current_frame_index += 1
        total_frames = self.frame_counts.get(self.current_state, 5) * (self.sprite_frames.get(self.current_state, 12) - 1)
        if self.current_frame_index > total_frames:
            self.current_frame_index = 0

    def _update_mask(self):
        self.mask = pygame.mask.from_surface(self.image)

    def _select_state_image(self) -> None:
        frame_count = self.frame_counts.get(self.current_state, 0)
        state_up = self.current_state + "_up"
        state_down_right = self.current_state + "_down_right"
        state_down_left = self.current_state + "_down_left"
        if self.current_y_direction == "up":
            self.image = self.sprites[state_up][self.current_frame_index // frame_count]
        else:
            if self.current_x_direction == "right":
                self.image = self.sprites[state_down_right][self.current_frame_index // frame_count]
            else:
                self.image = self.sprites[state_down_left][self.current_frame_index // frame_count]

    def _select_image(self):
        self._select_state_image()
        self._update_rectangle()

    def _update_rectangle(self):
        old_center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = old_center

    def update_sprite(self):
        self._increment_frame()
        self._select_image()
        self._update_mask()
