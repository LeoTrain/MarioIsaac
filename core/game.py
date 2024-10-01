import pygame

from ..core.main_menu import MainMenu
from ..levels.level import Level
from ..logic.event_handler import EventHandler


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.display_width, self.display_height = 800, 600
        self.display = pygame.display.set_mode(
            (self.display_width, self.display_height)
        )
        self.running = True
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.level = Level(self.display)
        self.level_active = False
        self.main_menu = MainMenu(self.display, "MarioIsaac/assets/tileset/menu_bg.jpg")
        self.main_menu_active = True
        self.event_handler = EventHandler(self.display, self.level)

    def handle_player_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.level.player.move(-1, 0)
            self.level.player.current_x_direction = "left"
            self.level.player.set_direction("left")
            self.level.player.current_state = "run"
        elif keys[pygame.K_d]:
            self.level.player.move(1, 0)
            self.level.player.current_x_direction = "right"
            self.level.player.set_direction("right")
            self.level.player.current_state = "run"
        elif keys[pygame.K_w]:
            self.level.player.move(0, -1)
            self.level.player.current_y_direction = "up"
            self.level.player.set_direction("up")
            self.level.player.current_state = "run"
        elif keys[pygame.K_s]:
            self.level.player.move(0, 1)
            self.level.player.current_y_direction = "down"
            self.level.player.set_direction("down")
            self.level.player.current_state = "run"
        else:
            if self.level.player.in_attack:
                if self.level.player.attack_counter < 25:
                    self.level.player.attack_counter += 1
                    self.level.player.current_state = "attack"
                else:
                    self.level.player.attack_counter = 0
                    self.level.player.in_attack = False
            else:
                self.level.player.current_state = "idle"

    def run(self):
        while self.running:
            if self.main_menu_active and not self.level_active:
                if not self.main_menu.handle_input():
                    self.main_menu.render()
                else:
                    self.main_menu_active = False
                    self.level_active = True
                    self.level.reset_level()
            elif self.level_active and not self.main_menu_active:
                self.event_handler.handle()
                self.handle_player_movement()
                self.level.update()
                self.level.render()

            self.clock.tick(self.fps)
        pygame.quit()
