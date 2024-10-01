class CollisionResolver:
    def resolve_tile_collision(self, entity, tiles):
        collision_detected = False
        for tile in tiles:
            overlap_x = entity.rect.centerx - tile.rect.centerx
            overlap_y = entity.rect.centery - tile.rect.centery
            if abs(overlap_x) > abs(overlap_y):
                if overlap_x > 0:
                    entity.rect.left = tile.rect.right
                    entity.can_move_left = False
                    collision_detected = True
                else:
                    entity.rect.right = tile.rect.left
                    entity.can_move_right = False
                    collision_detected = True
            else:
                if overlap_y > 0:
                    entity.rect.top = tile.rect.bottom
                    entity.can_move_up = False
                    collision_detected = True
                else:
                    entity.rect.bottom = tile.rect.top
                    entity.can_move_down = False
                    collision_detected = True

        if not collision_detected:
            entity.can_move_right = True
            entity.can_move_left = True
            entity.can_move_down = True
            entity.can_move_up = True

    def resolve_entity_collision(self, entity1, entity2):
        if entity1.rect.centerx < entity2.rect.centerx:
            entity1.rect.right = entity2.rect.left
        else:
            entity1.rect.left = entity2.rect.right

        if entity1.rect.centery < entity2.rect.centery:
            entity1.rect.bottom = entity2.rect.top
        else:
            entity1.rect.top = entity2.rect.bottom
