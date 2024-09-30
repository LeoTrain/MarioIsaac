import pygame


import pygame

class CollisionHandler:
    def __init__(self, player, collision_tiles, enemies, collision_cooldown=500):
        self.player = player
        self.collision_tiles = collision_tiles
        self.enemies = enemies
        self.is_colliding = False
        self.collision_cooldown = collision_cooldown
        self.collision_timer = 0

    def handle_collisions(self) -> None:
        if self.collision_timer > 0:
            self.collision_timer -= pygame.time.get_ticks()

        if self.is_colliding:
            vertical_collided = self._handle_vertical_collision()
            horizontal_collided = self._handle_horizontal_collision()
            if not vertical_collided and not horizontal_collided:
                self.is_colliding = False
                self.collision_timer = self.collision_cooldown
        else:
            if self.collision_timer <= 0:
                vertical_collided = self._handle_vertical_collision()
                horizontal_collided = self._handle_horizontal_collision()
                if vertical_collided or horizontal_collided:
                    self.is_colliding = True

        self._handle_goblins_collision()

    def _handle_horizontal_collision(self) -> bool:
        collision_detected = False
        for tile in self.collision_tiles:
            if pygame.sprite.collide_mask(self.player, tile):
                if self.player.last_pressed_direction == "right":
                    overlap = self.player.rect.right - tile.rect.left
                    if overlap > 0:
                        self.player.rect.right = tile.rect.left
                        self.player.can_move_right = False

                elif self.player.last_pressed_direction == "left":
                    overlap = self.player.rect.right - tile.rect.left
                    if overlap > 0:
                        self.player.rect.left = tile.rect.right
                    self.player.can_move_left = False
                collision_detected = True

        if not collision_detected:
            if self.player.last_pressed_direction == "right":
                self.player.can_move_left = True
            elif self.player.last_pressed_direction == "left":
                self.player.can_move_right = True

        return collision_detected

    def _handle_vertical_collision(self) -> bool:
        collision_detected = False
        for tile in self.collision_tiles:
            if pygame.sprite.collide_mask(self.player, tile):
                if self.player.last_pressed_direction == "down":
                    overlap = self.player.rect.bottom - tile.rect.top
                    if overlap > 0:
                        self.player.rect.bottom = tile.rect.top
                        self.player.can_move_down = False

                elif self.player.last_pressed_direction == "up":
                    overlap = tile.rect.bottom - self.player.rect.top
                    if overlap > 0:
                        self.player.rect.top = tile.rect.bottom
                        self.player.can_move_up = False
                collision_detected = True

        if not collision_detected:
            if self.player.last_pressed_direction == "down":
                self.player.can_move_up = True
            elif self.player.last_pressed_direction == "up":
                self.player.can_move_down = True
        return collision_detected


    def _handle_goblins_collision(self) -> None:
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

