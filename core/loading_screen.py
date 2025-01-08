import pygame


class LoadingScreen:
    def __init__(
        self,
        surface,
        font,
        total_steps,
        background_color=(0, 0, 0),
        text_color=(255, 255, 255),
    ):
        self.surface = surface
        self.font = font
        self.background_color = background_color
        self.text_color = text_color
        self.loading_text = "Loading..."
        self.progress = 0
        self.total_steps = total_steps
        self.current_step = 0

    def draw(self):
        self.surface.fill(self.background_color)

        text_surface = self.font.render(self.loading_text, True, self.text_color)
        text_rect = text_surface.get_rect(
            center=(self.surface.get_width() // 2, self.surface.get_height() // 2 - 50)
        )
        self.surface.blit(text_surface, text_rect)

        bar_width = self.surface.get_width() // 2
        bar_height = 30
        bar_x = (self.surface.get_width() - bar_width) // 2
        bar_y = self.surface.get_height() // 2

        pygame.draw.rect(
            self.surface, (200, 200, 200), (bar_x, bar_y, bar_width, bar_height)
        )

        progress_width = int(bar_width * (self.progress / 100))
        pygame.draw.rect(
            self.surface, self.text_color, (bar_x, bar_y, progress_width, bar_height)
        )

    def update_progress(self, new_progress):
        self.progress = new_progress

    def increment_step(self):
        self.current_step += 1
        self.progress = (self.current_step / self.total_steps) * 100

    def update(self):
        self.draw()
        pygame.display.flip()
