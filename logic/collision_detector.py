import pygame


class CollisionDetector:
    def detect_tile_collisions(self, entity, tiles):
        collided_tiles = []
        for tile in tiles:
            if pygame.sprite.collide_mask(entity, tile):
                collided_tiles.append(tile)
        return collided_tiles

    def detect_entity_collision(self, entity1, entity2):
        return pygame.sprite.collide_mask(entity1, entity2)
