import pygame
import sys


class DeathScreen:
    def __init__(self, surface):
        self.surface = surface
        self.font = pygame.font.Font(None, 50)
        self.options = ["Restart Game", "Return To Menu", "Quit"]
        self.selected_index = 0
        self._initiate_rectangles()

    def _initiate_rectangles(self):
        self.option_rectangles = []
        for option in self.options:
            text = self.font.render(option, True, (0, 0, 0))
            text_rect = text.get_rect()
            self.option_rectangles.append({
                "text": text,
                "rect": text_rect
            })
        rect_height_sum = sum([opt["rect"].height for opt in self.option_rectangles])
        x_start = self.surface.get_width() // 2
        y_start = self.surface.get_height() // 2 - rect_height_sum // 2
        for i, option in enumerate(self.option_rectangles):
            option["rect"].center = (x_start, y_start)
            y_start += option["rect"].height + 20

    def render(self):
        self.surface.fill((0, 0, 0))
        for i, option in enumerate(self.option_rectangles):
            color = (255, 0, 0) if i == self.selected_index else (255, 255, 255)
            text = self.font.render(self.options[i], True, color)
            self.surface.blit(text, option["rect"])
        pygame.display.update()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_index = (self.selected_index - 1) % len(self.options)
                elif event.key == pygame.K_DOWN:
                    self.selected_index = (self.selected_index + 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    if self.selected_index == 0:
                        return "start_game"
                    elif self.selected_index == 1:
                        return "main_menu"
                    elif self.selected_index == 2:
                        pygame.quit()
                        sys.exit()
        return None
