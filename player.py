import math
import pygame
from game_object import GameObject
from setting import player_angle_perframe, player_sprint

class Player(GameObject):
    def __init__(self,
                 type_: str,
                 pos: tuple[int, int],
                 radius: float,
                 speed: float,
                 angle: float):
        super().__init__(type_, pos)
        self.radius = radius
        self.rect = pygame.Rect(self.x - self.radius,
                                self.y - self.radius,
                                self.radius * 2,
                                self.radius * 2)
        self.speed = speed
        self.angle = angle

    def _update_rect(self) -> None:
        self.rect.x = int(self.x - self.radius)
        self.rect.y = int(self.y - self.radius)

    def collide_self_rect(self, new_x: float, new_y: float, game_map) -> bool:
        test_rect = pygame.Rect(int(new_x - self.radius),
                                int(new_y - self.radius),
                                int(self.radius * 2),
                                int(self.radius * 2))
        for obj in game_map:
            if obj.type == "w":
                if test_rect.colliderect(obj.rect):
                    return True
        return False

    def movement(self, game_map) -> None:
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:  # K_LEFT
            self.angle -= player_angle_perframe
        if keys[pygame.K_d]:  # K_RIGHT
            self.angle += player_angle_perframe

        dir_x = dir_y = 0.0
        if keys[pygame.K_w]:
            dir_x += cos_a
            dir_y += sin_a
        if keys[pygame.K_s]:
            dir_x -= cos_a
            dir_y -= sin_a
        # if keys[pygame.K_a]:
            # dir_x += sin_a
            # dir_y -= cos_a
        # if keys[pygame.K_d]:
            # dir_x -= sin_a
            # dir_y += cos_a

        speed_multiplier = player_sprint if keys[pygame.K_LSHIFT] else 1.0
        if dir_x or dir_y:
            length = math.hypot(dir_x, dir_y)
            if length == 0:
                return
            delta_x = (dir_x / length) * self.speed * speed_multiplier
            delta_y = (dir_y / length) * self.speed * speed_multiplier
            if not self.collide_self_rect(self.x + delta_x, self.y, game_map):
                self.x += delta_x
            if not self.collide_self_rect(self.x, self.y + delta_y, game_map):
                self.y += delta_y
            self._update_rect()