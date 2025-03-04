from .engine.main import GameEngine
from .engine.MenuScene import MenuScene

if __name__ == "__main__":
    engine = GameEngine()

    menu_scene = MenuScene(engine)
    engine.change_scene(menu_scene)

    engine.run()
