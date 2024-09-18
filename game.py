import pygame

from .levels.level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.DEAD = pygame.USEREVENT + 1
        self.display_width, self.display_height = 800, 600
        self.display = pygame.display.set_mode(
            (self.display_width, self.display_height)
        )
        self.running = True
        self.clock = pygame.time.Clock()
        self.fps = 60

        self.level = Level(self.display)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    self.level.player.draw_rect_border = not self.level.player.draw_rect_border
                elif event.key == pygame.K_p:
                    self.level.player.color_mask = not self.level.player.color_mask
                elif event.key == pygame.K_k:
                    for entity in self.level.enemies:
                        entity.draw_rect_border = not entity.draw_rect_border
                elif event.key == pygame.K_l:
                    for entity in self.level.enemies:
                        entity.color_mask = not entity.color_mask
                elif event.key == pygame.K_SPACE:
                    self.level.player.attack()
            elif event.type == self.DEAD:
                self.running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.level.player.move(-1, 0)
            self.level.player.current_x_direction = "left"
            self.level.player.current_y_direction = "down"
            self.level.player.last_pressed_direction = "left"
        elif keys[pygame.K_d]:
            self.level.player.move(1, 0)
            self.level.player.current_x_direction = "right"
            self.level.player.current_y_direction = "down"
            self.level.player.last_pressed_direction = "right"
        elif keys[pygame.K_w]:
            self.level.player.move(0, -1)
            self.level.player.current_y_direction = "up"
            self.level.player.last_pressed_direction = "up"
        elif keys[pygame.K_s]:
            self.level.player.move(0, 1)
            self.level.player.current_y_direction = "down"
            self.level.player.last_pressed_direction = "down"

    def run(self):
        while self.running:
            self.handle_events()
            self.level.update()
            self.level.render()

            self.clock.tick(self.fps)
        pygame.quit()
