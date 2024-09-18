import pygame
import pytmx

from ..bll.tile import Tile


class Map:
    def __init__(self, map_file):
        self.tmx_data = pytmx.util_pygame.load_pygame(map_file)
        self.width = self.tmx_data.width
        self.height = self.tmx_data.height
        self.tile_size = 64

    def render(self, surface, offset_x, offset_y):
        for layer in self.tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = self.tmx_data.get_tile_image_by_gid(gid)
                    if tile:
                        surface.blit(tile, (x * self.tile_size - offset_x, y * self.tile_size - offset_y))

    def get_collision_tiles(self, surface):
        collision_tiles = []
        for layer in self.tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer) and "Hard" in layer.name:
                for x, y, gid in layer:
                    if gid != 0:
                        tile = Tile(surface)
                        tile.rect.topleft = (x * self.tile_size, y * self.tile_size)
                        collision_tiles.append(tile)
        return collision_tiles

    def get_player_starting_position(self):
        x_start = 0
        y_start = 0
        for obj in self.tmx_data.objects:
            print(obj)
            if obj.name == "player_spawn":
                x_start = obj.x
                y_start = obj.y
        return (x_start, y_start)

    def get_enemy_starting_position(self, enemy_name):
        x_start = 0
        y_start = 0
        positions = []
        for obj in self.tmx_data.objects:
            print(obj)
            if enemy_name in obj.name:
                x_start = obj.x
                y_start = obj.y
                positions.append((x_start, y_start))
        return positions
