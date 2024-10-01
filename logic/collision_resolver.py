import pygame


class CollisionResolver:
    def resolve_tile_collision(self, entity, tiles):
        collision_left = False
        collision_right = False
        collision_up = False
        collision_down = False
        for tile in tiles:
            overlap_x = entity.rect.centerx - tile.rect.centerx
            overlap_y = entity.rect.centery - tile.rect.centery
            if abs(overlap_x) > abs(overlap_y):
                if overlap_x > 0:
                    entity.rect.left = tile.rect.right
                    collision_left = True
                else:
                    entity.rect.right = tile.rect.left
                    collision_right = True
            else:
                if overlap_y > 0:
                    entity.rect.top = tile.rect.bottom
                    collision_up = True
                else:
                    entity.rect.bottom = tile.rect.top
                    collision_down = True
        if collision_left:
            entity.can_move_left = False
        if collision_right:
            entity.can_move_right = False
        if collision_up:
            entity.can_move_up = False
        if collision_down:
            entity.can_move_down = False

    def resolve_entity_collision(self, entity1, entity2):
        overlap_x = entity1.rect.centerx - entity2.rect.centerx
        overlap_y = entity1.rect.centery - entity2.rect.centery

        if abs(overlap_x) > abs(overlap_y):
            if overlap_x > 0:
                entity1.rect.left = entity2.rect.right
            else:
                entity1.rect.right = entity2.rect.left
        else:
            if overlap_y > 0:
                entity1.rect.top = entity2.rect.bottom
            else:
                entity1.rect.bottom = entity2.rect.top


