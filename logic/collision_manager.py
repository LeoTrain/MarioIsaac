from .collision_detector import CollisionDetector
from .collision_effect_handler import CollisionEffectHandler
from .collision_resolver import CollisionResolver
from ..entities.player import Player


class CollisionManager:
    def __init__(self):
        self.collision_detector = CollisionDetector()
        self.collision_resolver = CollisionResolver()
        self.collision_effect_handler = CollisionEffectHandler()

    def handle_collisions(self, entities, tiles):
        for entity in entities:
            collided_tiles = self.collision_detector.detect_tile_collisions(entity, tiles)
            if collided_tiles:
                self.collision_resolver.resolve_tile_collision(entity, collided_tiles)
            else:
                entity.can_move_up = True
                entity.can_move_down = True
                entity.can_move_left = True
                entity.can_move_right = True
                    
            for other_entity in entities:
                if entity != other_entity:
                    if self.collision_detector.detect_entity_collision(entity, other_entity):
                        self.collision_resolver.resolve_entity_collision(entity, other_entity)
                        self.collision_effect_handler.handle_entity_collision_effects(entity, other_entity)


