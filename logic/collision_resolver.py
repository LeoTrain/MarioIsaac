from math import sqrt
import pygame
from pygame.math import Vector2

class CollisionResolver:
    def resolve_tile_collision(self, entity, tiles):
        collision_left = collision_right = collision_up = collision_down = False

        for tile in tiles:
            overlap = entity.position - tile.position
            if abs(overlap.x) > abs(overlap.y):
                if overlap.x > 0:
                    entity.position.x = tile.position.x + tile.rect.width
                    collision_left = True
                else:
                    entity.position.x = tile.position.x - entity.rect.width
                    collision_right = True
            else:
                if overlap.y > 0:
                    entity.position.y = tile.position.y + tile.rect.height
                    collision_up = True
                else:
                    entity.position.y = tile.position.y - entity.rect.height
                    collision_down = True

        entity.can_move_left = not collision_left
        entity.can_move_right = not collision_right
        entity.can_move_up = not collision_up
        entity.can_move_down = not collision_down

    def resolve_entity_collision(self, entity1, entity2, collision_vector:Vector2) -> None:
        collision_normal = collision_vector.normalize()
        overlap = (entity1.rect.width / 2 + entity2.rect.width / 2) - collision_vector.length()

        if entity1.isEnemy() and entity2.isPlayer():
            entity1.changeMoving(False)
            entity1.collided()
            return

        if entity1.isEnemy() and entity2.isEnemy():
            # entity2.position += collision_normal * overlap / 2
            # entity1.position -= collision_normal * overlap / 2
            #
            # velocity1 = entity1.velocity
            # velocity2 = entity2.velocity
            # entity1.velocity = velocity2
            # entity2.velocity = velocity1
            #
            # separation = entity2.position - entity1.position
            # adjustment = separation.normalize() * (overlap / 2)
            # entity1.position -= adjustment
            # entity2.position += adjustment
            # entity1.rect = entity1.old_rect
            # entity2.changeMoving(False)
            # entity2.collided()
            self.resolve_tile_collision(entity1, [entity2])

