import pygame

from ..bll.tile import Tile
from ..bll.player import Player
from ..bll.goblin import Goblin
from ..levels.map import Map
from ..bll.collision_handler import CollisionHandler


class Level(CollisionHandler):
    def __init__(self, surface):
        self.surface = surface
        self.game_map = Map("MarioIsaac/maps/level_one.tmx")
        self.enemies = []
        self._initialise_player()
        self._initialise_enemies()
        self._initialise_images()
        super().__init__(self.player, self.game_map.get_collision_tiles(surface), self.enemies)
        self.all_sprites = pygame.sprite.Group()
        self.camera_offset_x = 0
        self.camera_offset_y = 0

    def _initialise_images(self):
        heart_alive_image = pygame.image.load("MarioIsaac/assets/sprites/hearts/heart_red.png")
        heart_dead_image = pygame.image.load("MarioIsaac/assets/sprites/hearts/heart_black.png")
        self.heart_alive_image = pygame.transform.scale(heart_alive_image, (64, 64))
        self.heart_dead_image = pygame.transform.scale(heart_dead_image, (64, 64))

    def _initialise_player(self):
        sprite_sheet_path = "MarioIsaac/assets/sprites/base_character/my_base_character_v2.png"
        self.player = Player(self.surface, sprite_sheet_path)
        starting_position = self.game_map.get_player_starting_position()
        self.player.rect.topleft = starting_position
        print(starting_position)
        self.player.mask = pygame.mask.from_surface(self.player.image)

    def _initialise_enemies(self):
        sprite_sheet_path = "MarioIsaac/assets/sprites/orcs/goblin.png"
        starting_positions = self.game_map.get_enemy_starting_position("goblin")
        for i in range(len(starting_positions)):
            goblin = Goblin(self.surface, sprite_sheet_path)
            goblin.rect = goblin.image.get_rect(topleft=starting_positions[i])
            self.enemies.append(goblin)

    def _update_camera(self):
        self.camera_offset_x = self.player.rect.centerx - self.surface.get_width() // 2
        self.camera_offset_y = self.player.rect.centery - self.surface.get_height() // 2

    def _draw_hearts(self):
        for i in range(self.player.starting_life_points):
            x = self.surface.get_width() - self.heart_alive_image.get_width() - self.heart_alive_image.get_width() * i
            pygame.surface.blit(self.heart_alive_image, (x, 100))

    def render(self):
        self.surface.fill((255, 255, 255))
        self.game_map.render(self.surface, self.camera_offset_x, self.camera_offset_y)
        self.player.draw(self.camera_offset_x, self.camera_offset_y)
        for enemy in self.enemies:
            enemy.draw(self.camera_offset_x, self.camera_offset_y)
        self._draw_hearts()

    def update(self):
        self.player.update()
        for enemy in self.enemies:
            enemy.update((self.player.rect.x, self.player.rect.y))
        self.handle_collisions()
        self._update_camera()
        pygame.display.update()

# import pygame
#
# from ..bll.player import Player
# from ..bll.tile import Tile
# from ..bll.goblin import Goblin
# from ..bll.collision_handler import CollisionHandler
#
#
# class Level(CollisionHandler):
#     level_one = [
#         "111111111111",
#         "100000000001",
#         "102000000001",
#         "100000000001",
#         "100000000001",
#         "100000000001",
#         "100000000001",
#         "100000000301",
#         "100000000001",
#         "100000303001",
#         "100000000001",
#         "111111111111",
#     ]
#
#     def __init__(self, display):
#         super().__init__()
#         self.current_level = 1
#         self.display = display
#         self.initialise_world()
#         self.initialise_player()
#         self.initialise_goblins()
#         self.all_sprites = pygame.sprite.Group()
#         for tile in self.world_tiles:
#             self.all_sprites.add(tile)
#         for goblin in self.goblins:
#             self.all_sprites.add(goblin)
#         self.all_sprites.add(self.player)
#         self.camera_offset_x = 0
#         self.camera_offset_y = 0
#
#     def initialise_world(self):
#         self.world_tiles = self.create_world_tiles()
#
#     def initialise_goblins(self):
#         sprite_sheet_path = "MarioIsaac/assets/sprites/orcs/goblin.png"
#         goblins = []
#         for y, rows in enumerate(self.level_one):
#             for x, column in enumerate(rows):
#                 if column == "3":
#                     goblin = Goblin(self.display, sprite_sheet_path)
#                     goblin.rect = goblin.image.get_rect(
#                         topleft=(x * 64, y * 64)
#                     )
#                     goblin.mask = pygame.mask.from_surface(goblin.image)
#                     goblins.append(goblin)
#         self.goblins = goblins
#
#     def initialise_player(self):
#         sprite_sheet_path = "MarioIsaac/assets/sprites/base_character/my_base_character_v2.png"
#         self.player = Player(self.display, sprite_sheet_path)
#         if self.current_level == 1:
#             for y, rows in enumerate(self.level_one):
#                 for x, column in enumerate(rows):
#                     if column == "2":
#                         self.player.rect = self.player.image.get_rect(
#                             topleft=(x * 64, y * 64)
#                         )
#                         self.player.mask = pygame.mask.from_surface(self.player.image)
#
#     def load_world_images(self):
#         tile_one = pygame.image.load("MarioIsaac/assets/background/black.png")
#         tile_one = pygame.transform.scale(tile_one, (64, 64))
#
#         return tile_one
#
#     def create_world_tiles(self):
#         image = self.load_world_images()
#         world_tiles = []
#         for y, rows in enumerate(self.level_one):
#             for x, column in enumerate(rows):
#                 if column == "1":
#                     tile = Tile(self.display)
#                     tile.image = image
#                     tile.rect = tile.image.get_rect(topleft=(x * 64, y * 64))
#                     world_tiles.append(tile)
#                     tile.mask = pygame.mask.from_surface(tile.image)
#
#         return world_tiles
#
#     def update_camera(self):
#         self.camera_offset_x = self.player.rect.centerx - self.display.get_width() // 2
#         self.camera_offset_y = self.player.rect.centery - self.display.get_height() // 2
#
#     def update(self):
#         self.player.update()
#         for goblin in self.goblins:
#             goblin.update((self.player.rect.x, self.player.rect.y))
#         self.handle_collisions()
#
#         self.update_camera()
#
#     def draw(self):
#         self.display.fill((255, 255, 255))
#         for sprite in self.all_sprites:
#             if sprite == self.player:
#                 sprite.draw(self.camera_offset_x, self.camera_offset_y)
#             else:
#                 sprite.draw(self.camera_offset_x, self.camera_offset_y)
#
#         pygame.display.update()
