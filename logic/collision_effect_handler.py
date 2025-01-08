from ..entities.player import Player


class CollisionEffectHandler:
    def handle_entity_collision_effects(self, entity1, entity2):
        if entity1.can_attack() and not isinstance(entity1, Player):
            entity1.attack(entity2)
        if entity2.can_attack() and not isinstance(entity2, Player):
            entity2.attack(entity1)
