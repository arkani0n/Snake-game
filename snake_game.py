import tkinter
import time

import settings
from entities.snake import Snake
import engine
import levels
from tkinter import messagebox


# ============= Functions


def start():
    global user_name
    global for_labels

    if for_labels is not None:
        for_labels.destroy()

    else:
        user_name_label.destroy()

    user_name = user_name_entery.get()
    if user_name == '':
        for_labels = tkinter.Label(text='Enter your name please', bg='red')
        for_labels.place(rely=0.37, relx=0.4)
        return

    for i in settings.NOT_ALLOWED_SIMMONS:
        if i in user_name:
            if for_labels is not None:
                for_labels.destroy()
            for_labels = tkinter.Label(text='Not allowed symbol')
            for_labels.place(rely=0.37, relx=0.4)
            return

    start_game_button.destroy()
    user_name_entery.destroy()
    canvas.pack(side=tkinter.BOTTOM)
    engine.place_level_button(already_placed_buttons, level_switch_variable, change_level, root)


def play(root, canvas, current_level, user_snake, level_index):
    global for_labels
    global is_show_massagebox
    is_show_massagebox = True
    move_counter = 0
    spawn_after = 10

    if for_labels is not None:
        for_labels.destroy()

    if level_index == 3:
        lowest, all_scores, for_labels = engine.show_highscore(for_labels, root)
    elif level_index == 0:
        for_labels = engine.show_tutorial(root)
    while is_show_massagebox:
        root.update()
        root.update_idletasks()

        # logic
        if user_snake.is_error() or (user_snake.head() in current_level.walls):
            if level_index == 3:
                if user_snake.eaten >= lowest or len(all_scores) < 10:
                    all_scores.append(str(user_snake.eaten) + '=' + user_name)
                engine.update_data(all_scores)
                for_labels = engine.show_highscore(for_labels, root)[2]
            if is_show_massagebox:
                is_show_massagebox = False

                is_again = tkinter.messagebox.askquestion(
                    'game over', 'Game over \n \n Your score is: ' + str(
                        user_snake.eaten) + ' points \n \n Do you want to try again?')
                if is_again == 'yes':
                    is_show_massagebox = True

                    engine.restart(user_snake, current_level, level_index)
            else:
                break
        else:
            if user_snake.head() in current_level.win_point:
                progress = engine.read_data('progress')
                messagebox.showinfo('Level completed',
                                    'Congratulations! \n \n '
                                    'You successfully manage to complete the level \n '
                                    + ('\nNow next level in unlocked' if progress[str(level_index + 1)] == '0' else ''))

                progress[str(level_index + 1)] = '1'
                engine.update_progress(progress)
                engine.place_level_button(already_placed_buttons, level_switch_variable, change_level, root)

                is_show_massagebox = False

            user_snake.move()
            move_counter += 1

            current_level.spawn_food()
            if user_snake.head() in current_level.food:
                current_level.food.remove(user_snake.head())
                user_snake.grow()
                user_snake.eaten += 1

            if user_snake.head() in current_level.bombs:
                current_level.bombs.remove(user_snake.head())
                user_snake.damage(settings.DAMAGE_BOMB)

            if move_counter == spawn_after and level_index == 3:
                engine.add_piace(current_level, user_snake)
                move_counter = 0
                spawn_after += 1

            # draw objects
            if is_show_massagebox:
                canvas.delete('all')
                for list, color in [[current_level.food, settings.COLOR_FOOD],
                                    [current_level.walls, settings.COLOR_WALL],
                                    [current_level.bombs, settings.COLOR_BOMB],
                                    [current_level.win_point, settings.COLOR_WIN_POINT],
                                    [user_snake.snake, settings.COLOR_SNAKE]]:
                    engine.draw(canvas, list, color)

            time.sleep(settings.DALEY if is_show_massagebox else 0)


def change_level():
    global current_level

    current_level_index = level_switch_variable.get()

    current_level = levels.Levels[current_level_index]
    engine.restart(user_snake, current_level, current_level_index)

    play(root, canvas, current_level, user_snake, current_level_index)


root = tkinter.Tk()
root.resizable(width=False, height=False)
root.geometry(settings.ROOT_SIZE)
root.title(settings.GAME_TITLE)
root['bg'] = settings.ROOT_BG
canvas = tkinter.Canvas(root, width=600, height=600)

level_switch_variable = tkinter.IntVar()
level_switch_variable.set(None)

already_placed_buttons = []
is_show_massagebox = True
user_snake = Snake(root)
current_level = None
for_labels = None
user_name = None

user_name_entery = tkinter.Entry(root)
start_game_button = tkinter.Button(text='Start', command=start)
user_name_label = tkinter.Label(text='Enter your name')
user_name_label.place(rely=0.37, relx=0.4)
user_name_entery.place(rely=0.4, relx=0.4)
start_game_button.place(relx=0.45, rely=0.43)
root.mainloop()
