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

        self._handle_enemy_collisions()

    def _handle_horizontal_collision(self) -> bool:
        collision_detected = False
        player_center = self.player.rect.width * 0.2
        for tile in self.collision_tiles:
            if pygame.sprite.collide_mask(self.player, tile):
                if self.player.last_pressed_direction == "right":
                    overlap = self.player.rect.right - tile.rect.left
                    if overlap > 0:
                        self.player.rect.right = tile.rect.left + player_center
                        self.player.can_move_right = False

                elif self.player.last_pressed_direction == "left":
                    overlap = self.player.rect.right - tile.rect.left
                    if overlap > 0:
                        self.player.rect.left = tile.rect.right - player_center
                        self.player.can_move_left = False
                collision_detected = True

        if not collision_detected:
            if self.player.last_pressed_direction == "right":
                self.player.can_move_left = True
                self.player.can_move_up = True
                self.player.can_move_down = True
            elif self.player.last_pressed_direction == "left":
                self.player.can_move_right = True
                self.player.can_move_up = True
                self.player.can_move_down = True

        return collision_detected

    def _handle_vertical_collision(self) -> bool:
        collision_detected = False
        player_center = self.player.rect.height * 0.2
        for tile in self.collision_tiles:
            if pygame.sprite.collide_mask(self.player, tile):
                if self.player.last_pressed_direction == "down":
                    overlap = self.player.rect.bottom - tile.rect.top
                    if overlap > 0:
                        self.player.rect.bottom = tile.rect.top + player_center
                        self.player.can_move_down = False

                elif self.player.last_pressed_direction == "up":
                    overlap = tile.rect.bottom - self.player.rect.top - player_center
                    if overlap > 0:
                        self.player.rect.top = tile.rect.bottom
                        self.player.can_move_up = False
                collision_detected = True

        if not collision_detected:
            if self.player.last_pressed_direction == "down":
                self.player.can_move_up = True
                self.player.can_move_left = True
                self.player.can_move_right = True
            elif self.player.last_pressed_direction == "up":
                self.player.can_move_down = True
                self.player.can_move_left = True
                self.player.can_move_right = True
        return collision_detected

    def _handle_horizontal_enemy_collision(self, enemy) -> bool:
        collision_detected = False
        enemy_center = enemy.rect.width * 0.2
        for tile in self.collision_tiles:
            if pygame.sprite.collide_mask(enemy, tile):
                if enemy.last_pressed_direction == "right":
                    overlap = enemy.rect.right - tile.rect.left
                    if overlap > 0:
                        enemy.rect.right = tile.rect.left
                        enemy.can_move_right = False
                elif enemy.last_pressed_direction == "left":
                    overlap = enemy.rect.left - tile.rect.right
                    if overlap > 0:
                        enemy.rect.left = tile.rect.right
                        enemy.can_move_left = False
                collision_detected = True

        if not collision_detected:
            if enemy.last_pressed_direction == "right":
                enemy.can_move_left = True
                enemy.can_move_up = True
                enemy.can_move_down = True
            elif enemy.last_pressed_direction == "left":
                enemy.can_move_right = True
                enemy.can_move_up = True
                enemy.can_move_down = True

        return collision_detected

    def _handle_vertical_enemy_collision(self, enemy) -> bool:
        collision_detected = False
        enemy_center = enemy.rect.height * 0.2
        for tile in self.collision_tiles:
            if pygame.sprite.collide_mask(enemy, tile):
                if enemy.last_pressed_direction == "down":
                    overlap = enemy.rect.bottom - tile.rect.top
                    if overlap > 0:
                        enemy.rect.bottom = tile.rect.top
                        enemy.can_move_down = False
                elif enemy.last_pressed_direction == "up":
                    overlap = tile.rect.bottom - enemy.rect.top
                    if overlap > 0:
                        enemy.rect.top = tile.rect.bottom
                        enemy.can_move_up = False
                collision_detected = True

        if not collision_detected:
            if enemy.last_pressed_direction == "down":
                enemy.can_move_up = True
                enemy.can_move_left = True
                enemy.can_move_right = True
            elif enemy.last_pressed_direction == "up":
                enemy.can_move_down = True
                enemy.can_move_left = True
                enemy.can_move_right = True

        return collision_detected

    def _handle_enemy_collisions(self) -> None:
        for enemy in self.enemies:
            vertical_collided = self._handle_vertical_enemy_collision(enemy)
            horizontal_collided = self._handle_horizontal_enemy_collision(enemy)
            if not vertical_collided and not horizontal_collided:
                enemy.is_colliding = False
            else:
                enemy.is_colliding = True
