import pygame

from ..bll.tile import Tile
from ..bll.player import Player
from ..bll.goblin import Goblin
from ..levels.map import Map
from ..bll.collision_handler import CollisionHandler


class Level(CollisionHandler):
    def __init__(self, surface):
        super().__init__()
        self.surface = surface
        self.game_map = Map("MarioIsaac/maps/level_one.tmx")
        self.all_sprites = pygame.sprite.Group()
        for tile in self.game_map.get_collision_tiles(surface):
            self.all_sprites.add(tile)
        self._initialise_player()
        self.camera_offset_x = 0
        self.camera_offset_y = 0

    def _initialise_player(self):
        sprite_sheet_path = "MarioIsaac/assets/sprites/base_character/my_base_character.png"
        self.player = Player(self.surface, sprite_sheet_path)
        starting_position = self.game_map.get_player_starting_position()
        self.player.rect.center = starting_position
        self.player.mask = pygame.mask.from_surface(self.player.image)
        self.all_sprites.add(self.player)

    def update_camera(self):
        self.camera_offset_x = self.player.rect.centerx - self.display.get_width() // 2
        self.camera_offset_y = self.player.rect.centery - self.display.get_height() // 2

    def render(self):
        self.surface.fill((255, 255, 255))
        self.game_map.render(self.surface, self.camera_offset_x, self.camera_offset_y)
        self.player.draw(self.camera_offset_x, self.camera_offset_y)

    def update(self):
        self.player.update()
        pygame.display.update()
