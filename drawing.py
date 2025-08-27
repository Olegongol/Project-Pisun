import math
import pygame
from setting import HALF_BLOCK_SIDE
from camera import Camera
from player import Player

class Drawing():
    def __init__(self, window:pygame.display):
        self.window = window

    def set_game_map(self, game_map:set):
        self.game_map = game_map

    def drawing_game_map(self):
        for obj in self.game_map:
            if obj.type == "w":
                pygame.draw.rect(self.window, (100, 100, 100), obj.rect)
    
    def set_camera(self, camera:Camera):
        self.camera = camera
        self.camera_font = pygame.font.Font(None, 25)

    def drawing_camera(self):
        pygame.draw.circle(self.window, (0, 200, 0), self.camera.pos, HALF_BLOCK_SIDE/2)
        text_surface = self.camera_font.render(f"{self.camera.distance_to_object(self.player.pos):.2f}", True, (0, 0, 0))
        self.window.blit(text_surface, self.camera.pos)

    def set_player(self, player:Player):
        self.player = player

    def drawing_player(self):
        pygame.draw.line(self.window, (0, 0, 200), self.player.pos,
                         (self.player.x+math.cos(self.player.angle)*HALF_BLOCK_SIDE, self.player.y+math.sin(self.player.angle)*HALF_BLOCK_SIDE))
        pygame.draw.circle(self.window, (0, 0, 200), self.player.pos, HALF_BLOCK_SIDE/2)