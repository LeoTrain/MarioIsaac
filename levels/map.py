import pygame
import pytmx

from typing import List
from pygame.math import Vector2
from ..entities.tile import Tile


class Map:
    def __init__(self, map_file):
        self.tmx_data = pytmx.util_pygame.load_pygame(map_file)
        self.width = self.tmx_data.width
        self.height = self.tmx_data.height
        self.tile_size = 128
        self.map_tile_size = 32

    def render(self, surface, offset_x, offset_y):
        for layer in self.tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = self.tmx_data.get_tile_image_by_gid(gid)
                    if tile:
                        tile = pygame.transform.scale(tile, (self.tile_size, self.tile_size))
                        position = Vector2(x * self.tile_size, y * self.tile_size) - Vector2(offset_x, offset_y)
                        surface.blit(tile, position.xy)

    def get_collision_tiles(self, surface):
        collision_tiles = []
        for layer in self.tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer) and "Hard" in layer.name:
                for x, y, gid in layer:
                    if gid != 0:
                        tile = Tile(surface, set_position=Vector2(x * self.tile_size, y * self.tile_size))
                        collision_tiles.append(tile)
        return collision_tiles

    def _calculate_scale_factor(self):
        i = 1
        while i <= 10:
            is_matching = True if self.map_tile_size * i == self.tile_size else False
            if is_matching:
                return i
            i += 1

    def get_player_starting_position(self) -> Vector2:
        scale_factor = self._calculate_scale_factor()
        for obj in self.tmx_data.objects:
            if obj.name == "player_spawn":
                return Vector2(obj.x * scale_factor, obj.y * scale_factor)
        return Vector2(0, 0)

    def get_enemy_starting_position(self, enemy_name) -> List[Vector2]:
        positions = []
        scale_factor = self._calculate_scale_factor()
        for obj in self.tmx_data.objects:
            if enemy_name in obj.name:
                positions.append(Vector2(obj.x * scale_factor, obj.y * scale_factor))
        return positions
