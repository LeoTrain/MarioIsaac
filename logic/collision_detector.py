import pygame
from pygame.math import Vector2

class CollisionDetector:
    def detect_tile_collisions(self, entity, tiles):
        return [tile for tile in tiles if pygame.sprite.collide_rect(entity, tile)]

    def detect_entity_collision(self, entity1, entity2) -> Vector2 | None:
        # offset = (int(entity2.position.x - entity1.position.x), int(entity2.position.y - entity1.position.y))
        # collision_point = entity1.mask.overlap(entity2.mask, offset)
        # if collision_point:
        #     collision_point = Vector2(collision_point[0] - entity1.rect.width // 2, collision_point[1] - entity1.rect.height // 2)
        copy1 = entity1.rect
        copy2 = entity2.rect
        entity1.rect = entity1.inflated_rect
        entity2.rect = entity2.inflated_rect
        intersection = entity1.rect.clip(entity2.rect)
        collision_point = Vector2(intersection.x, intersection.y)
        entity1.rect = copy1
        entity2.rect = copy2
        return collision_point if intersection.width > 0 and intersection.height > 0 else None


