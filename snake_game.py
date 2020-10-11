import tkinter, time

import settings

from entities.snake import Snake
from levels import *

# ============= Functions
def restart(snake, level, num):
    snake.snake = [[10, 10], [10, 20], [10, 30]]
    snake.eaten = 0
    snake.direction = 'right'
    level.food = [[-10, -10]]
    level.bombs = bombs[num].copy()


def draw(canvas, list, color):
    for i in range(len(list)):
        canvas.create_rectangle(
            list[i][0], list[i][1], list[i][0] + 10, list[i][1] + 10, fill=(color))


def change_level():
    global in_game
    global current_level
    curent_level_index=switch_variable.get()
    in_game = False
    current_level = Levels[curent_level_index]
    restart(user_snake, current_level, curent_level_index)
    in_game = True
    play(root, canvas, current_level, user_snake,curent_level_index)


def play(root, canvas, current_level, user_snake, level_index):
    global in_game
    end = 0

    while in_game:
        root.update()
        root.update_idletasks()

        canvas.delete('all')
        for list, color in [[current_level.food, settings.COLOR_FOOD],
                            [current_level.walls, settings.COLOR_WALL],
                            [current_level.bombs, settings.COLOR_BOMB],
                            [current_level.win_point, settings.COLOR_WIN_POINT],
                            [user_snake.snake, settings.COLOR_SNAKE]]:
            draw(canvas, list, color)
        if len(user_snake.snake) == 0 or (user_snake.eror() or user_snake.snake[0] in current_level.walls):
            in_game = False
        else:
            if user_snake.snake[0] in current_level.win_point:
                progress[str(level_index+1)]='1'
                update_progress()
                place_level_button()
                return
            user_snake.move()
            current_level.spawn_food()
            if user_snake.snake[0] in current_level.food:
                current_level.food.remove(user_snake.snake[0])
                user_snake.grow()

            if user_snake.snake[0] in current_level.bombs:
                current_level.bombs.remove(user_snake.snake[0])
                user_snake.damage(settings.DAMAGE_BOMB)

            time.sleep(0.1 if in_game else 0)


# ========== Progress

def place_level_button():
    with open(settings.USER_PROGRESS_FILE, 'r+') as file:
        for i in file.readlines():
            i=i.strip().split('=')
            progress[i[0]]=i[1]
        print(progress)
        for i in for_buttons:
            if i[0] in already_placed:
                continue
            if int(progress[str(i[2])]):
                tkinter.Radiobutton(root, text=i[0], variable=switch_variable,
                            indicatoron=False, value=i[2], width=8,
                            command=change_level).place(anchor=tkinter.NW, rely=i[1])
                already_placed.append(i[2])

def update_progress():
    with open(settings.USER_PROGRESS_FILE,'w') as file:
        for i in progress:
            file.write(i+'='+progress[i])
            file.write('\n')


# ========================== ROOT WINDOW SETTINGS
root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=600, height=600)
root.resizable(width=False, height=False)
root.geometry(settings.ROOT_SIZE)
root.title(settings.GAME_TITLE)
root['bg'] = settings.ROOT_BG

switch_variable = tkinter.IntVar()
switch_variable.set(None)
for_buttons = [("Tutorial", 0.26, 0),
               ("Level  1", 0.30, 1),
               ("Level  2", 0.34, 2),
               ("Level  3", 0.38, 3),
               ]

already_placed = []
canvas.pack(side=tkinter.BOTTOM)
in_game = False
user_snake = Snake(root)
current_level = None
progress = {}
place_level_button()
root.mainloop()
