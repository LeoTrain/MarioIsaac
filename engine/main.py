import pygame

class GameEngine:
    def __init__(self, width=800, height=600, title="My Game Engine"):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self, dt):
        pass

    def render(self):
        self.screen.fill((0, 0, 0))
        pygame.display.flip()

    def run(self, fps=60):
        while self.running:
            dt = self.clock.tick(fps) / 1000
            self.handle_events()
            self.update(dt)
            self.render()

        pygame.quit()
