import pygame
from .levels.map import Map
from .bll.player import Player


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Test Map Tiled")

map_file = "MarioIsaac/maps/level_one.tmx"
game_map = Map(map_file)
collision_tiles = game_map.get_collision_tiles(screen)
for tile in collision_tiles:
    print(tile)
all_collideball_tiles = collision_tiles
player_starting_position = game_map.get_player_starting_position()


sprite_sheet_path = "MarioIsaac/assets/sprites/base_character/my_base_character_v2.png"
player = Player(screen, sprite_sheet_path)
print(player_starting_position)
player.rect.topleft = player_starting_position

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    game_map.render(screen)
    player.draw(0, 0)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
