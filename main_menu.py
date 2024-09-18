import pygame
import sys


class MainMenu:
    def __init__(self, surface):
        self.surface = surface
        self.font = pygame.font.Font(None, 50)
        self.options = ["Start Game", "Quit"]
        self.selected_index = 0

    def render(self):
        self.surface.fill((0, 0, 0))
        for i, option in enumerate(self.options):
            color = (255, 255, 255) if i == self.selected_index else (100, 100, 100)
            text = self.font.render(option, True, color)
            text_rect = text.get_rect(center=(self.surface.get_width() // 2, 150 + i * 60))
            self.surface.blit(text, text_rect)
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
                        pygame.quit()
                        sys.exit()
        return None
