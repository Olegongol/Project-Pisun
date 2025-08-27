import sys
import pygame
from setting import (
    WINDOW_WIGHT,
    WINDOW_HEIGHT,
    HALF_BLOCK_SIDE,
    camera_pos,
    camera_angle,
    player_pos,
    player_angle,
    player_speed,
    FPS)
from maps import dict_rooms
from drawing import Drawing
from camera import Camera
from player import Player


pygame.init()
window = pygame.display.set_mode((WINDOW_WIGHT, WINDOW_HEIGHT))
drawing = Drawing(window)
clock = pygame.time.Clock()

camera = Camera("camera", camera_pos, camera_angle)
player = Player("player", player_pos, player_angle, HALF_BLOCK_SIDE / 2, player_speed)

drawing.set_game_map(dict_rooms["room_1"])
drawing.set_camera(camera)
drawing.set_player(player)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill((200, 200, 200))

    drawing.drawing_game_map()
    drawing.drawing_camera()
    drawing.drawing_player()

    player.movement(drawing.game_map)

    pygame.display.flip()
    clock.tick(FPS)