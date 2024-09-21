import pygame


class CollisionHandler:
    def __init__(self, player, collision_tiles, enemies):
        self.player = player
        self.collision_tiles = collision_tiles
        self.enemies = enemies
        self.is_colliding = False

    def _handle_vertical_collision(self):
        collision_detected = False
        for tile in self.collision_tiles:
            if pygame.sprite.collide_mask(self.player, tile):
                if self.player.last_pressed_direction == "down" and self.player.rect.bottom > tile.rect.top:
                    self.player.rect.bottom = tile.rect.top
                elif self.player.last_pressed_direction == "up" and self.player.rect.top < tile.rect.bottom:
                    self.player.rect.top = tile.rect.bottom
                self.is_colliding = True
                collision_detected = True
        return collision_detected
                

    def _handle_horizontal_collision(self):
        collision_detected = False
        for tile in self.collision_tiles:
            if pygame.sprite.collide_mask(self.player, tile):
                if self.player.last_pressed_direction == "right" and self.player.rect.right > tile.rect.left:
                    self.player.rect.right = tile.rect.left
                elif self.player.last_pressed_direction == "left" and self.player.rect.left <  tile.rect.right:
                    self.player.rect.left = tile.rect.right
                self.is_colliding = True
                collision_detected = True
        return collision_detected

    def _handle_goblins_collision(self):
        for entity in self.enemies:
            for tile in self.collision_tiles:
                if pygame.sprite.collide_mask(entity, tile):
                    pass

            if pygame.sprite.collide_mask(entity, self.player):
                if entity.can_attack():
                    entity.attack(self.player)

            for other_entity in self.enemies:
                if other_entity is not entity:
                    if pygame.sprite.collide_mask(entity, other_entity):
                        if entity.rect.centerx < other_entity.rect.centerx:
                            entity.rect.right = other_entity.rect.left
                        elif entity.rect.centerx > other_entity.rect.centerx:
                            entity.rect.left = other_entity.rect.right

    def handle_collisions(self):
        if self.is_colliding:
            vertical_collided = self._handle_vertical_collision()
            horizontal_collided = self._handle_horizontal_collision()
            if not vertical_collided and not horizontal_collided:
                self.is_colliding = False
        else:
            # place player to 
        self._handle_goblins_collision()
