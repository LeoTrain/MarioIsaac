import pygame
from ..engine.MovableObject import MovableObject
from ..engine.Scene import Scene

class GameScene(Scene):
    def __init__(self, engine):
        super().__init__(engine)

    def enter(self):
        self.player = MovableObject(100, 100, 50, 50, (255, 0, 0))
        self.engine.add_object(self.player)

    def exit(self):
        self.engine.remove_object(self.player)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self, dt):
        self.player.update(dt)

    def render(self):
        self.engine.screen.fill((0, 0, 0))
        self.engine.all_sprites.draw(self.engine.screen)
        pygame.display.flip()
