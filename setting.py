# GAME
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
HALF_WINDOW_WIGHT = WINDOW_WIDTH // 2
HALF_WINDOW_HEIGHT = WINDOW_HEIGHT // 2
FPS = 60
BLOCK_SIDE = 25
HALF_BLOCK_SIDE = BLOCK_SIDE / 2

# CAMERA
camera_pos = (HALF_WINDOW_WIGHT, HALF_WINDOW_HEIGHT)
camera_zone_rect = (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)

# PLAYER
player_pos = (HALF_WINDOW_WIGHT, HALF_WINDOW_HEIGHT)
player_radius = BLOCK_SIDE / 3
player_speed = BLOCK_SIDE / 10
player_sprint = 1.2
player_angle = 0
player_angle_perframe = 0.07