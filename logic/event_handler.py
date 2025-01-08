import pygame

from ..logic.event_dick import event_dick
from ..core.death_screen import DeathScreen
from ..core.winner_screen import WinnerScreen
from ..helpers.directions import Directions
from pygame.math import Vector2


class EventHandler:
    def __init__(self, display, level, game) -> None:
        self.level = level
        self.death_screen = DeathScreen(display, level)
        self.winner_screen = WinnerScreen(display, level)
        self.game = game

    def handle_player_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self._player_move_to_direction(Directions.LEFT)
        elif keys[pygame.K_d]:
            self._player_move_to_direction(Directions.RIGHT)
        elif keys[pygame.K_w]:
            self._player_move_to_direction(Directions.UP)
        elif keys[pygame.K_s]:
            self._player_move_to_direction(Directions.DOWN)
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

    def _player_move_to_direction(self, direction:Vector2) -> None:
        self.level.player.move(direction)
        self.level.player.current_direction = direction
        self.level.player.set_direction(direction)
        self.level.player.current_state = "run"

    def handle_event(self, event):
        self.handle_custom_events(event)
        self.handle_pygame_events(event)

    def handle_pygame_events(self, event):
        if event.type == pygame.QUIT:
            self.game.running = False
        elif event.type == pygame.KEYDOWN:
            self.handle_keydown_events(event)

    def handle_keydown_events(self, event):
        if event.key == pygame.K_o:
            self.level.player.draw_rect_border = not self.level.player.draw_rect_border
        elif event.key == pygame.K_p:
            self.level.player.color_mask = not self.level.player.color_mask
        elif event.key == pygame.K_k:
            for entity in self.level.enemies:
                entity.draw_rect_border = not entity.draw_rect_border
        elif event.key == pygame.K_l:
            for entity in self.level.enemies:
                entity.color_mask = not entity.color_mask
        elif event.key == pygame.K_SPACE:
            self.level.player.in_attack = True
            self.level.player.attack(self.level.enemies)

    def handle_end_state(self, state):
        if state == "start_game":
            self.level.reset_level()
            self.game.nextLevel()
            self.game.level_active = True
            self.game.main_menu_active = False
        elif state == "main_menu":
            self.game.level_active = False
            self.game.main_menu_active = True
        return False

    def handle_custom_events(self, event):
        if event.type == event_dick["player_dead"]:
            state = self.death_screen.run()
            self.handle_end_state(state)

        elif event.type == event_dick["enemy_dead"]:
            self.level.enemies = [
                enemy for enemy in self.level.enemies if enemy.life_points > 0
            ]

        elif event.type == event_dick["player_won"]:
            state = self.winner_screen.run()
            self.handle_end_state(state)

    def handle(self):
        for event in pygame.event.get():
            self.handle_event(event)
        self.handle_player_movement()
