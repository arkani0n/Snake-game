from entities.buttonData import ButtonData

GAME_TITLE = "SNAKE"
USER_PROGRESS_FILE = "user_progress.txt"
HIGHSCORE_FILE='high_score.txt'

NOT_ALLOWED_SIMMONS= ' \\/,.:;\'\"=-+_!@#$%^&*()~`|{[}]<>?'
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
    ButtonData("Survival", 0.38, 3),
]



# gameplay
DAMAGE_BOMB = 1
DALEY=0.15

for_tutorial='Use W A S D to move \n' \
             'green squares is food, eat them to grow \n' \
             'red squares is bombs they will decrease ' \
             'your length by ' + str(DAMAGE_BOMB) + '\n' \
            'blue squares is walls hiting them will make ' \
            'your game over'

pieces=[[[0,0],[10,0],[20,0],[30,0],[40,0],[50,0]],

        [[0,0],[0,10],[0,20],[0,30],[0,40],[0,50]],

        [[0,0],[0,10],[0,20],[10,20],[20,20]],

        [[0,0],[10,0],[10,10],[0,10]],

        [[0,0],[10,10],[20,0],[30,10],[40,0],[50,10]],

        [[0, 0], [0, 10], [0, 20], [10, 0], [20, 0]],

        [[40, 0], [50, 0], [60, 0], [60, 10], [60, 20]],

        [[20, 0], [20, 10], [20, 20], [10, 20], [0, 20]],

        [[0, 0], [10, 10], [0, 20], [10, 30], [0, 40]]
        ]

