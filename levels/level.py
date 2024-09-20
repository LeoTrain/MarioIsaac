import pygame

from ..entities.player import Player
from ..entities.goblin import Goblin
from ..levels.map import Map
from ..logic.collision_handler import CollisionHandler
from ..logic.event_dick import event_dick
from ..core.loading_screen import LoadingScreen


class Level(CollisionHandler):
    def __init__(self, surface):
        self.surface = surface
        self.game_map = Map("MarioIsaac/maps/level_one.tmx")
        self._initialise_player()
        self._initialise_enemies()
        self._initialise_images()
        super().__init__(self.player, self.game_map.get_collision_tiles(surface), self.enemies)
        self.all_sprites = pygame.sprite.Group()
        self.camera_offset_x = self.player.rect.topleft[0]
        self.camera_offset_y = self.player.rect.topleft[1]

    def _initialise_images(self):
        heart_alive_image = pygame.image.load("MarioIsaac/assets/tileset/hearts/heart_red.png")
        heart_dead_image = pygame.image.load("MarioIsaac/assets/tileset/hearts/heart_black.png")
        self.heart_alive_image = pygame.transform.scale(heart_alive_image, (32, 32))
        self.heart_dead_image = pygame.transform.scale(heart_dead_image, (32, 32))

    def _initialise_player(self):
        sprite_sheet_path = "MarioIsaac/assets/sprites/base_character/my_base_character_v2.png"
        self.player = Player(self.surface, sprite_sheet_path)
        starting_position = self.game_map.get_player_starting_position()
        self.player.rect.topleft = starting_position[0], starting_position[1]
        print(starting_position)
        self.player.mask = pygame.mask.from_surface(self.player.image)

    def _initialise_enemies(self):
        sprite_sheet_path = "MarioIsaac/assets/sprites/orcs/goblin.png"
        starting_positions = self.game_map.get_enemy_starting_position("goblin")
        self.enemies = []
        for i in range(len(starting_positions)):
            goblin = Goblin(self.surface, sprite_sheet_path)
            goblin.rect = goblin.image.get_rect(topleft=starting_positions[i])
            self.enemies.append(goblin)

    def wait(self):
        pygame.time.wait(1000)

    def reset_level(self):
        font = pygame.font.Font(None, 36)
        self.loading_screen = LoadingScreen(self.surface, font, total_steps=5)
        self.loading_screen.update()

        self._initialise_images()
        self.loading_screen.increment_step()
        self.loading_screen.update()

        self._initialise_enemies()
        self.loading_screen.increment_step()
        self.loading_screen.update()

        self._initialise_player()
        self.loading_screen.increment_step()
        self.loading_screen.update()

        self._initialise_player()
        self.wait()
        self._initialise_player()
        self.wait()

    def _update_camera(self):
        self.camera_offset_x = self.player.rect.centerx - self.surface.get_width() // 2
        self.camera_offset_y = self.player.rect.centery - self.surface.get_height() // 2

    def _draw_hearts(self):
        dead = self.player.starting_life_points - self.player.life_points
        heart_width = self.heart_alive_image.get_width()
        x_pos = self.surface.get_width() - heart_width
        for i in range(self.player.life_points):
            x_pos -= heart_width
            self.surface.blit(self.heart_alive_image, (x_pos, 50))
        for i in range(dead):
            x_pos -= heart_width
            self.surface.blit(self.heart_dead_image, (x_pos, 50))

    def render(self):
        self.surface.fill((92, 82, 71))
        self.game_map.render(self.surface, self.camera_offset_x, self.camera_offset_y)
        self.player.draw(self.camera_offset_x, self.camera_offset_y)
        for enemy in self.enemies:
            enemy.draw(self.camera_offset_x, self.camera_offset_y)
        self._draw_hearts()

    def did_player_win(self):
        if len(self.enemies) == 0:
            event = pygame.event.Event(event_dick["player_won"])
            pygame.event.post(event)

    def update(self):
        self.player.update()
        for enemy in self.enemies:
            enemy.update((self.player.rect.x, self.player.rect.y))
        self.handle_collisions()
        self.did_player_win()
        self._update_camera()
        pygame.display.update()
