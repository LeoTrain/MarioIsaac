import pygame

class Scene:
    def __init__(self, engine):
        self.engine = engine
        self.running = True

    def enter(self):
        """Initialisation of the scene."""
        pass

    def exit(self):
        """Cleaning the scene"""
        pass

    def handle_events(self):
        """Handle scenes"""
        pass

    def update(self, dt):
        """Handle events"""
        pass

    def render(self):
        """Show scenes."""
        pass
