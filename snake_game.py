import tkinter, time

from entities.snake import Snake
from engine import *



root = tkinter.Tk()
root.resizable(width=False, height=False)
root.geometry(settings.ROOT_SIZE)
root.title(settings.GAME_TITLE)
root['bg'] = settings.ROOT_BG

canvas = tkinter.Canvas(root, width=600, height=600)

# ???
level_switch_variable = tkinter.IntVar()
level_switch_variable.set(None)

# ???
already_placed_buttons = []

in_game = False
user_snake = Snake(root)
current_level = None


## ??

def change_level():
    global in_game
    global current_level

    current_level_index = level_switch_variable.get()
    in_game = False

    current_level = Levels[current_level_index]
    restart(user_snake, current_level, current_level_index)

    in_game = True
    play(root, canvas, current_level, user_snake,current_level_index)

def play(root, canvas, current_level, user_snake, level_index):
    global in_game

    while in_game:
        root.update()
        root.update_idletasks()

        canvas.delete('all')

        # draw objects
        for list, color in [[current_level.food, settings.COLOR_FOOD],
                            [current_level.walls, settings.COLOR_WALL],
                            [current_level.bombs, settings.COLOR_BOMB],
                            [current_level.win_point, settings.COLOR_WIN_POINT],
                            [user_snake.snake, settings.COLOR_SNAKE]]:
            draw(canvas, list, color)

        # logic
        if user_snake.is_error() or (user_snake.head() in current_level.walls):
            in_game = False
        else:
            if user_snake.head() in current_level.win_point:

                progress = read_progress()
                progress[str(level_index + 1)] = '1'
                update_progress(progress)

                place_level_button(already_placed_buttons)
                return
            user_snake.move()
            current_level.spawn_food()
            if user_snake.head() in current_level.food:
                current_level.food.remove(user_snake.head())
                user_snake.grow()

            if user_snake.head() in current_level.bombs:
                current_level.bombs.remove(user_snake.head())
                user_snake.damage(settings.DAMAGE_BOMB)

            time.sleep(0.1 if in_game else 0)

def place_level_button(already_placed_buttons):

    progress = read_progress()

    # draw buttons
    for button in settings.buttons:

        if button.value in already_placed_buttons:
            continue

        if progress[str(button.value)] == '1':
            tkinter.Radiobutton(root, text=button.name, variable=level_switch_variable,
                                indicatoron=False, value=button.value, width=8,
                                command=change_level).place(anchor=tkinter.NW, rely=button.relY)
            already_placed_buttons.append(button.value)


place_level_button(already_placed_buttons)
canvas.pack(side=tkinter.BOTTOM)
root.mainloop()