import pygame
import sys


class MainMenu:
    def __init__(self, surface, background_image_path):
        self.surface = surface
        self.font = pygame.font.Font(None, 50)
        self.options = ["Start Game", "Quit"]
        self.selected_index = 0
        self.background_image = pygame.image.load(background_image_path)
        self.background_image = pygame.transform.scale(self.background_image, (self.surface.get_width(), self.surface.get_height()))

    def render(self):
        self.surface.blit(self.background_image, (0, 0))
        for i, option in enumerate(self.options):
            color = (255, 255, 0) if i == self.selected_index else (255, 255, 255)
            text = self.font.render(option, True, color)
            shadow = self.font.render(option, True, (0, 0, 0))
            shadow_rect = shadow.get_rect(center=(self.surface.get_width() // 2, 150 + i * 60))
            text_rect = text.get_rect(center=(self.surface.get_width() // 2, 150 + i * 60))
            self.surface.blit(shadow, (shadow_rect.x + 2, shadow_rect.y + 2))
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

    def run(self):
        menu_choice = None
        while menu_choice is None:
            menu_choice = self.handle_input()
            self.render()
        return menu_choice
