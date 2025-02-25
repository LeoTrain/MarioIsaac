from .collision_detector import CollisionDetector
from .collision_effect_handler import CollisionEffectHandler
from .collision_resolver import CollisionResolver
from typing import List
from ..entities.base_character import BaseCharacter
from ..entities.tile import Tile


class CollisionManager:
    def __init__(self):
        self.collision_detector = CollisionDetector()
        self.collision_resolver = CollisionResolver()
        self.collision_effect_handler = CollisionEffectHandler()

    def handle_collisions(self, entities:List[BaseCharacter], tiles:List[Tile]):
        for entity in entities:
            collided_tiles = self.collision_detector.detect_tile_collisions(entity, tiles)
            if collided_tiles:
                self.collision_resolver.resolve_tile_collision(entity, collided_tiles)
                entity.collided()
            else:
                entity.changeMoving(True)
                entity.stoppedColliding()

            for other_entity in entities:
                if entity != other_entity:
                    collision_vector = self.collision_detector.detect_entity_collision(entity, other_entity)
                    if collision_vector:
                        self.collision_resolver.resolve_entity_collision(entity, other_entity, collision_vector)
