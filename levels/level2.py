from ..levels.level import Level


class Level2(Level):
    def __init__(self, surface):
        self.surface = surface
        self._load_map("MarioIsaac/maps/level_two.tmx")
        self._initialise_components()
        self.camera_offset_x = self.player.rect.topleft[0]
        self.camera_offset_y = self.player.rect.topleft[1]
        self.level_finished = False
