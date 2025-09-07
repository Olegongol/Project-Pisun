import sys
import pygame
from setting import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    camera_pos,
    camera_zone_rect,
    player_pos,
    player_radius,
    player_speed,
    player_angle,
    FPS)
from maps import dict_rooms
from drawing import Drawing
from camera import Camera
from player import Player


pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
drawing = Drawing(window)
clock = pygame.time.Clock()

camera = Camera("c", camera_pos, camera_zone_rect)
player = Player("p", player_pos, player_radius, player_speed, player_angle)

drawing.set_game_map(dict_rooms["test_room"])
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