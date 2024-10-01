import pygame

from ..core.main_menu import MainMenu
from ..levels.level import Level
from ..logic.event_handler import EventHandler


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.display_width, self.display_height = 800, 600
        self.display = pygame.display.set_mode((self.display_width, self.display_height))
        self.running = True
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.level = Level(self.display)
        self.level_active = False
        self.main_menu = MainMenu(self.display, "MarioIsaac/assets/tileset/menu_bg.jpg")
        self.main_menu_active = True
        self.event_handler = EventHandler(self.display, self.level, self)

    def run(self):
        while self.running:
            if self.main_menu_active and not self.level_active:
                menu_choice = self.main_menu.run()
                if menu_choice == "start_game":
                    self.main_menu_active = False
                    self.level_active = True
                    self.level.reset_level()
            elif self.level_active and not self.main_menu_active:
                self.event_handler.handle()
                self.level.update()
                self.level.render()
            self.clock.tick(self.fps)
        pygame.quit()
