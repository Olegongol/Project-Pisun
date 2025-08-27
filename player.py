import math
import pygame
from setting import player_angle_perframe, sprint
from game_object import GameObject

class Player(GameObject):
    def __init__(self, type: str, pos=(0, 0), angle=0.0, radius=0.0, speed=0.0):
        super().__init__(type, pos, angle)
        self.radius = radius
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
        self.speed = speed
        
    def collide_self_rect(self, new_x, new_y, game_map):
        test_rect = pygame.Rect(new_x - self.radius, new_y - self.radius, self.radius * 2, self.radius * 2)
        for obj in game_map:
            if obj.type == "w":
                if test_rect.colliderect(obj.rect):
                    return True
        return False

    def movement(self, game_map):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.angle -= player_angle_perframe
        if keys[pygame.K_RIGHT]:
            self.angle += player_angle_perframe

        dir_x = dir_y = 0.0
        if keys[pygame.K_w]:
            dir_x += cos_a
            dir_y += sin_a
        if keys[pygame.K_s]:
            dir_x -= cos_a
            dir_y -= sin_a
        if keys[pygame.K_a]:
            dir_x -= sin_a
            dir_y += cos_a
        if keys[pygame.K_d]:
            dir_x += sin_a
            dir_y -= cos_a

        speed_multiplier = sprint if keys[pygame.K_LSHIFT] else 1.0
        if dir_x or dir_y:
            length = math.hypot(dir_x, dir_y)
            delta_x = (dir_x / length) * self.speed * speed_multiplier
            delta_y = (dir_y / length) * self.speed * speed_multiplier
            if not self.collide_self_rect(self.x + delta_x, self.y, game_map):
                self.x += delta_x
            if not self.collide_self_rect(self.x, self.y + delta_y, game_map):
                self.y += delta_y