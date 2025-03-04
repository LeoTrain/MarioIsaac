import pygame
from ..engine.Scene import Scene
from ..engine.GameScene import GameScene

class MenuScene(Scene):
    def __init__(self, engine):
        super().__init__(engine)
        self.font = pygame.font.Font(None, 74)
        self.small_font = pygame.font.Font(None, 36)
        self.options = ["Start", "Options", "Quit"]
        self.selected_option = 0

    def enter(self):
        print("Menu entered")

    def exit(self):
        print("Menu quitted")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.select_option()
                if event.key == pygame.K_DOWN:
                    self.selected_option = (self.selected_option + 1) % len(self.options)
                if event.key == pygame.K_UP:
                    self.selected_option = (self.selected_option - 1) % len(self.options)

    def select_option(self):
        if self.selected_option == 0:
            self.engine.change_scene(GameScene(self.engine))
        elif self.selected_option == 1:
            print("Opening options...")
        elif self.selected_option == 2:
            pygame.quit()
            sys.exit()

    def update(self, dt):
        pass

    def draw_title(self):
        title_text = self.font.render("My Game", True, (255, 255, 255))
        self.engine.screen.blit(title_text, (self.engine.screen.get_width() // 2 - title_text.get_width() // 2, 100))

    def draw_menu(self):
        for index, option in enumerate(self.options):
            color = (255, 0, 0) if index == self.selected_option else (255, 255, 255)
            text = self.small_font.render(option, True, color)
            x_pos = self.engine.screen.get_width() // 2 - text.get_width() // 2
            y_pos = 200 + index * 60
            self.engine.screen.blit(text, (x_pos, y_pos))

    def render(self):
        self.engine.screen.fill((0, 0, 0))
        self.draw_title()
        self.draw_menu()
        pygame.display.flip()
