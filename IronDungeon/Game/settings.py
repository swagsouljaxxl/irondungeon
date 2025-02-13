import os
from .utils import resource_path


# General Settings
SCREEN_HEIGHT = 480
SCREEN_WIDTH = int(SCREEN_HEIGHT * 16 / 9)

FINAL_HEIGHT = 480
FINAL_WIDTH = int(FINAL_HEIGHT * 16 / 9)

FULLSCREEN = False
SHOW_FPS = False

WIN_TITLE = "Iron Dungeon"
FPS = 60

# Game Constants
jump_time = 0.75
jump_height = 64+16
t = jump_time/2
GRAVITY = int((2*jump_height)/(t*t))
PLAYER_JUMP_SPEED = int((2*jump_height)/t)
PLAYER_WALK_SPEED = int(32*6/jump_time)

# terminal velocity
TERMINAL_V = 700

MAX_COLLISION_STEP_SIZE = 8
MIN_SLOPE_DIST = 0

# Debug toggles
DEBUG_DRAW = False
DEBUG_DRAW_COLOR = (255, 0, 255)

# Resource Folders
resource_folder = resource_path('Resources')
img_folder = os.path.join(resource_folder, 'images')
music_folder = os.path.join(resource_folder, 'music')
font_folder = os.path.join(resource_folder, 'font')
levels_folder = os.path.join(resource_folder, 'levels')
