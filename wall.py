import pygame
from game_object import GameObject

class Wall(GameObject):
    def __init__(self, type_: str, pos: tuple[int, int], wh: tuple[int, int]):
        super().__init__(type_, pos)
        self.rect = pygame.Rect(pos, wh)