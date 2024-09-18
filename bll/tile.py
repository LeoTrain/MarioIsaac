import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, display, image=None):
        super().__init__()
        self.display = display
        if image is not None:
            self.image = image
        else:
            self.image = pygame.Surface((128, 128))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.old_rect = self.rect.copy()
        self.max_offset = 200
        self.draw_rect_border = False
        self.color_mask = False

    def draw_mask(self, offset_x, offset_y, color=(128, 0, 128)):
        mask_surface = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
        width, height = self.mask.get_size()
        for x in range(width):
            for y in range(height):
                if self.mask.get_at((x, y)):
                    mask_surface.set_at((x, y), color)
        self.display.blit(
            mask_surface, (self.rect.x - offset_x, self.rect.y - offset_y)
        )

    def draw(self, offset_x, offset_y):
        self.display.blit(self.image, (self.rect.x - offset_x, self.rect.y - offset_y))
        if self.draw_rect_border:
            pygame.draw.rect(self.display, (255, 0, 0), self.rect.move(-offset_x, -offset_y), 1)
        if self.color_mask:
            self.draw_mask(offset_x, offset_y)

    def update_old_rect(self):
        self.old_rect = self.rect.copy()
