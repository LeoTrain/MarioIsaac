import pygame

class GameEngine:
    def __init__(self, width=800, height=600, title="My Game Engine"):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = True
        self.all_sprites = pygame.sprite.Group()
        self.current_scene = None
        self.scene_stack = []

    def add_object(self, obj):
        self.all_sprites.add(obj)

    def change_scene(self, scene):
        if self.current_scene:
            self.current_scene.exit()
        self.scene_stack.append(self.current_scene)
        self.current_scene = scene
        self.current_scene.enter()

    def pop_scene(self):
        if len(self.scene_stack) > 0:
            self.current_scene.exit()
            self.current_scene = self.scene_stack.pop()
            self.current_scene.enter()

    def handle_events(self):
        self.current_scene.handle_events()
        self.running = self.current_scene.running

    def update(self, dt):
        self.current_scene.update(dt)

    def render(self):
        self.current_scene.render()

    def run(self, fps=60):
        while self.running:
            dt = self.clock.tick(fps) / 1000
            self.handle_events()
            self.update(dt)
            self.render()

        pygame.quit()
