import pygame

from ..entities.player import Player
from ..entities.goblin import Goblin
from ..levels.map import Map
from ..logic.collision_manager import CollisionManager
from ..logic.event_dick import event_dick
from ..core.loading_screen import LoadingScreen


class Level:
    def __init__(self, surface):
        self.surface = surface
        self._load_map("MarioIsaac/maps/level_one.tmx")
        self._initialise_components()
        self.camera_offset_x = self.player.position.x
        self.camera_offset_y = self.player.position.y
        self.level_finished = False

    def run(self, event_handler):
        self._update(event_handler)
        self._render()

    def _update(self, event_handler):
        event_handler.handle()
        self._updateEnemyPositions()
        self.collision_manager.handle_collisions([self.player] + self.enemies, self.collision_tiles)
        self._updateSprites()
        self._did_player_win()
        self._update_camera()
        pygame.display.update()

    def _load_map(self, map_path):
        self.game_map = Map(map_path)
        self.collision_tiles = self.game_map.get_collision_tiles(self.surface)

    def _initialise_components(self):
        self._initialise_images()
        self._initialise_player()
        self._initialise_enemies()
        self.collision_manager = CollisionManager()
        self.all_sprites = pygame.sprite.Group()

    def _initialise_images(self):
        heart_alive_image = pygame.image.load(
            "MarioIsaac/assets/tileset/hearts/heart_red.png"
        )
        heart_dead_image = pygame.image.load(
            "MarioIsaac/assets/tileset/hearts/heart_black.png"
        )
        self.heart_alive_image = pygame.transform.scale(heart_alive_image, (32, 32))
        self.heart_dead_image = pygame.transform.scale(heart_dead_image, (32, 32))

    def _initialise_player(self):
        sprite_sheet_path = (
            "MarioIsaac/assets/sprites/base_character/my_base_character_v3.png"
        )
        self.player = Player(self.surface, sprite_sheet_path, set_position=self.game_map.get_player_starting_position())
        self.player.mask = pygame.mask.from_surface(self.player.image)

    def _initialise_enemies(self):
        sprite_sheet_path = "MarioIsaac/assets/sprites/orcs/my_goblin_v1.png"
        starting_positions = self.game_map.get_enemy_starting_position("goblin")
        self.enemies = [
            Goblin(self.surface, sprite_sheet_path, set_position=pos)
            for pos in starting_positions
        ]

    def reset_level(self):
        font = pygame.font.Font(None, 36)
        loading_screen = LoadingScreen(self.surface, font, total_steps=4)
        steps = [
            self._initialise_images,
            self._initialise_enemies,
            self._initialise_player,
        ]
        for step in steps:
            step()
            loading_screen.increment_step()
            loading_screen.update()

    def _update_camera(self):
        self.camera_offset_x = self.player.rect.centerx - self.surface.get_width() // 2
        self.camera_offset_y = self.player.rect.centery - self.surface.get_height() // 2

    def _render(self):
        self.surface.fill((92, 82, 71))
        self.game_map.render(self.surface, self.camera_offset_x, self.camera_offset_y)
        self.player.draw(self.camera_offset_x, self.camera_offset_y)
        self.player.draw_xp_bar(self.surface)
        for enemy in self.enemies:
            enemy.draw(self.camera_offset_x, self.camera_offset_y)
        self._draw_hearts()

    def _draw_hearts(self):
        dead_hearts = self.player.max_life_points - self.player.life_points
        heart_width = self.heart_alive_image.get_width()
        x_pos = self.surface.get_width() - heart_width
        for _ in range(self.player.life_points):
            x_pos -= heart_width
            self.surface.blit(self.heart_alive_image, (x_pos, 50))
        for _ in range(dead_hearts):
            x_pos -= heart_width
            self.surface.blit(self.heart_dead_image, (x_pos, 50))

    def _did_player_win(self):
        if not self.enemies:
            pygame.event.post(pygame.event.Event(event_dick["player_won"]))
            pass
            

    def _updateSprites(self):
        self.player.updateSprite()
        self._updateEnemySprites()

    def _updateEnemyPositions(self):
        for enemy in self.enemies:
            enemy.move_to_player(self.player.position)

    def _updateEnemySprites(self):
        for enemy in self.enemies:
            enemy.updateSprite()
