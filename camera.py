import math
import pygame
from game_object import GameObject
from player import Player

class Camera(GameObject):
    def __init__(self, type_: str, pos: tuple[int, int], zone: tuple[int, int, int, int]):
        super().__init__(type_, pos)
        self.set_zone(zone)

    def distance_to_object(self, object_pos: tuple[int, int]) -> float:
        return math.sqrt((self.x - object_pos[0]) ** 2 + (self.y - object_pos[1]) ** 2)

    def set_zone(self, zone: tuple[int, int, int, int]):
        self.rect = pygame.Rect(zone)

    def colliderect(self, player: Player) -> bool:
        return self.rect.colliderect(player.rect)