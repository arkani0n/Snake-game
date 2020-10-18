from entities.buttonData import ButtonData

GAME_TITLE = "SNAKE"
USER_PROGRESS_FILE = "user_progress.txt"

ROOT_SIZE = "800x700" # Full window size
ROOT_BG = "black"

CANVAS_SIZE = "600x600"

COLOR_BOMB = "red"
COLOR_FOOD = "green"
COLOR_SNAKE = "black"
COLOR_WALL = "blue"
COLOR_WIN_POINT = "yellow"

buttons = [
    ButtonData("Tutorial", 0.26, 0),
    ButtonData("Level  1", 0.30, 1),
    ButtonData("Level  2", 0.34, 2),
    ButtonData("Level  3", 0.38, 3),
]

# gameplay
DAMAGE_BOMB = 2
