import pygame
import sys


class WinnerScreen:
    def __init__(self, surface, level):
        self.surface = surface
        self.level = level
        self.font = pygame.font.Font(None, 50)
        self.options = ["Next level", "Return To Menu", "Quit"]
        self.selected_index = 0
        self._initiate_rectangles()

    def _initiate_rectangles(self):
        self.option_rectangles = []
        for option in self.options:
            text = self.font.render(option, True, (255, 255, 255))
            text_rect = text.get_rect()
            self.option_rectangles.append({"text": text, "rect": text_rect})
        rect_height_sum = sum([opt["rect"].height for opt in self.option_rectangles])
        x_start = self.surface.get_width() // 2
        y_start = self.surface.get_height() // 2 - rect_height_sum // 2
        for option in self.option_rectangles:
            option["rect"].center = (x_start, y_start)
            y_start += option["rect"].height + 40

    def render(self):
        overlay = pygame.Surface(
            (self.surface.get_width(), self.surface.get_height()), pygame.SRCALPHA
        )
        overlay.fill((0, 0, 0, 150))
        self.surface.blit(overlay, (0, 0))

        for i, option in enumerate(self.option_rectangles):
            color = (255, 233, 0) if i == self.selected_index else (255, 255, 204)
            text = self.font.render(self.options[i], True, color)

            outline_text = self.font.render(self.options[i], True, (204, 153, 150))
            outline_rect = outline_text.get_rect(center=option["rect"].center)
            for offset in [-2, 2]:
                self.surface.blit(
                    outline_text, (outline_rect.x + offset, outline_rect.y)
                )
                self.surface.blit(
                    outline_text, (outline_rect.x, outline_rect.y + offset)
                )
            self.surface.blit(text, option["rect"])

        title_font = pygame.font.Font(None, 80)
        title_text = title_font.render("You Won!", True, (255, 140, 0))
        title_rect = title_text.get_rect(
            center=(self.surface.get_width() // 2, self.surface.get_height() // 4)
        )
        self.surface.blit(title_text, title_rect)

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

    def run(self):
        winner_choice = None
        while winner_choice is None:
            self.level._render()
            winner_choice = self.handle_input()
            self.render()
        return winner_choice
